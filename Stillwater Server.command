#!/bin/zsh
# double click to serve Stillwater on this Mac and your phone
cd "$(dirname "$0")"
IP=$(ipconfig getifaddr en0 2>/dev/null || echo "your-mac-ip")
echo ""
echo "  Stillwater is running."
echo "  On this Mac:    http://localhost:8642"
echo "  On your phone:  http://$IP:8642  (same WiFi)"
echo ""
echo "  Press Ctrl+C to stop."
echo ""
open "http://localhost:8642"
python3 -m http.server 8642
