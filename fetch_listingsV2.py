import pprint
import re
import requests
from bs4 import BeautifulSoup

file_path = 'link-builder/all-property-links.txt'

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

    # continue_prompt = input("Continue? (y/n): ")
    # if continue_prompt.lower() != "y":
        # break
        
    # send a GET request to the URL and get the response
    response = requests.get(url)
    
    # parse the HTML content of the page using Beautiful Soup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # remove script tags and their content
    for script in soup.find_all('script'):
        script.extract()
     # remove elements with id="footer-bottom"
    for footer_bottom in soup.find_all(id='footer-bottom'):
        footer_bottom.extract()
    
    for more_options_wrapper in soup.find_all(class_='more-options-wrapper'):
        more_options_wrapper.extract()
    
    for sidebar in soup.find_all(class_='sidebar'):
        sidebar.extract()


    # find the <!-- End Main Content --> tag
    end_main_content_tag = soup.find(text='<!-- End Main Content -->')

    # remove all siblings of the <!-- End Main Content --> tag
    if end_main_content_tag:
        for sibling in end_main_content_tag.find_next_siblings():
            sibling.extract()

    # find the </footer> tag
    footer_tag = soup.find('footer')
    if footer_tag:
        # find all the siblings of the </footer> tag and remove them
        for sibling in footer_tag.find_next_siblings():
            sibling.extract()

    # find the <footer> tag and remove it along with its contents
    footer_tag = soup.find('footer')
    if footer_tag:
        footer_tag.extract()
    
    # find the <header> tag and remove it along with its contents
    header_tag = soup.find('header')
    if header_tag:
        header_tag.extract()
    
    # find the <head> tag and remove it along with its contents
    head_tag = soup.find('head')
    if head_tag:
        head_tag.extract()
    
    # find the section with class "listing-layout property-grid"
    listing_section = soup.find('section', class_='listing-layout property-grid')
    # remove the section if found
    if listing_section:
        listing_section.extract()
    
    # find the section with class "map-wrap"
    map_wrap = soup.find('div', class_='map-wrap')
    # remove the section if found
    if map_wrap:
        map_wrap.extract()
    
    # find the section with class "agent-detail"
    agent_detail = soup.find('div', class_='agent-detail')
    # remove the section if found
    if agent_detail:
        agent_detail.extract()
    
    # find the section with class "header-wrapper"
    header_wrapper = soup.find('div', class_='header-wrapper')
    # remove the section if found
    if header_wrapper:
        header_wrapper.extract()
    
    # find the section with class "property-meta"
    property_meta = soup.find('div', class_='property-meta')
    # remove the section if found
    if property_meta:
        property_meta.extract()
    
    # find the section with class "page-head"
    page_head = soup.find('div', class_='page-head')
    # remove the section if found
    if page_head:
        page_head.extract()
    
    # find the section with class "sidebar-wrap"
    sidebar_wrap = soup.find('div', class_='sidebar-wrap')
    # remove the section if found
    if sidebar_wrap:
        sidebar_wrap.extract()
    
    # find the section with class "child-properties"
    child_properties = soup.find('div', class_='child-properties')
    # remove the section if found
    if child_properties:
        child_properties.extract()
    
    # find the section with class "child-properties"
    catItemIntroText = soup.find('div', class_='catItemIntroText')
    # remove the section if found
    if catItemIntroText:
        catItemIntroText.extract()
    
    # find the section with class "catItemBody"
    catItemBody = soup.find('div', class_='catItemBody')
    # remove the section if found
    if catItemBody:
        catItemBody.extract()
    
    # find the section with class "catItemBody"
    printer_icon = soup.find('span', class_='printer-icon')
    # remove the section if found
    if  printer_icon:
        printer_icon.extract()


    style_tags = soup.find_all('style')
    # remove all content within <style> tags
    for style_tag in style_tags:
        style_tag.decompose()


    # find all <svg> tags
    svg_tags = soup.find_all('svg')
    # remove all <svg> tags
    for svg_tag in svg_tags:
        svg_tag.extract()
    
    # find all <form> tags
    form_tags = soup.find_all('form')
    # remove all <form> tags
    for form_tag in form_tags:
        form_tag.extract()


    # define the url_list variable
    url_list = []
    # find all <a> tags with class "swipebox"
    a_tags = soup.find_all('a', class_='swipebox')
    for a_tag in a_tags:
        url = a_tag.get('href')
        url_list.append(url)


    # find the <img> tag within the <div> element
    div_element = soup.find('div', id='property-featured-image')
    img_tag = div_element.find('img')
    # extract the URL of the 'src' attribute
    if img_tag:
        featured_image_url = img_tag.get('src')
        featured_image = featured_image_url

    # find the section with class "property-detail-flexslidercatItemBody"
    property_detail_flexslider = soup.find('div', id='property-detail-flexslider')
    # remove the section if found
    if property_detail_flexslider:
        property_detail_flexslider.extract()
    
    # find the section with class "property-featured-image"
    property_featured_image = soup.find('div', id='property-featured-image')
    # remove the section if found
    if property_featured_image:
        property_featured_image.extract()

    # Find the element with class 'features'
    features_element = soup.find(class_='features')
    # Find all list items (li) within the features element
    list_elements = features_element.find_all('li')
    # Extract the text value of each list item as a string
    values = [li.text.strip() for li in list_elements]
    # Create a comma-separated list of the values
    comma_separated_list = ', '.join(values)

    # find the section with class "features"
    features = soup.find('div', class_='features')
    if features:
        features.extract()
    
    title = soup.find('h4', class_='title')
    title_text = title.get_text().strip().replace("Property ID :", "")

    price = soup.find('h5', class_='price')
    price_text = price

    #price_text = title.get_text().strip().replace("Property ID :", "")
    status_label = soup.find('span', class_='status-label')
    status = status_label

    status = status.get_text(strip=True)


    # Find the nested span with class "status-label" and extract it
    status_label = price.find('span', class_='status-label')
    if status_label:
        status_label.extract()

    # Get the cleaned price text
    price_text = price.get_text().strip()


    category_tag = price.find('small')
    category = category_tag.get_text().replace('- ', '') if category_tag else ''


    # display the fetched HTML content
    #print("\nFetched HTML Content:")
    #print(soup.prettify())
#   
   # print("Desc:")
   # print(full_text)
    print()
    print("Property ID:", title_text)
    print()
    print("Category:", category)
    print()
    print("Listing Tags:", comma_separated_list)
    print()
    print("Price:", price_text)
    print()
    print("Status:", status)
    print()
    print("Featured Image:")
    print(featured_image)
    print()
    print("Images to import:")
    for url in url_list:
        print(url)
