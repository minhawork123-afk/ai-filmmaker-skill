#!/usr/bin/env bash
# Package the skill for upload to Claude.ai, ChatGPT Skills and the Gemini app.
# Produces:
#   dist/ai-filmmaker.zip           ai-filmmaker/ as the top-level folder (required by Claude.ai)
#   dist/ai-filmmaker-portable.zip  SYSTEM_PROMPT.md + knowledge/ + full file + setup guide
set -euo pipefail
cd "$(dirname "$0")/.."

rm -rf dist
mkdir -p dist
python3 build/build_portable.py --check

(cd skills && zip -qr -X ../dist/ai-filmmaker.zip ai-filmmaker -x '*/__pycache__/*' '*.pyc' '*/.DS_Store')
(cd portable && zip -qr -X ../dist/ai-filmmaker-portable.zip . -x '.DS_Store')

# The skill folder must be the zip's top level, or Claude.ai rejects the upload.
if unzip -Z1 dist/ai-filmmaker.zip | grep -qv '^ai-filmmaker/'; then
  echo "ERROR: ai-filmmaker.zip has files outside ai-filmmaker/" >&2
  exit 1
fi
unzip -Z1 dist/ai-filmmaker.zip | grep -qx 'ai-filmmaker/SKILL.md' || { echo "ERROR: SKILL.md missing from zip" >&2; exit 1; }

ls -la dist
