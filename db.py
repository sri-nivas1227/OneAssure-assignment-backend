from pymongo import MongoClient
import json
import csv

client = MongoClient("localhost", 27017)
db = client["oneassure"]
collection = db["premium_data"]
# make product code unique
collection.create_index("ProductCode", unique=True)

csv_file = open("assignment_raw_rate.csv", "r")
reader = csv.DictReader(csv_file)
data = {}
i = 0
for row in reader:
    product_code = row["ProductCode"]
    tier_id = row["TierID"]
    sum_insured = row["SumInsured"]
    tenure = row["Tenure"]
    age = row["Age"]
    rate = float(row["Rate"])

    if product_code not in data:
        data[product_code] = {}
    if tier_id not in data[product_code]:
        data[product_code][tier_id] = {}
    if sum_insured not in data[product_code][tier_id]:
        data[product_code][tier_id][sum_insured] = {}
    if tenure not in data[product_code][tier_id][sum_insured]:
        data[product_code][tier_id][sum_insured][tenure] = {}

    data[product_code][tier_id][sum_insured][tenure][age] = rate

# with open("data.json", "w") as json_file:
#     json.dump(data, json_file)

try:
    for key in data:
        collection.insert_one(data[key])
except Exception as e:
    print("Data exists")
