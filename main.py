from fastapi import FastAPI
from qdrant_client import QdrantClient, models
from sentence_transformers import SentenceTransformer
import pandas as pd
import json

app = FastAPI()

# Load and preprocess data
df = pd.read_csv("/app/data/food_rows.csv")
df.fillna("", inplace=True)  # Handle NaN values
data = df.to_dict("records")

# Initialize Qdrant
encoder = SentenceTransformer("all-MiniLM-L6-v2")
qdrant = QdrantClient("qdrant", port=6333)

qdrant.recreate_collection(
    collection_name="recipes",
    vectors_config=models.VectorParams(
        size=encoder.get_sentence_embedding_dimension(),
        distance=models.Distance.COSINE
    )
)

# Upload data to Qdrant
qdrant.upload_points(
    collection_name="recipes",
    points=[
        models.PointStruct(
            id=idx,
            vector=encoder.encode(doc["Name"]).tolist(),
            payload=doc,
        ) for idx, doc in enumerate(data)
    ]
)

@app.get("/search")
def search(query: str, limit: int = 3):
    query_vector = encoder.encode(query).tolist()
    hits = qdrant.search(
        collection_name="recipes",
        query_vector=query_vector,
        limit=limit
    )
    return [hit.payload for hit in hits]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

