import base64
import os
import requests

TELEGRAM_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
KIMI_API_KEY = os.environ["MOONSHOT_API_KEY"]
KIMI_MODEL = os.environ.get("KIMI_MODEL", "moonshot-v1-8k")
TG = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"
GITHUB_PAT = os.environ.get("GITHUB_PAT")
GITHUB_REPO = os.environ.get("GITHUB_REPO", "as1411307-collab/kimi")
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


def gh_headers():
    return {"Authorization": f"Bearer {GITHUB_PAT}", "Accept": "application/vnd.github+json"}


def gh_read(path):
    r = requests.get(f"https://api.github.com/repos/{GITHUB_REPO}/contents/{path}", headers=gh_headers(), timeout=30)
    r.raise_for_status()
    return base64.b64decode(r.json()["content"]).decode()


def gh_write(path, content):
    url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{path}"
    body = {"message": f"Update {path} via bot", "content": base64.b64encode(content.encode()).decode()}
    existing = requests.get(url, headers=gh_headers(), timeout=30)
    if existing.status_code == 200:
        body["sha"] = existing.json()["sha"]
    r = requests.put(url, headers=gh_headers(), json=body, timeout=30)
    r.raise_for_status()


def handle_github(chat_id, text):
    if not GITHUB_PAT:
        send(chat_id, "GITHUB_PAT is not configured.")
        return
    parts = text.split(maxsplit=2)
    try:
        if parts[0] == "/read" and len(parts) >= 2:
            send(chat_id, gh_read(parts[1]))
        elif parts[0] == "/write" and len(parts) == 3:
            gh_write(parts[1], parts[2])
            send(chat_id, f"Saved {parts[1]}")
        else:
            send(chat_id, "Usage: /read <path> or /write <path> <content>")
    except requests.RequestException as e:
        send(chat_id, f"GitHub error: {e}")


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
    if text.startswith(("/read", "/write")):
        handle_github(chat_id, text)
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
