import os

# Токен Telegram-бота загружается из переменных окружения
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
siteDomain = os.getenv("SITE_DOMAIN", "http://127.0.0.1:8000")
OurSite = os.getenv("OUR_SITE", "http://127.0.0.1:8000")
REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "10"))
