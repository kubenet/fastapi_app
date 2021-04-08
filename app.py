from fastapi import FastAPI
from pymongo import MongoClient
import datetime
import logging

logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

client = MongoClient('mongodb://localhost:27017/')
db = client.test
collection = db.posts


post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(db.list_collection_names())

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/about")
async def about():
    return {"message": "Page About"}

@app.get("/help")
async def help():
    return {"message": "FAQ..."}

@app.post("/number/<value>")
async def help(value):
    return {"message": value}

