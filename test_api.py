#!/usr/bin/env python3
"""
LunarCrush API Test Script
Test your API key and environment setup
"""

import os
import requests
import json
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def test_api_key(api_key: Optional[str] = None) -> bool:
    """
    Test the LunarCrush API key
    
    Args:
        api_key: Optional API key. If not provided, will try to get from environment
        
    Returns:
        bool: True if API key works, False otherwise
    """
    # Get API key from parameter or environment
    if not api_key:
        api_key = os.getenv('LUNARCRUSH_API_KEY')
    
    if not api_key:
        print("❌ No API key found!")
        print("Please set LUNARCRUSH_API_KEY environment variable or pass api_key parameter")
        return False
    
    # Test API endpoint
    url = "https://lunarcrush.com/api4/public/topics/list/v1"
    headers = {"Authorization": f"Bearer {api_key}"}
    
    try:
        print(f"🔍 Testing API key: {api_key[:8]}...")
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            topics_count = len(data.get('data', []))
            print(f"✅ API key is valid!")
            print(f"📊 Found {topics_count} trending topics")
            
            # Show first topic as example
            if topics_count > 0:
                first_topic = data['data'][0]
                print(f"🔥 Top trending topic: {first_topic.get('title', 'N/A')}")
                print(f"📈 Interactions: {first_topic.get('interactions_24h', 0):,}")
            
            return True
        else:
            print(f"❌ API request failed with status code: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")
        return False
    except json.JSONDecodeError as e:
        print(f"❌ JSON decode error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def main():
    """Main function to test API setup"""
    print("🚀 LunarCrush API Test Script")
    print("=" * 40)
    
    # Check environment variables
    api_key = os.getenv('LUNARCRUSH_API_KEY')
    base_url = os.getenv('LUNARCRUSH_BASE_URL', 'https://lunarcrush.com/api4')
    
    print(f"📍 Base URL: {base_url}")
    
    if api_key:
        print(f"🔑 API Key: {api_key[:8]}...{api_key[-4:]}")
    else:
        print("🔑 API Key: Not set")
    
    print()
    
    # Test the API
    success = test_api_key(api_key)
    
    print()
    if success:
        print("🎉 Setup complete! Your LunarCrush API is ready to use.")
        print("\nNext steps:")
        print("1. Check out the README.md for usage examples")
        print("2. Explore the API endpoints")
        print("3. Build your social analytics application!")
    else:
        print("💡 Troubleshooting tips:")
        print("1. Make sure you have a valid API key from https://lunarcrush.com/developers/api/authentication")
        print("2. Set the LUNARCRUSH_API_KEY environment variable")
        print("3. Check your internet connection")
        print("4. Verify the API key is not expired")

if __name__ == "__main__":
    main()
