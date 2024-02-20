#!/bin/bash
# Usage: ./gen_cli_icon.sh <CAPTION> [FILENAME]
SCRIPT_DIR=$(cd -P -- "$(dirname -- "$0")" && pwd -P)
CAPTION=$1
FILENAME="${2:-out.png}"

if [ $# -eq 0 ] || [ "$1" = "--help" ] || [ -z "$2" ]; then
  echo "Usage: ./gen_cli_icon.sh <CAPTION> [FILENAME]"
  exit 1
fi

convert "$SCRIPT_DIR/terminal-256.png" \
 -background transparent \
 -gravity center \
 -fill white \
 -size 200x128 \
 caption:"\n$CAPTION" \
 -composite "$FILENAME"
