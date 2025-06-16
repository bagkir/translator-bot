import requests

from app.config import settings
from app.config_logger import setup_logger

logger = setup_logger(__name__)


def check_access_token() -> bool:
    logger.debug("Checking access token...")

    url = "https://gigachat.devices.sberbank.ru/api/v1/models"
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {settings.AUTH_KEY.get_secret_value()}'
    }
    try:
        response = requests.get(url, headers=headers)
        return response.status_code == 200
    except Exception as e:
        logger.error(f"Checking token error: {e}")
