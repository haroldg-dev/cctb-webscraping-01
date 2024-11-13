import requests, json

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Origin': 'https://www.psychobunny.com',
    'Referer': 'https://www.psychobunny.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36 Edg/130.0.0.0',
    'content-type': 'application/x-www-form-urlencoded',
    'sec-ch-ua': '"Chromium";v="130", "Microsoft Edge";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}

query = input("Enter a search query: ")
data = '{"requests":[{"indexName":"pbus_products","params":"clickAnalytics=true&distinct=true&facets=%5B%22named_tags.category%22%2C%22named_tags.color%22%2C%22named_tags.department%22%2C%22price%22%5D&highlightPostTag=__%2Fais-highlight__&highlightPreTag=__ais-highlight__&maxValuesPerFacet=200&page=0&query='+query+'&ruleContexts=%5B%22country_US%22%5D&tagFilters="}]}'

response = requests.post(
    'https://9ydqfuzlmp-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(4.20.0)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.60.0)%3B%20Shopify%20Integration%3B%20JS%20Helper%20(3.15.0)&x-algolia-api-key=c0e14a2e1cf1b29a21c468576d2ff669&x-algolia-application-id=9YDQFUZLMP',
    headers=headers,
    data=data,
)

# print(response.json())

data = response.json()

products = data["results"][0]["hits"]

final_products = []

for product in products:
    final_products.append({
        "title": product["title"],
        "price": product["price"],
        "sku": product["sku"],
        "product_image": product["product_image"],
        "grams": product["grams"],
        "weight": product["weight"],
    })

with open("psychoBunny.json", "w", encoding="utf-8") as file:
    file.write(json.dumps(final_products, indent=4)) 