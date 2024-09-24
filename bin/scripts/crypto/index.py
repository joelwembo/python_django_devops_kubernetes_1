import requests
url = "https://api.coingecko.com/api/v3/simple/price"
params = {  
         "ids": "ethereum",
         "vs_currencies": "USD"
}

# Replace 'YOUR_API_KEY' with your actual API key
headers = { 'x-cg-demo-api-key': 'YOUR_API_KEY' }

response = requests.get(url, params = params)

