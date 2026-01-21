#!/usr/bin/env python3
"""
Test script to verify Ticketly API functionality
"""
import sys
import os

# Add the app directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Set environment variables for testing
os.environ['DATABASE_URL'] = 'sqlite:///./test.db'
os.environ['SECRET_KEY'] = 'test-secret-key-for-development'
os.environ['ALGORITHM'] = 'HS256'
os.environ['ACCESS_TOKEN_EXPIRE_MINUTES'] = '30'

from fastapi.testclient import TestClient
from app.main import app, create_tables

# Create database tables
create_tables()

# Create test client
client = TestClient(app)

def test_health_check():
    """Test health check endpoint"""
    print("🧪 Testing health check endpoint...")
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
    print("✓ Health check passed")

def test_root():
    """Test root endpoint"""
    print("\n🧪 Testing root endpoint...")
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "Welcome to Ticketly API" in data["message"]
    print("✓ Root endpoint passed")

def test_user_registration():
    """Test user registration"""
    print("\n🧪 Testing user registration...")
    response = client.post(
        "/auth/register",
        json={"email": "test@example.com", "password": "testpassword123"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "test@example.com"
    assert "id" in data
    print(f"✓ User registration passed - User ID: {data['id']}")

def test_user_login():
    """Test user login"""
    print("\n🧪 Testing user login...")
    response = client.post(
        "/auth/login",
        json={"email": "test@example.com", "password": "testpassword123"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
    print("✓ User login passed")
    print(f"  Token: {data['access_token'][:20]}...")
    return data["access_token"]

def test_get_current_user(token):
    """Test getting current user info"""
    print("\n🧪 Testing get current user...")
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/auth/me", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"
    print("✓ Get current user passed")

def test_duplicate_registration():
    """Test duplicate registration fails"""
    print("\n🧪 Testing duplicate registration (should fail)...")
    response = client.post(
        "/auth/register",
        json={"email": "test@example.com", "password": "testpassword123"}
    )
    assert response.status_code == 400
    print("✓ Duplicate registration correctly rejected")

def test_invalid_login():
    """Test invalid login fails"""
    print("\n🧪 Testing invalid login (should fail)...")
    response = client.post(
        "/auth/login",
        json={"email": "test@example.com", "password": "wrongpassword"}
    )
    assert response.status_code == 401
    print("✓ Invalid login correctly rejected")

if __name__ == "__main__":
    print("=" * 60)
    print("🎫 Ticketly API Test Suite")
    print("=" * 60)
    
    try:
        test_health_check()
        test_root()
        test_user_registration()
        token = test_user_login()
        test_get_current_user(token)
        test_duplicate_registration()
        test_invalid_login()
        
        print("\n" + "=" * 60)
        print("✅ All tests passed!")
        print("=" * 60)
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
