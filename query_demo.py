from src.db.vector_index import VectorIndex


def main():
    index = VectorIndex(dimension=4)

    index.add_embedding("img_001", [0.12, 0.45, -0.88, 0.31])
    index.add_embedding("img_002", [0.80, 0.10, -0.20, 0.44])
    index.add_embedding("img_003", [0.05, 0.40, -0.90, 0.28])

    query_embedding = [0.10, 0.44, -0.86, 0.30]

    results = index.search(query_embedding, top_k=2)

    print("Top search results:")
    for result in results:
        print(result)


if __name__ == "__main__":
    main()