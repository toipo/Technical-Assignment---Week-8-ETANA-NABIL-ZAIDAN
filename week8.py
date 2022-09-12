from typing import Collection
import pymongo
import uuid

client = pymongo.MongoClient("mongodb+srv://Eta66:<4eMb5uzWYYo9N5p9>@cluster0.x5jtdtw.mongodb.net/?retryWrites=true&w=majority")
db = client.database
collection = db.Cluster0

def locationn(kecepatan,latitude,longitude,timestamp):
    data = {
        "ID transaksi": str(uuid.uuid4()),
        "kecepatan": 90,
        "latitude": 6.2088,
        "longitude": 106.8456
        "timestamp": timestamp
    }
    records = collection.insert_one(data)
    print("data tersimpan",records)
