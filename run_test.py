import requests
import json

def test_tavily():
    api_key = "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"
    url = "https://api.tavily.com/search"
    
    payload = {
        "api_key": api_key,
        "query": "What is the weather in Tehran today?",
        "search_depth": "basic"
    }
    
    print("Connecting to Tavily API...")
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("Successfully connected!")
            print("Response Data:")
            print(json.dumps(response.json(), indent=2))
        else:
            print(f"Failed! Status code: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    test_tavily()
