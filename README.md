# Web_page_batch_access_tool
Web page batch access tool

**Prerequisites:**

Before you start, make sure you have Python installed on your system. You'll also need to install the `requests` library, which can be done using `pip`.

```bash
pip install requests
```

**Step 1: Create a List of Target URLs**

Open a text editor or an integrated development environment (IDE) and create a Python script. Start by defining a list of the target URLs you want to access. You can add as many URLs as you like.

```python
import requests

# List the target URLs you want to access
target_urls = [
    'http://example.com',
    'http://example.org',
    'http://example.net',
    # Add more URLs here
]
```

**Step 2: Iterate through the URLs and Send Requests**

Next, we'll iterate through the list of URLs and send GET requests to each one. We'll also check the response status code to determine if the access was successful.

```python
for url in target_urls:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Successfully accessed {url}")
        else:
            print(f"Encountered an issue while accessing {url}, status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An exception occurred while accessing {url}: {str(e)}")
```

**Step 3: Run the Script**

Save the script with a `.py` extension, such as `batch_access_urls.py`. Open a terminal or command prompt, navigate to the script's directory, and run it using Python:

```bash
python batch_access_urls.py
```

The script will start accessing the URLs one by one. If it encounters any issues or exceptions, it will display appropriate messages.

**Important Notes:**

- Ensure that you have permission to access the URLs you specify.
- Respect the usage policies and terms of service of the websites you access.
- This script is intended for legal and ethical use cases only.

That's it! You now have a Python script that can batch access multiple different target URLs. This can be useful for tasks like web scraping, monitoring, or any other legitimate use case.
