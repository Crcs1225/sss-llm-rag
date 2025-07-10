# create_export_script.py
import chromadb
import json
import os

def export_chromadb_to_json():
    # Load your existing ChromaDB
    client = chromadb.PersistentClient(path="./sss_vectors")
    collection = client.get_collection("sss_documents")
    
    # Get all data
    all_data = collection.get(
        include=["documents", "metadatas", "embeddings"]
    )
    
    # Prepare export data
    export_data = {
        "documents": [],
        "total_count": len(all_data["documents"])
    }
    
    # Check if we have embeddings
    has_embeddings = all_data.get("embeddings") is not None and len(all_data["embeddings"]) > 0
    
    for i in range(len(all_data["documents"])):
        doc_data = {
            "id": all_data["ids"][i],
            "content": all_data["documents"][i],
            "metadata": all_data["metadatas"][i] if all_data.get("metadatas") else {},
        }
        
        # Handle embeddings properly
        if has_embeddings:
            # Convert numpy array to list if necessary
            embedding = all_data["embeddings"][i]
            if hasattr(embedding, 'tolist'):
                doc_data["embedding"] = embedding.tolist()
            else:
                doc_data["embedding"] = embedding
        else:
            doc_data["embedding"] = None
            
        export_data["documents"].append(doc_data)
    
    # Save to JSON
    with open("sss_documents_export.json", "w", encoding="utf-8") as f:
        json.dump(export_data, f, indent=2, ensure_ascii=False)
    
    print(f"Exported {len(export_data['documents'])} documents to sss_documents_export.json")
    
    # Print file size
    file_size = os.path.getsize("sss_documents_export.json") / (1024 * 1024)  # MB
    print(f"File size: {file_size:.2f} MB")
    
    # If file is too large, create a version without embeddings
    if file_size > 50:  # If larger than 50MB
        print("File is large. Creating a version without embeddings...")
        export_data_no_embeddings = {
            "documents": [],
            "total_count": len(all_data["documents"])
        }
        
        for i in range(len(all_data["documents"])):
            doc_data = {
                "id": all_data["ids"][i],
                "content": all_data["documents"][i],
                "metadata": all_data["metadatas"][i] if all_data.get("metadatas") else {},
            }
            export_data_no_embeddings["documents"].append(doc_data)
        
        with open("sss_documents_no_embeddings.json", "w", encoding="utf-8") as f:
            json.dump(export_data_no_embeddings, f, indent=2, ensure_ascii=False)
        
        no_emb_size = os.path.getsize("sss_documents_no_embeddings.json") / (1024 * 1024)
        print(f"No embeddings file size: {no_emb_size:.2f} MB")

if __name__ == "__main__":
    export_chromadb_to_json()