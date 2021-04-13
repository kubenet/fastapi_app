from pydantic import BaseModel, ValidationError
import types


# класс  модели данных Pydantic
class CreateUser(BaseModel):
    # language: str
    # name: str
    # nickname: str
    # email: email
    # password: str
    # devices_list: list
    # sensors_list: list
    # sensor_data: list
    # company: str
    # status: True
    # service_plan: str
    # time_limit: bool
    # device_limit: bool
    # sensor_limit: bool
    # date_registration: datetime
    # last_update: datetime

    email: str
    name: str
    device: list
