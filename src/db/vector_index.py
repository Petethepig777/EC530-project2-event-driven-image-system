import faiss
import numpy as np


class VectorIndex:
    def __init__(self, dimension=4):
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)
        self.image_ids = []

    def add_embedding(self, image_id: str, embedding: list):
        vector = np.array([embedding]).astype("float32")
        self.index.add(vector)
        self.image_ids.append(image_id)

    def search(self, query_embedding: list, top_k: int = 3):
        if self.index.ntotal == 0:
            return []

        query = np.array([query_embedding]).astype("float32")
        distances, indices = self.index.search(query, top_k)

        results = []
        for distance, index in zip(distances[0], indices[0]):
            if index == -1:
                continue
            results.append({
                "image_id": self.image_ids[index],
                "distance": float(distance)
            })

        return results
        