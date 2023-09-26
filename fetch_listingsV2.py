import pprint
import re
import time
import requests
from bs4 import BeautifulSoup

def main():
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
        soup2 = BeautifulSoup(response.text, 'html.parser')
       

        #soup2 stuff

        # remove script tags and their content
        for script in soup2.find_all('script'):
            script.extract()
        
        # Remove all <path> tags from the soup object
        for path in soup2.find_all('path'):
            path.decompose()

        # Remove all <svg> tags from the soup object
        for svg in soup2.find_all('svg'):
            svg.decompose()
        
        for form in soup2.find_all('form'):
            form.decompose()
        

        title = soup2.find('h1').text.strip()



        #soup stuff

        # find the section with class "catItemBody"
        printer_icon = soup.find('span', class_='printer-icon')
        # remove the section if found
        if  printer_icon:
            printer_icon.extract()

        
        # Remove all <path> tags from the soup object
        for path in soup.find_all('path'):
            path.decompose()

        # Remove all <svg> tags from the soup object
        for svg in soup.find_all('svg'):
            svg.decompose()
        
        for form in soup.find_all('form'):
            form.decompose()
        

        # Updated soup object without <path> and <svg> tags
        updated_html = str(soup)

        # find the <path> tags and remove them along with their contents
        path_tag = soup.find('path')
        if path_tag:
            path_tag.extract()
        
        # remove script tags and their content
        for script in soup.find_all('script'):
            script.extract()

         # remove elements with id="footer-bottom"
        for footer_bottom in soup.find_all(id='footer-bottom'):
            footer_bottom.extract()
        
        for add_to_favorite in soup.find(id='add-to-favorite'):
            add_to_favorite.extract()
        
        for more_options_wrapper in soup.find_all(class_='more-options-wrapper'):
            more_options_wrapper.extract()
        
        for sidebar in soup.find_all(class_='sidebar'):
            sidebar.extract()


        end_main_content_tag = soup.find(text='<!-- End Main Content -->')
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
        
        # find the section with class "map-wrap"
        add_to_fav = soup.find('span', class_='add-to-fav')
        # remove the section if found
        if add_to_fav:
            add_to_fav.extract()
       

# Find the span tag with class "printer-icon"
        span_tag = soup.find('span', class_='printer-icon')

# Check if the span tag exists and remove it
        if span_tag:
            span_tag.decompose()


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
        short_description = soup.find('div', class_='property-meta')
        short_description = short_description.get_text(strip=True)
        # remove the section if found
        #if short_description:
        #    short_description.extract()

        descriptive_text = soup.find("div", class_="content clearfix").get_text()
        descriptive_text = descriptive_text.replace("Check Our Facebook Page!", "")
        descriptive_text = descriptive_text.replace("Subscribe to our YouTube page for the latest information!", "")
        descriptive_text = descriptive_text.strip()

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
        imgcnt = len(url_list)


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
        
        id_text = soup.find('h4', class_='title')
        id = id_text.get_text().strip().replace("Property ID :", "")

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

        match = re.search(r'\$\d+(?:,\d+)*(?:\.\d+)?', price_text)
        if match:
            currency_number = int(re.sub(r'[^\d]', '', match.group()))



        category_tag = price.find('small')
        category = category_tag.get_text().replace('- ', '') if category_tag else ''



        #description = soup.find('div', class_='catItemHeader').text.strip()
        #print(description)



        lines = descriptive_text.splitlines()

        # Filter out blank lines using a list comprehension
        non_blank_lines = [line for line in lines if line.strip()]

        # Join the non-blank lines back into a string
        filtered_description = '\n'.join(non_blank_lines)

        # Print the filtered description
        #print(filtered_description)
        descriptive_text = filtered_description


# # Using regular expressions to split the data
        # area_matches = re.findall(r'\d+(?:\.\d+)?\s*(?:sq\.?\s*m(?:et(?:er)?s?)?|m²)', short_description)
        # area = area_matches[0].strip() if area_matches else None  # Extracts the area component

        # bedroom_matches = re.findall(r'\d+\s*Bedrooms', short_description)
        # bedrooms = bedroom_matches[0].split()[0] if bedroom_matches else None  # Extracts the bedroom count component

        # bathroom_matches = re.findall(r'\d+(?:\.\d+)?\s*Bathrooms', short_description)
        # bathrooms = bathroom_matches[0].split()[0] if bathroom_matches else None  # Extracts the bathroom count component


