#!/bin/bash

# Define variables
APP_DIR="/root/c412Python"
FLASK_APP="app3.py"
LOG_FILE="app.log"

echo "Navigating to app directory..."
cd "$APP_DIR" || exit # exit if directory doesnt exist 

echo "Setting execute permissions..."
chmod +x "$FLASK_APP"

echo "Stopping any existing Flask application..."
pkill -f "$FLASK_APP" || echo "No existing process found."
#-f = kills process name

echo "Starting Flask application..."
nohup python "$FLASK_APP" > "$LOG_FILE" 2>&1 &
#nohup - runs command without hanging up - even when terminal closes
#python FLASKAPP - runs app 
#redirects to app.log file 
#error logs also to the same file 
#& runs in background

echo "Deployment completed successfully."