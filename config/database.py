from pymongo import MongoClient

client = MongoClient('mongodb+srv://kasimsabir:AG8iendn9xJaOqHZ@python-fast-api.o61dqs5.mongodb.net/?retryWrites=true&w=majority&appName=python-fast-api')

db = client.todo_db
collection = db["todo_collection"]
