import requests

try:
    from ..config import TELEGRAM_TOKEN, CHAT_ID
except ImportError:
    from config import TELEGRAM_TOKEN, CHAT_ID


def send(alert):
    if not TELEGRAM_TOKEN:
        return

    message = (
        f"NISR ALERT\n"
        f"Type: {alert['type']}\n"
        f"Severity: {alert['severity']}\n\n"
        f"{alert['raw']}"
    )

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    try:
        requests.post(url, data={
            "chat_id": CHAT_ID,
            "text": message
        })
    except Exception as e:
        print("Alert Error:", e)