# # Using regular expressions to split the data
        # area_matches = re.findall(r'\d+(?:\.\d+)?\s*(?:sq\.?\s*m(?:et(?:er)?s?)?|m²|\bm²\b)', short_description)
        # area = area_matches[0].strip() if area_matches else None  # Extracts the area component

        # bedroom_matches = re.findall(r'\d+\s*Bedrooms', short_description)
        # bedrooms = bedroom_matches[0].split()[0] if bedroom_matches else None  # Extracts the bedroom count component

        # bathroom_matches = re.findall(r'\d+(?:\.\d+)?\s*Bathrooms', short_description)
        # bathrooms = bathroom_matches[0].split()[0] if bathroom_matches else None  # Extracts the bathroom count component

        # print("Area:", area)
        # print("Bedrooms:", bedrooms)
        # print("Bathrooms:", bathrooms)

# Using regular expressions to split the data
        #area_matches = re.findall(r'\d+(?:\.\d+)?\s*(?:sq\.?\s*m(?:et(?:er)?s?)?|m²|\bm²\b)', short_description)
        area_matches = re.findall(r'\d+(?:\.\d+)?\s*(?:sq\.?\s*m(?:et(?:er)?s?)?|m²|\bm²\b)', short_description)
        area = area_matches[0].strip() if area_matches else None  # Extracts the area component

        #bedroom_matches = re.findall(r'\b\d+\s*Bedrooms', short_description)
        bedroom_matches = re.findall(r'\d+\s*Bedrooms', short_description)
        bedrooms = bedroom_matches[0].split()[0] if bedroom_matches else None  # Extracts the bedroom count component

        bathroom_matches = re.findall(r'\d+(?:\.\d+)?\s*Bathrooms', short_description)
        bathrooms = bathroom_matches[0].split()[0] if bathroom_matches else None  # Extracts the bathroom count component

        print("Area:", area)
        print("Bedrooms:", bedrooms)
        print("Bathrooms:", bathrooms)


        elements = comma_separated_list.split(',')
        elements = [element for element in elements if element not in ('Inside')]
        new_comma_separated_list = ','.join(elements)
        
        elements = new_comma_separated_list.split(',')
        elements = [element for element in elements if element not in ('Outside')]
        new_comma_separated_list = ','.join(elements)

        # display the fetched HTML content
        #print("\nFetched HTML Content:")
        #print(soup2.prettify())
#   
       # print("Desc:")
       # print(full_text)
        
        #metastring = "105  sq. mtrs.2 Bedrooms2.5 Bathrooms"
        #split_meta("105  sq. mtrs.2 Bedrooms2.5 Bathrooms")
        #split_meta(metastring)

        print()
        print("ID:", id)
        print("Title:", title)
        print("Category:", category)
        print("Tags:", new_comma_separated_list)
        print("metastring:", split_meta(short_description))
        print("Area:", area)
        print("Bedrooms:", bedrooms)
        print("Bathrooms:", bathrooms)
        print("Short Description:", short_description) 
        print()
        print("Description:")
        print(descriptive_text)
        print()
        print("Status:", status)
        print("Price: $"+  str(currency_number))
        print(" More pricing info: ", price_text)
        print("1 Featured Image + ", imgcnt, " gallery images")
        #print(imgcnt + 1, " Images")
        #print(featured_image)
        #print("Gallery Images:")
        #for url in url_list:
            #print(url)
        time.sleep(4)

def split_meta(metastring):
    #metastring = "TEST"
    allthree = {}
    # Using regular expressions to split the data
    area_matches = re.findall(r'\d+(?:\.\d+)?\s*(?:sq\.?\s*m(?:et(?:er)?s?)?|m²|\bm²\b)', metastring)
    area = area_matches[0].strip() if area_matches else None  # Extracts the area component

    bedroom_matches = re.findall(r'\d+\s*Bedrooms', metastring)
    bedrooms = bedroom_matches[0].split()[0] if bedroom_matches else None  # Extracts the bedroom count component

    bathroom_matches = re.findall(r'\d+(?:\.\d+)?\s*Bathrooms', metastring)
    bathrooms = bathroom_matches[0].split()[0] if bathroom_matches else None  # Extracts the bathroom count component

    allthree = (area, " ", bedrooms, " ",  bathrooms)
    #print(metastring)
    return allthree

main()
