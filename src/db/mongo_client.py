import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()


class MongoDBClient:
    def __init__(self):
        self.client = MongoClient(os.getenv("MONGO_URI"))
        self.db = self.client["ec530_project2"]
        self.annotations = self.db["annotations"]

    def store_annotation(self, annotation: dict):
        return self.annotations.insert_one(annotation)

    def get_annotation_by_image_id(self, image_id: str):
        return self.annotations.find_one({"image_id": image_id})