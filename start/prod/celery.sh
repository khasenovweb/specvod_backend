#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/../../app"
source "$SCRIPT_DIR/../../.venv/bin/activate"
celery -A app worker -l info