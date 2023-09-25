import pprint

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
#pprint.pprint(urls)
count = len(urls)
print(f"URLs to crawl: {count}")
