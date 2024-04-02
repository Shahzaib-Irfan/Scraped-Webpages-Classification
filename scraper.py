import requests
from bs4 import BeautifulSoup

# Define the URL
url = "https://www.aliexpress.com/w/wholesale-health-and-fitness-equipment.html?g=y&SearchText=health+and+fitness+equipment"

for i in range(1, 15):
    print(f"Page: {i}")
    # Send a GET request
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all div elements with the specified class
    divs = soup.find_all('div', class_='list--gallery--C2f2tvm search-item-card-wrapper-gallery')

    print(len(divs))

    # Loop through each div and extract information
    for div in divs:
        # Extract the title
        title_div = div.find('div', class_='multi--content--11nFIBL').find('div', class_='multi--title--G7dOCj3').h3
        title = title_div.text.strip() if title_div else "N/A"
        
        # Extract the number of items sold
        items_sold_span = div.find('div', class_='multi--tradeContainer--3TqP9qf')
        items_sold = items_sold_span.span.text.strip() if items_sold_span and items_sold_span.span else "N/A"
        
        # Extract the price
        price_div = div.find('div', class_='multi--price-sale--U-S0jtj')
        price = price_div.text.strip() if price_div else "N/A"
        
        # Extract the original price
        original_price_span = div.find('div', class_='multi--price-original--1zEQqOK')
        original_price = original_price_span.span.text.strip() if original_price_span and original_price_span.span else "N/A"
        
        # Extract the discount
        discount_span = div.find('div', class_='multi--discount--3hksz5G')
        discount = discount_span.text.strip() if discount_span else "N/A"
        
        # Extract the shipping information
        shipping_info_span = div.find('div', class_='multi--serviceContainer--3vRdzWN')
        shipping_info = shipping_info_span.span.text.strip() if shipping_info_span and shipping_info_span.span else "N/A"
        
        # Extract the store information
        store_info_span = div.find('span', class_='cards--store--3GyJcot')
        store_info = store_info_span.text.strip() if store_info_span else "N/A"
        
        # Print the extracted information
        # print("Title:", title)
        # print("Items Sold:", items_sold)
        # print("Price:", price)
        # print("Original Price:", original_price)
        # print("Discount:", discount)
        # print("Shipping Info:", shipping_info)
        # print("Store Info:", store_info)
        # print("----------")


        print(title, items_sold, price, original_price, discount, shipping_info, store_info)
        print("----------")

        url = f"https://www.aliexpress.com/w/wholesale-health-and-fitness-equipment.html?page={i + 1}&g=y&SearchText=health+and+fitness+equipment"