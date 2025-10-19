#!/usr/bin/env python3
"""
LunarCrush API Test Script
Tests if the API key is working by making a simple request to the topics list endpoint.
"""

import os
import requests
import json
from typing import Optional

def load_api_key() -> Optional[str]:
    """Load API key from environment variable or .env file."""
    # First try environment variable
    api_key = os.getenv('LUNARCRUSH_API_KEY')
    if api_key:
        return api_key
    
    # Try loading from .env file
    try:
        with open('.env', 'r') as f:
            for line in f:
                if line.startswith('LUNARCRUSH_API_KEY='):
                    return line.split('=', 1)[1].strip().strip('"\'')
    except FileNotFoundError:
        pass
    
    return None

def test_api_connection(api_key: str) -> bool:
    """Test API connection with a simple topics list request."""
    base_url = "https://lunarcrush.com/api4"
    endpoint = "/public/topics/list/v1"
    url = f"{base_url}{endpoint}"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    try:
        print(f"Testing API connection to: {url}")
        response = requests.get(url, headers=headers, timeout=10)
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print("✅ API Key is working!")
            print(f"Response contains {len(data.get('data', []))} topics")
            
            # Show first few topics as example
            topics = data.get('data', [])[:3]
            if topics:
                print("\nFirst few topics:")
                for topic in topics:
                    print(f"  - {topic.get('topic', 'Unknown')}")
            
            return True
        elif response.status_code == 401:
            print("❌ Authentication failed - API key is invalid")
            return False
        elif response.status_code == 429:
            print("⚠️  Rate limit exceeded - API key works but you're hitting limits")
            return True
        else:
            print(f"❌ Unexpected response: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")
        return False

def main():
    """Main function to test the LunarCrush API."""
    print("LunarCrush API Key Test")
    print("=" * 30)
    
    # Load API key
    api_key = load_api_key()
    
    if not api_key:
        print("❌ No API key found!")
        print("\nPlease set your API key in one of these ways:")
        print("1. Environment variable: export LUNARCRUSH_API_KEY='your_key_here'")
        print("2. Create a .env file with: LUNARCRUSH_API_KEY=your_key_here")
        return
    
    print(f"API Key found: {api_key[:8]}...")
    
    # Test the API
    if test_api_connection(api_key):
        print("\n🎉 API key verification successful!")
    else:
        print("\n💥 API key verification failed!")

if __name__ == "__main__":
    main()