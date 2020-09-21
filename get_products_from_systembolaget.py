"""
    This script bodgily makes a list, products_of_interest.json, of all of the products available in a given Systembolaget store in a given category.
    You can tweak which store by tweaking the site_id variable, and you can tweak which category by tweaking the categories variable.
"""
import pysystembolaget  # Claes Hallstrom's python wrapper for systembolaget's API https://github.com/claha/pysystembolaget
import json
fetch_new_assortment = False  # Takes around 30 sec to run if true

# From systembolaget's website https://api-portal.systembolaget.se/developer
api_key = '5dc11a79008c4759a8bdc99d569f140a'
site_id = '1412'  # Kapellplatsen 4
categories = ['Röda viner', 'Vita viner']  # Case sensitive

if fetch_new_assortment:
    systembolaget = pysystembolaget.Systembolaget(api_key)

    # Get product list for each store
    response = systembolaget.product_get_products_with_store()

    # Find index of my store in response
    for i in range(len(response)):
        if (response[i]['SiteId'] == site_id):
            site_index = i
            break
    products_in_store = response[site_index]['Products']

    # Save store product list
    with open('products_in_store.json', 'w') as products_in_store_file:
        json.dump(products_in_store, products_in_store_file, indent=4)

    # Get complete product list with descriptions
    response = systembolaget.product_get_all_products()
    product_descriptions = response

    # Save complete product list with descriptions
    with open('products_descriptions.json', 'w') as products_descriptions_file:
        json.dump(product_descriptions, products_descriptions_file, indent=4)

else:
    with open('products_in_store.json', 'r') as products_in_store_file:
        products_in_store = json.load(products_in_store_file)

    with open('products_descriptions.json', 'r') as all_products_file:
        product_descriptions = json.load(all_products_file)

products_of_interest = []  # Initiate

# Find the full product descriptions of each product in store_products in product_descriptions
for product in products_in_store:
    product_id = product['ProductId']

    # Find index of product in product_descriptions
    for i in range(len(product_descriptions)):
        if product_descriptions[i]['ProductId'] == product_id:
            product_index = i
            break

    # If product is in the category of interest, add it to the products_of_interest dict
    if product_descriptions[product_index]['Category'] in categories:
        products_of_interest += [product_descriptions[product_index]]

# Save the descriptions for the products of interest
with open('products_of_interest.json', 'w') as products_of_interest_file:
    json.dump(products_of_interest, products_of_interest_file, indent=4)

print(f'Wrote {len(products_of_interest)} product descriptions to file')
