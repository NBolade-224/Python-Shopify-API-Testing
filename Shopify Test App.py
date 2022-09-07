import requests

# Credential and endpoint
admin_access_token = "TOKEN GOES HERE"
endpoint = "https://test-storedev246.myshopify.com/admin/api/2022-04/products/6945359593572.json"
# Set session header
session = requests.Session()
session.headers = {
                "X-Shopify-Access-Token": admin_access_token,
                "Content-Type": "application/json" }
response = session.get(endpoint)

payload = {
"product": {
    "handle": "product for testing 27",
    "title": "product for testing 12",
    "body_html": "product for testing body 1241",
}
}

Product_Update = requests.put(endpoint, json=payload,  headers=session.headers)
products = response.json()

print(Product_Update)
print()
print(products)

