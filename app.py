from random import random, randint
from fastapi import FastAPI
from fastapi.logger import logger
from pymongo import MongoClient
import datetime
import logging


logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')

client = MongoClient('mongodb://localhost:27017/')
db = client.test


post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

#posts = db.posts
#post_id = posts.insert_one(post).inserted_id
print(db.list_collection_names())

app = FastAPI()
logger = logging.getLogger("app.error")

@app.get("/")
async def root():
	db.posts({"name":"Vasya","status":"new_user"})
	logger.info('Main Page: [Get request]')
	return {"message": "Hello World"}

@app.get("/about")
async def about():
	logger.info('About Page: [get request]')
	return {"message": "Page About"}

@app.get("/help")
async def help():
	logger.info('HELP Page [get]')
	return {"message": "FAQ..."}

@app.post("/number/<value>")
async def help(value):
	logger.info('Number Page [post]')
	return {"message": value}

@app.get("/gnumber")
async def gnumber():
	value = randint(1,100)
	global db
	db.post.insert_one({"name": "Vasya", "number": value})
	logger.info(f'Get Number Page [get] {value}')
	return {"message": value}
