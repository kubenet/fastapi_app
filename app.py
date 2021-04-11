from random import randint
from fastapi import FastAPI
from fastapi.logger import logger
import mongo_config
import logging

logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='a',
                    format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')

app = FastAPI()
logger = logging.getLogger("app.error")


@app.get("/")
async def root():
    logger.info('Main Page: [Get request]')
    return {"message": "Hello World"}


@app.get("/about")
async def about():
    logger.info('About Page: [get request]')
    return {"message": "Page About"}


@app.get("/help")
async def faq():
    logger.info('HELP Page [get]')
    return {"message": "FAQ..."}


@app.post("/number/<value>")
async def post_number(value):
    logger.info('Number Page [post]')
    return {"message": value}


@app.get("/gnumber")
async def get_number():
    #    value = randint(1, 100)
    #    global db
    #    db.post.insert_one({"name": "Vasya", "number": value})
    #    logger.info(f'Get Number Page [get] {value}')
    return {"message": "Get Number Page [get]"}


@app.post("/newclient/<email>")
async def new_client(email):
    logger.info(f'Request to create a new client: {email}')
    result = mongo_config.init_client(email)
    if result["status"]:
        return {"message": email, "password": result["password"]}
    else:
        return result
