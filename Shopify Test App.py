import requests, json

 ##### https://shopify.dev/api/admin-rest

########################################
#### CONNECTION AND AUTHORISATION
########################################

admin_access_token = "TOKEN GOES HERE"
session = requests.Session()
session.headers = {
                "X-Shopify-Access-Token": admin_access_token,
                "Content-Type": "application/json" }


########################################
#### ADD PRODUCT
########################################

endpoint = "https://test-storedev246.myshopify.com/admin/api/2022-04/products.json"
response = session.get(endpoint)
payload = {
"product": {
    "handle": "product for testing 27",
    "title": "product for testing 12",
    "body_html": "product for testing body 1241",
}
}

Product_upload = requests.post(endpoint, json=payload,  headers=session.headers)
products = response.json()

print(json.dumps(Product_upload, indent=1))

########################################
#### GET PRODUCT
########################################

endpoint = "https://test-storedev246.myshopify.com/admin/api/2022-04/products/%d.json" % "PRODUCT # ID GOES HERE"
response = session.get(endpoint)

products = response.json()

print(json.dumps(products, indent=1))

########################################
#### UPDATE PRODUCT
########################################

endpoint = "https://test-storedev246.myshopify.com/admin/api/2022-04/products/%d.json" % "PRODUCT # ID GOES HERE"
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

print(json.dumps(Product_Update, indent=1))

