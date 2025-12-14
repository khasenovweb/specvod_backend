#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/../../app"
source "$SCRIPT_DIR/../../.venv/bin/activate"
gunicorn -w 5 app.wsgi -b 127.0.0.1:8001