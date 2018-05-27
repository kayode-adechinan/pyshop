"""
Demo project for making http requests from python to Shopify
"""

import requests


# post request: create product
def create_product():

    payload = {
      "product": {
        "title": "product for testing",
        "body_html": "product for testing body",
      }
    }

    headers = {"Accept": "application/json", "Content-Type": "application/json"}

    r = requests.post("https://apikey:password@storeaddress.myshopify.com/admin/products.json", json=payload,  headers=headers)

    print(r.json())


# get request: retrieve all products
def get_all_products():

    r = requests.get("https://apikey:password@storeaddress.myshopify.com/admin/products.json")

    print(r.json()['products'][0]['vendor'])


# get request: retrieve product by id
def get_specific_product():

    r = requests.get("https://apikey:password@storeaddress.myshopify.com/admin/products/934425690169.json")

    print(r.json())


# update request: update product
def update_product():

    payload = {
      "product": {
        "title": "product for testing updated",
        "body_html": "product for testing body updated",
      }
    }

    headers = {"Accept": "application/json", "Content-Type": "application/json"}

    r = requests.put("https://apikey:password@storeaddress.myshopify.com/admin/products/934425690169.json", json=payload,  headers=headers)

    print(r.json())


# delete request: delete product
def delete_product():

    r = requests.delete("https://apikey:password@storeaddress.myshopify.com/admin/products/934425690169.json")

    print(r.status_code)



if __name__ == '__main__':

    delete_product()
