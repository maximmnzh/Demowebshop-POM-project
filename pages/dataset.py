import time


def register_dataset():
    first_name = str(time.time())
    last_name = str(time.time())
    email = str(time.time()) + "@mail.com"
    password = "testtest"
    return first_name, last_name, email, password


class TestDatasets:
    email = "test111222@test111222.com"
    password = "test123"
    new_password = "test1234"
