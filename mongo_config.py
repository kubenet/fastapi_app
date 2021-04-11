from pymongo import MongoClient
import datetime
import requests

client = MongoClient('mongodb://localhost:27017/')

template_base = {"name": "",
                 "nickname": "",
                 "email": "email",
                 "password": "",
                 "devices_list": [],
                 "sensors_list": [],
                 "sensor_data": "",
                 "company": "",
                 "status": True,
                 "service_plan": "base",
                 "time_limit": True,
                 "device_limit": True,
                 "sensor_limit": True,
                 "date_registration": datetime.datetime.utcnow(),
                 "last_update": datetime.datetime.utcnow()
                 }


def init_client(email):
    try:
        r = requests.get("https://www.passwordrandom.com/query?command=password")
    except requests.exceptions.Timeout:
        # Maybe set up for a retry, or continue in a retry loop
        return {"status": False, "message": "requests.exceptions.[Timeout generation password service]"}
    except requests.exceptions.TooManyRedirects:
        # Tell the user their URL was bad and try a different one
        return {"status": False,
                "message": "requests.exceptions.TooManyRedirects. [Timeout generation password service]"}
    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        raise SystemExit(e)
        print(e)
        return {"status": False,
                "message": "requests.exceptions.RequestException. [Timeout generation password service]"}

    db = client['clients']
    if email in db.list_collection_names():  # logging
        return {"status": False, "message": "Email incorrect!"}
    else:
        posts = db[email]
        template = template_base
        template["email"] = email
        template["password"] = r.text
        post_id = posts.insert_one(template).inserted_id  # logging
        print(post_id)  # logging
        return {"status": True, "password": r.text}
