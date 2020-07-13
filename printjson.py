import json
import pprint

with open('./Category-based scrape/product_detail.txt', "r") as f:
    data = json.load(f)
    pprint.pprint(data['product_detail'])
