import random
import string

def generate_email():
    return f"Dariya_Takenova_26_{random.randint(100, 999)}@yandex.ru"

def generate_password(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

VALID_NAME = "Клиент"
INVALID_PASSWORD = "123"
