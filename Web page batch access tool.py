import requests

# List the target URLs you want to access
target_urls = [
    'http://example.com',
    'http://example.org',
    'http://example.net',
    # Add more URLs
]

# Iterate through the list of target URLs and access each one
for url in target_urls:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Successfully accessed {url}")
        else:
            print(f"Encountered an issue while accessing {url}, status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An exception occurred while accessing {url}: {str(e)}")