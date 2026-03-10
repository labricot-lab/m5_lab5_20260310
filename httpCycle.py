import requests

def observe_https_cycle(url):
    """
    Sends a GET request to the specified URL and prints the response details.

    Args:
    url (str): The URL of the web server.
    """

    # Send a GET request to the specified URL
    response = requests.get(url)

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        # If successful, print the HTTP status code
        print(f"HTTP Status Code: {response.status_code} (Success)")

        # Print response headers
        print(f"Headers:\n {response.headers}")

        # Access response content (preview)
        content = response.text
        print(f"\nContent Preview:\n {content[:100]}...")  # Print first 100 characters

    else:
        # If response status code is not 200, print the error code
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    # Specify the target URL (replace with your desired URL)
    url = "https://extension.berkeley.edu/"

    # Call the function to observe the HTTPS cycle
    observe_https_cycle(url)