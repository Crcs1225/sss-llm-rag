# app.py
import os
import time
import json
from typing import Optional, List, Dict
from utils.chroma import ChromaDBManager
from utils.llm import LightweightLLM
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
import numpy as np

from dotenv import load_dotenv
load_dotenv('.env.local')


# For CPU inference
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"  # Force CPU

app = FastAPI(
    title="SSS AI Assistant - Free LLM Edition",
    description="Free, lightweight AI assistant for SSS queries",
    version="1.0.0"
)

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request/Response Models
class ChatRequest(BaseModel):
    query: str
    model: Optional[str] = "tinyllama"
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = 256
    use_rag: Optional[bool] = True

class ChatResponse(BaseModel):
    answer: str
    model_used: str
    context_used: bool
    response_time: float
    sources: List[str] = []

class SearchRequest(BaseModel):
    query: str
    top_k: Optional[int] = 3
    
# Global variables
llm = None
chromadb_manager = None
embedder = None

# Initialize on startup
@app.on_event("startup")
async def startup():
    global llm, chromadb_manager, embedder
    # Load environment variables
    from dotenv import load_dotenv
    load_dotenv('.env.local')
    print("Initializing SSS AI Assistant...")
    # Verify token is loaded
    token = os.getenv("HF_TOKEN")
    if token:
        print("✓ HF_TOKEN loaded successfully")
    else:
        print("⚠️ Warning: HF_TOKEN not found!")
    # Load embedding model (lightweight)
    print("Loading embedding model...")
    embedder = SentenceTransformer('all-MiniLM-L6-v2')
    
    # Load ChromaDB
    print("Loading ChromaDB...")
    chromadb_manager = ChromaDBManager()
    chromadb_manager.load()
    
    # Load LLM
    print("Loading LLM...")
    llm = LightweightLLM(hf_token=token)
    llm.load_model("tinyllama")  # TinyLlama for free tier
    
    print("✓ Initialization complete!")

# API Endpoints
@app.get("/")
async def root():
    """Redirect to docs"""
    return RedirectResponse(url="/docs")

@app.get("/health")
async def health():
    """Health check"""
    return {
        "status": "healthy",
        "llm_loaded": llm is not None and llm.model is not None,
        "chromadb_loaded": chromadb_manager is not None and chromadb_manager.is_loaded,
        "embedder_loaded": embedder is not None
    }

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Main chat endpoint"""
    start_time = time.time()
    context = ""
    sources = []
    
    try:
        # RAG search if enabled
        if request.use_rag and chromadb_manager and chromadb_manager.is_loaded:
            # Encode query
            query_embedding = embedder.encode(request.query)
            
            # Search
            results = chromadb_manager.search(query_embedding, k=3)
            
            # Build context
            if results:
                context_parts = []
                for result in results:
                    context_parts.append(result['content'])
                    if result['source']:
                        sources.append(result['source'])
                
                context = "\n\n".join(context_parts)
        
        # Build prompt
        # In your chat endpoint
        if context:
            prompt = f"Context: {context}\n\nQuestion: {request.query}"
        else:
            prompt = request.query
        
        # Generate response
        answer = llm.generate(
            prompt,
            temperature=request.temperature,
            max_tokens=request.max_tokens
        )
        
        response_time = time.time() - start_time
        
        return ChatResponse(
            answer=answer,
            model_used=llm.model_id,
            context_used=bool(context),
            response_time=round(response_time, 2),
            sources=list(set(sources))[:3]  # Unique sources
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/search")
async def search(request: SearchRequest):
    """Search documents"""
    if not chromadb_manager or not chromadb_manager.is_loaded:
        raise HTTPException(status_code=503, detail="Search not available")
    
    try:
        # Encode query
        query_embedding = embedder.encode(request.query)
        
        # Search
        results = chromadb_manager.search(query_embedding, request.top_k)
        
        return {
            "query": request.query,
            "results": results,
            "count": len(results)
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/models")
async def get_models():
    """Get available models"""
    available_models = llm.get_available_models()
    return {
        "available_models": available_models
    }
    
# Add this endpoint to your FastAPI app.py
@app.post("/switch-model/{model_id}")
async def switch_model(model_id: str):
    """Force switch to a different model"""
    global llm
    
    valid_models = ["deepseek", "llama", "mistral"]  # Updated model IDs
    if model_id not in valid_models:
        raise HTTPException(status_code=400, detail=f"Invalid model: {model_id}")
    
    try:
        # Load the new model with HF token if available
        llm = LightweightLLM(hf_token=os.getenv("HF_TOKEN"))
        success = llm.load_model(model_id)
        
        if success:
            return {"status": "success", "current_model": model_id}
        else:
            raise HTTPException(status_code=500, detail="Failed to load model")
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# For local testing
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)