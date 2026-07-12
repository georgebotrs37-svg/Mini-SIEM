# Mini SIEM

Mini SIEM is a lightweight security monitoring prototype that watches a log file, detects suspicious events, and prints alerts to the console. It also tries to display simple images when alerts are triggered.

## What it does

- Watches a log file for new entries
- Detects common events such as:
  - Failed password attempts (Brute Force)
  - Accepted password logins (Login Success)
- Prints alert details to the console
- Can optionally send Telegram alerts when a token and chat ID are configured

## Project structure

- main.py: entry point for running the app from the project root
- nisr/main.py: main monitoring loop
- nisr/core/: detection, alerting, and log watching logic
- nisr/state/: state tracking for duplicate alerts
- test.log: example log file used by the app

## Requirements

Install the Python dependencies:

```bash
pip install -r nisr/requirements.txt
```

## Run the app

From the project root:

```bash
python main.py
```

If you are using the virtual environment inside the project:

```bash
.\.venv\Scripts\python.exe main.py
```

## Configuration

Edit [nisr/config.py](nisr/config.py) to set:

- LOG_FILE: the log file path to monitor
- TELEGRAM_TOKEN: optional Telegram bot token
- CHAT_ID: optional Telegram chat ID

## Notes

- The app currently uses [test.log](test.log) as the default log source.
- If no Telegram credentials are provided, alerts remain console-only.
- The image display is best-effort and will not stop the app if an image file is missing.
