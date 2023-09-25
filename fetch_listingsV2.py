import pprint
import requests
from bs4 import BeautifulSoup

file_path = '../link-builder/all-property-links.txt'

urls = []  # empty list to hold the URLs

# open the file for reading
with open(file_path, 'r') as file:
    # read the contents of the file as a list of lines
    lines = file.readlines()

# process each line and add the URL to the list
for line in lines:
    url = line.strip()  # strip any leading/trailing whitespaces or newline characters
    urls.append(url)

# printing the list of URLs
count = len(urls)
print(f"URLs to crawl: {count}")

# iterate over each URL
for url in urls:
    print(f"\nFetching URL: {url}")
    continue_prompt = input("Continue? (y/n): ")

    if continue_prompt.lower() != "y":
        break
        
    # send a GET request to the URL and get the response
    response = requests.get(url)
    
    # parse the HTML content of the page using Beautiful Soup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # display the fetched HTML content
    print("\nFetched HTML Content:")
    print(soup.prettify())
