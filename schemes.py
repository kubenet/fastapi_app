from pydantic import BaseModel, ValidationError
import types


# класс  модели данных Pydantic
class User(BaseModel):
    name: str   # имя пользователь (например ФИО)
    nickname: str   # псевдоним - виден другим пользоавателям
    language: str   # язык
    email: str  # адрес электронной почты
    password: str   # пароль от сервиса
    device: list    # устройства
    status: True    # статус юзера [True - активный, False - заблокированный]
    createdAt: str  # дата регистрации юзера


class Device(BaseModel):
    id: str  # уникальный дентификатор устройства
    name: str  # название устройтсва
    location: str  # расположение устройства (страна: город)
    manufacturer: str  # производитель устройства или бренд (например: Raspberry Pi, Arduino, Amperka)
    mcu: str  # название процессора/микроконтроллера
    mcuArchitecture: []  # архитектура процессора
    createdAt: str  # дата создания устройства
    status: True  # статус устройства (если False, то усройтсво считается неактивным и
    # сервис не обрабатывает запросы от данного устройства, если статус True - запросы устройства обрабатываются)
    description: str    # описание устройства
    groupDevices: str   # устройство может состоять в группе в другими устройствами по общему признаку
    # логическому либо физическому [комната, офисное помещение, сеть устройств, мониторинг)

class Sensor(BaseModel):
    sensors_list: list  #
    sensor_data: list   #
    status: True    #
    last_update: str    #


class Config(BaseModel):
    devices_list: list  #
    service_plan: str   #
    time_limit: bool    #
    device_limit: bool  #
    sensor_limit: bool  #
    date_registration: str  #
    last_update: str    #
