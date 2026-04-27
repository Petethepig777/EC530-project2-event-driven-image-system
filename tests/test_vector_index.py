from src.db.vector_index import VectorIndex


def test_add_and_search_embedding():
    index = VectorIndex(dimension=4)

    index.add_embedding("img_001", [0.1, 0.2, 0.3, 0.4])
    index.add_embedding("img_002", [0.9, 0.8, 0.7, 0.6])

    results = index.search([0.1, 0.2, 0.3, 0.4], top_k=1)

    assert len(results) == 1
    assert results[0]["image_id"] == "img_001"