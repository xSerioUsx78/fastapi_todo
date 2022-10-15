from pymongo import MongoClient


client = MongoClient()
database = client.get_database('todo_app')