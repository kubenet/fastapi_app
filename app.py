from random import randint
from fastapi import FastAPI
from fastapi.logger import logger
import mongo_config
import logging
from schemes import Sensor, User, Device

logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='a',
                    format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')

app = FastAPI()
logger = logging.getLogger("app.error")


@app.get("/")
@app.get("/index")
@app.get("/main")
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


@app.post("/registration/{email, passwd}")
async def registration(email):
    logger.info(f'Receive request to create a new client: {email}')
    try:
        result = mongo_config.init_client(email)
    except:
        logger.error(f'Receive request to create a new client: {email}')
    if result["status"]:
        return {"message": email, "password": result["password"]}
    else:
        return result


@app.post("/test_user")
async def test(new_user: User):
    return {"new user": new_user}


######

# Создать устройство [device]
@app.post("/{user}/new_device/{name_device}")
async def test(sensor: Sensor):
    return {"status": "ok"}, 200


# получить информацию об одном устройстве [device]
@app.get("/{user}/{deviceName}")
async def test(sensor: Sensor):
    return {"status": "ok"}, 200


# получить список всех устройств юзера [devices]
@app.get("/{user}/devices")
async def test(user: User):
    return {"activeDevices": ["device1", "device2", "device3"],
            "inactiveDevices": ["device4", "device5"], "version": "ver 0.1"}, 200


# Добавить датчик к устройству [device] в поле [sensor]
@app.post("/{user}/deviceName/new_sensor")
async def test(sensor: Sensor):
    return {"status": "ok"}, 200


# изменить датчик к устройству [device] в поле [sensor]
@app.post("/{user}/device/{id}/new_sensor")
async def test(sensor: Sensor):
    return {"status": "ok"}, 200


# Запись данных с дачтика подключенного к устройству [device] в поле [sensor]
@app.post("/{user}/device/{id}/sensor")
async def test(sensor: Sensor):
    return {"status": "ok"}, 200
