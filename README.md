Overview
This project implements an event-driven image annotation and retrieval system using Redis pub-sub architecture.
The system simulates image inference, stores annotation data in MongoDB, generates simulated embeddings, and uses FAISS for vector similarity search.
The main goal is to focus on software engineering design, service communication, and system architecture instead of training machine learning models.

System Pipeline
image.submitted
→ inference.completed
→ annotation.stored
→ embedding.created
→ final result received

Workflow
- main.py publishes image.submitted
- inference_service.py generates simulated labels
- annotation_service.py stores annotations in MongoDB
- embedding_service.py creates simulated embeddings and stores them in FAISS
- result_listener.py receives the final result
- query_demo.py demonstrates top-k retrieval using FAISS
Technologies Used
- Python
- Redis Cloud
- MongoDB Atlas
- FAISS
- Pytest
- python-dotenv

Environment Variables
Create a .env file:
REDIS_HOST=your_redis_host
REDIS_PORT=your_redis_port
REDIS_PASSWORD=your_redis_password
MONGO_URI=your_mongodb_connection_string
Do not upload .env to GitHub.

Installation
pip install -r requirements.txt
requirements.txt
redis
pytest
python-dotenv
pymongo
faiss-cpu

How to Run
Terminal 1
python -m src.services.inference_service
Terminal 2
python -m src.services.annotation_service
Terminal 3
python -m src.services.embedding_service
Terminal 4
python -m src.services.result_listener
Terminal 5
python main.py
This runs the full event-driven pipeline.

Query Demo
python query_demo.py
This shows FAISS top-k similarity search.

Testing
python -m pytest
Current result:
6 passed
