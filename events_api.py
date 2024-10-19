import pandas as pd
import requests

UK_COUNTRY_CODE = 97

base_url = "https://images.parkrun.com/events.json"
response = requests.get(base_url)
result_json = response.json()

events = []

for feature in result_json["events"]["features"]:
    id = feature["id"]
    event_name = feature["properties"]["EventLongName"]
    country_code = feature["properties"]["countrycode"]
    long = feature["geometry"]["coordinates"][0]
    lat = feature["geometry"]["coordinates"][1]
    event_location = feature["properties"]["EventLocation"]

    output_dict = {
        "id": id,
        "name": event_name,
        "country_code": country_code,
        "latitude": lat,
        "longitude": long,
        "location": event_location,
    }

    events.append(output_dict)

df = pd.DataFrame(events)

df["is_junior_event"] = df["name"].str.contains("junior")  # Identifies junior events

df.to_csv("output/Global events.csv", index=False, header=True)

# UK has a country code of 97
uk_events = df[df.country_code == UK_COUNTRY_CODE].drop(["country_code"], axis=1)
uk_events.to_csv("output/UK Events.csv", index=False, header=True)
