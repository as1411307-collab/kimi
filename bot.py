import os
import requests

TELEGRAM_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
KIMI_API_KEY = os.environ["MOONSHOT_API_KEY"]
KIMI_MODEL = os.environ.get("KIMI_MODEL", "moonshot-v1-8k")
TG = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"
MAX_HISTORY = 20

histories = {}


def ask_kimi(messages):
    r = requests.post(
        "https://api.moonshot.ai/v1/chat/completions",
        headers={"Authorization": f"Bearer {KIMI_API_KEY}"},
        json={"model": KIMI_MODEL, "messages": messages},
        timeout=120,
    )
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]


def send(chat_id, text):
    for i in range(0, len(text), 4000):
        requests.post(f"{TG}/sendMessage", json={"chat_id": chat_id, "text": text[i:i + 4000]}, timeout=30)


def handle(message):
    chat_id = message["chat"]["id"]
    text = message.get("text")
    if not text:
        return
    if text.strip() == "/start":
        histories.pop(chat_id, None)
        send(chat_id, "Hi! Send me a message and Kimi will answer.")
        return
    history = histories.setdefault(chat_id, [])
    history.append({"role": "user", "content": text})
    del history[:-MAX_HISTORY]
    try:
        answer = ask_kimi(history)
    except requests.RequestException as e:
        history.pop()
        send(chat_id, f"Error contacting Kimi: {e}")
        return
    history.append({"role": "assistant", "content": answer})
    send(chat_id, answer)


def main():
    offset = None
    while True:
        try:
            r = requests.get(f"{TG}/getUpdates", params={"timeout": 30, "offset": offset}, timeout=40)
            for u in r.json().get("result", []):
                offset = u["update_id"] + 1
                if "message" in u:
                    handle(u["message"])
        except requests.RequestException:
            continue


if __name__ == "__main__":
    main()
