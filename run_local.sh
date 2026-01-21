#!/bin/bash
# Simple test script to verify the application works without Docker

echo "🧪 Testing Ticketly Application"
echo "================================"
echo ""

# Use SQLite for local testing
export DATABASE_URL="sqlite:///./test.db"
export SECRET_KEY="test-secret-key-for-development-only"
export ALGORITHM="HS256"
export ACCESS_TOKEN_EXPIRE_MINUTES="30"
export APP_NAME="Ticketly"
export DEBUG="True"

# Activate virtual environment
source venv/bin/activate

echo "✓ Environment configured"
echo "✓ Starting FastAPI server..."
echo ""
echo "📍 API will be available at: http://localhost:8000"
echo "📖 API docs at: http://localhost:8000/docs"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Run the application
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
