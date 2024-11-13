import requests, json

headers = {
    'content-type': 'application/json',
    'origin': 'https://m.yelp.ca',
    'priority': 'u=1, i',
    'referer': 'https://m.yelp.ca/search?find_desc=Restaurants&find_loc=Vancouver%2C+British+Columbia%2C+CA',
    # 'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36 Edg/130.0.0.0',
}

json_data = [
    {
        'operationName': 'getBizOpenHours',
        'variables': {
            'BizEncId': 'oPAvVk2g_FUQOioH5RP9fA',
        },
        'extensions': {
            'operationType': 'query',
            'documentId': 'ab2b498c8ca32f9efde89952247fe63c9fb0955e0046e118659d21b166b2a99d',
        },
    },
    {
        'operationName': 'GetAdCampaignId',
        'variables': {},
        'extensions': {
            'operationType': 'query',
            'documentId': 'e790e74f182b25fb3756546250d703e71d53a44c80fd9b38910cf80303721843',
        },
    },
    {
        'operationName': 'getBizOpenHours',
        'variables': {
            'BizEncId': '31ag-M_QiaycGQrvAi169w',
        },
        'extensions': {
            'operationType': 'query',
            'documentId': 'ab2b498c8ca32f9efde89952247fe63c9fb0955e0046e118659d21b166b2a99d',
        },
    },
    {
        'operationName': 'getBizOpenHours',
        'variables': {
            'BizEncId': 'NdEPf2Ls5Ql3_nkwjqKvXA',
        },
        'extensions': {
            'operationType': 'query',
            'documentId': 'ab2b498c8ca32f9efde89952247fe63c9fb0955e0046e118659d21b166b2a99d',
        },
    },
    {
        'operationName': 'getBizOpenHours',
        'variables': {
            'BizEncId': 'crM1idgY_glhtxXT5kERNg',
        },
        'extensions': {
            'operationType': 'query',
            'documentId': 'ab2b498c8ca32f9efde89952247fe63c9fb0955e0046e118659d21b166b2a99d',
        },
    },
    {
        'operationName': 'GetOrganicSearchResults',
        'variables': {
            'contextId': 'b6f9593b3e607b3f',
            'contextWriteTime': 1731457803.02285,
            'distanceUnits': 'KM',
            'offset': 10,
        },
        'extensions': {
            'operationType': 'query',
            'documentId': '69b42a03f7c3efea389b20aae0b9718cc2a3b5ba168ea3cb1139ca4631042853',
        },
    },
    {
        'operationName': 'GetBusinessesData',
        'variables': {
            'FetchAdditionalAnnotations': False,
            'encBizIds': [
                'NdEPf2Ls5Ql3_nkwjqKvXA',
                'crM1idgY_glhtxXT5kERNg',
                '4EV_ZcQmjAmP3pmO-_nb2A',
                'OHMv-_cc0kmRCWV3kM44Bg',
                'V4w2oMsWgZSmGKbbku9lKA',
                'GmEeIcJ9vR04kxzYgPMEgg',
                'Ufhxnrt_OJu4jHfVTP3aRQ',
                'iid0VenH7rIp3AWuyQAAHw',
                'sDmD24fm6R7GVSf4Jn5vdg',
                'JGZbGEKXmZ7OeqjYaGp4bw',
                'WAoOGyNniFmpksKjPysagQ',
                'WZz3gI0V6hN9M_cpeyo9Jg',
                'S-wgeQmV5v4g4wti05zUlQ',
                'XAH2HpuUUtu7CUO26pbs4w',
                'p5thThuUITUjAy8gS3sPMw',
                '9DIct6R794tApbOtdHafXA',
                'jKO4Og6ucdX2-YCTKQVYjg',
                't-soDjOlN6XkySHBdhRkKA',
                'F5wxgIiZE7LYQxgqhI483A',
                'SIdbZcE5gp63UjRN8tLr0g',
                'TQj4HSCmm5GnriKMiSpqpQ',
                'BUFt4lRzuOWUmqHBtv7AmQ',
                '0oGCF9xsvKe1vS6Sm3o3VQ',
                'yeNenSjz_HCqngGFU5d8NQ',
                'LRGDX7adkuh9JMM2vufYvw',
                'DkKH_q0_vdWSWZwFhPFLZw',
                'uAROEz8D29elXoNxjnPrkQ',
                '_4R46MNkwx9MeOyt0YfNxA',
                'gt1BSfVFvzI-qHdJ3LUZug',
                'K1nbiOrySlw_-XG-3NmErQ',
                '1sqnY52m11uWJFLzD-s5BA',
                'uxJqItMyU6pAJxxmveiXBw',
                'WAKwis2gWtNjRqFGkgwORw',
                'vs_sg8N8nCWkZyyk5Xbeow',
                'QzZfjFBnqtBZUUFlWVCd5w',
                'WDTzL8N__Jr2nxH3NijbMw',
                'QstYU_fo1_47oeHb_JBoZA',
                'wVlLeeowJn_VEhMOJVxMBQ',
                'fkyvSfVYXHlG6nHRTBhsdA',
                'YCAjLW8fkGufQizqiu9OBA',
                'X7aMzFlFEt6CdOuZ6BQHDg',
                'VPqWLp9kMiZEbctCebIZUA',
                'V-kQkPZzlOXIqk3rSqkikg',
                'y7vRab3A0WyPKGOZT5fjPQ',
                'rpJpZOvTPbVmBh2goK1iOA',
                'pHLp3uNBUvNbADbh7B3gBw',
                '6iOAgzJ0DRZNSKA3FSrrOg',
                'wHTXCWVsx2PYPT21JV-HeQ',
                'nfdTh56TAqekRLz-TUFOBg',
                '2L1qgW7SlsvmEs5wzAaM0w',
                'bgQRJLO8QFYDpCfkeOhjVA',
                'JgSGpSMHbGecAXs_o1rE_g',
                'YU5Sz2ATtlA1GrIn5YeNeA',
                '9Waotz-_G9woVPWZTmZcwA',
                'LjdbthVdtLYKSi7iVAFl0g',
                'k7-oClu97qColM6BcCaQMw',
                'qR4rQOC8ewW0PD5KK9Blng',
                'jMz_y_-cWMfiZF7Q5snE6Q',
                'QmkGDL-8zexdKV3Xcn8ZYg',
                'hDQmMvYXpLVXwhXSu9HsOQ',
            ],
            'FetchFirstRelevantReview': False,
            'PhotoSize': 'SQUARE_90',
            'FetchAmbience': False,
        },
        'extensions': {
            'operationType': 'query',
            'documentId': '0b8c6baeab1f325d14f643df8c6ab96d3b439bf1d0b306a65b523b9d3170c64f',
        },
    },
]

response = requests.post('https://m.yelp.ca/gql/batch', headers=headers, json=json_data)

data = response.json()

# businesses = []

# for item in data:
#     if item["data"].get("businesses", None):
#         businesses.append(item["data"]["businesses"])

businesses = data[6]["data"]["businesses"]

final_businesses = []

for business in businesses:
    final_businesses.append({
        "name": business["name"],
    })

with open("yepTest2.json", "w", encoding="utf-8") as file:
    file.write(json.dumps(final_businesses, indent=4)) 