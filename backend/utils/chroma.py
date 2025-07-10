
import chromadb

# ChromaDB Manager
class ChromaDBManager:
    def __init__(self, persist_dir="sss_vectors"):
        self.persist_dir = persist_dir
        self.collection = None
        self.is_loaded = False
        
    def load(self):
        """Load existing ChromaDB"""
        try:
            # Load ChromaDB
            self.client = chromadb.PersistentClient(path=self.persist_dir)
            self.collection = self.client.get_collection("sss_documents")
            
            doc_count = self.collection.count()
            print(f"✓ ChromaDB loaded with {doc_count} documents")
            self.is_loaded = True
            return True
            
        except Exception as e:
            print(f"Error loading ChromaDB: {e}")
            self.is_loaded = False
            return False
    
    def search(self, query_embedding, k=3):
        """Search for relevant documents"""
        if not self.is_loaded:
            return []
        
        results = self.collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=k,
            include=["documents", "metadatas", "distances"]
        )
        
        formatted_results = []
        if results['documents'] and results['documents'][0]:
            for doc, meta, dist in zip(
                results['documents'][0],
                results['metadatas'][0],
                results['distances'][0]
            ):
                formatted_results.append({
                    "content": doc,
                    "source": meta.get("source", ""),
                    "relevance": 1 - dist
                })
        
        return formatted_results
