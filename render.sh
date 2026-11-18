#!/bin/sh
# Re-render entry.png from render.html (build-time only; the grader runs main.py).
# Uses a headless Chromium binary. Adjust CHROME to your local install.
CHROME="${CHROME:-$HOME/.cache/ms-playwright/chromium-1255/chrome-linux64/chrome}"
"$CHROME" --headless --no-sandbox --disable-gpu --hide-scrollbars \
  --window-size=1024,1024 --screenshot="$1" "file://$PWD/render.html"
