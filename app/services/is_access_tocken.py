import requests
from app.config import settings

from app.config_logger import py_logger


def check_access_token():
    py_logger.debug("Checking access token...")

    url = "https://gigachat.devices.sberbank.ru/api/v1/models"
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {settings.AUTH_KEY.get_secret_value()}'
    }
    try:
        response = requests.get(url, headers=headers)
        return response.status_code == 200
    except Exception as e:
        py_logger.error(f"Checking token error: {e}")
