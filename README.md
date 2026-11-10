# kimi
Study 

## Telegram bot

A Telegram bot that answers using the Kimi (Moonshot) API.

```
pip install -r requirements.txt
export TELEGRAM_BOT_TOKEN=...   # from @BotFather
export MOONSHOT_API_KEY=...
python bot.py
```

Optional: set `GITHUB_PAT` (a personal access token with Contents read/write on the repo) and `GITHUB_REPO` (default `as1411307-collab/kimi`) to enable `/read <path>` and `/write <path> <content>`. Never commit the token.
