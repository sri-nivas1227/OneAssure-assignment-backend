from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
client = MongoClient(os.getenv("MONGO_DB_URI"))
db = client["oneassure"]
premuim_data_collection = db["premium_data"]


def premium_calculator(age_list, sum_insured, city_tier, tenure):
    rates = []
    age_list.sort()
    for age in age_list:
        data = premuim_data_collection.find_one(
            {},
            {
                f"tier_id.{city_tier}.sum_insured.{sum_insured}.tenure.{tenure}.age_rate.{age}": 1
            },
        )

        rate = data["tier_id"][city_tier]["sum_insured"][sum_insured]["tenure"][tenure][
            "age_rate"
        ][age]["rate"]
        rates.append(int(rate))
    premium = 0
    for i in range(len(rates) - 1):
        rates[i] = rates[i] / 2
    for rate in rates:
        premium += rate
    print("premium", premium)
    return premium


# calculate_premium(["46", "35", "10"], "500000", "1", "1")
