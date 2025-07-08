from fastapi import FastAPI
from pydantic import BaseModel

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from langchain.llms import HuggingFacePipeline
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA

# === Embedding setup ===
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# === Load ChromaDB ===
db = Chroma(persist_directory="sss_chroma", embedding_function=embedding)

# === Load lightweight LLM (flan-t5-small) ===
model_id = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSeq2SeqLM.from_pretrained(model_id)

pipe = pipeline(
    "text2text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=512,
    do_sample=False
)

llm = HuggingFacePipeline(pipeline=pipe)

# === RAG Chain ===
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=db.as_retriever(),
    return_source_documents=True
)

# === FastAPI App ===
app = FastAPI()

class Question(BaseModel):
    query: str

@app.post("/ask")
def ask_question(data: Question):
    result = qa_chain({"query": data.query})
    return {
        "answer": result["result"],
        "sources": [doc.metadata["source"] for doc in result["source_documents"]]
    }
