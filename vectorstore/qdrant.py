from utils.data import qa_pairs
from encoder.encoder import model
from encoder.encoder import create_embedding
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
import numpy as np
# Assuming you have an embedding function

# Initialize Qdrant client
client = QdrantClient("localhost", port=6333)

# Create collection with appropriate vector size
client.create_collection(
    collection_name="kubernetes_qa",
    vectors_config=VectorParams(size=384, distance=Distance.COSINE)
)

# Process and upload each Q&A pair

for i, qa_pair in enumerate(qa_pairs):
    # Create embedding from the question
    question_embedding = create_embedding(qa_pair["question"])
    
    # Store the vector with complete Q&A as payload
    client.upsert(
        collection_name="kubernetes_qa",
        points=[
            PointStruct(
                id=i,
                vector=question_embedding,
                payload={
                    "question": qa_pair["question"],
                    "answer": qa_pair["answer"],
                    "topic": qa_pair["topic"],
                    "type": qa_pair["type"],
                    "difficulty": qa_pair["difficulty"]
                }
            )
        ]
    )
