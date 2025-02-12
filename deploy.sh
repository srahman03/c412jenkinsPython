#!/bin/bash

# Define variables
APP_DIR="/root/c412Python"
FLASK_APP="app3.py"
LOG_FILE="app.log"

echo "Navigating to app directory..."
cd "$APP_DIR" || exit

echo "Setting execute permissions..."
chmod +x "$FLASK_APP"

echo "Stopping any existing Flask application..."
pkill -f "$FLASK_APP" || echo "No existing process found."

echo "Starting Flask application..."
nohup python "$FLASK_APP" > "$LOG_FILE" 2>&1 &

echo "Deployment completed successfully."