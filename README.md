# ChromeExtension — Link Share

A Chrome extension that sends your current browser tab's URL directly to your phone via SMS. Useful for quickly moving links from desktop to mobile without copy-pasting.

## How It Works

1. Click the extension icon while on any page.
2. The extension captures the current tab URL.
3. A Node.js connector calls a Python SMS backend (`SMS.py`) using `python-shell`.
4. `SMS.py` routes the message through your carrier's SMS-to-email gateway via SMTP.

Supported carriers include AT&T, T-Mobile, Verizon, Sprint, Boost Mobile, Cricket Wireless, and more.

## Tech Stack

- **Extension** — JavaScript, Chrome Extension Manifest V3
- **SMS backend** — Python (`smtplib`, email-to-SMS gateway)
- **Bridge** — Node.js (`python-shell`)

## Files

| File | Purpose |
|---|---|
| `connector.js` | Node.js bridge that invokes the Python SMS script |
| `SMS.py` | Sends the URL via SMTP to the carrier's SMS gateway |
| `bundle.js` | Bundled extension script |

## Setup

1. Configure `SMS.py` with your SMTP credentials and target phone number.
2. Load the extension folder in Chrome via **chrome://extensions → Load unpacked**.
3. Click the extension icon on any page to send the URL to your phone.

> **Note:** Requires a Gmail account with an app password configured in `SMS.py`.
