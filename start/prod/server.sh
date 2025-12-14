#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/../../app"
/root/.local/bin/uv run gunicorn -w 5 app.wsgi -b 127.0.0.1:8001