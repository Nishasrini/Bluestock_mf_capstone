import requests
import pandas as pd

hdfc_url = "https://api.mfapi.in/mf/125497"

response = requests.get(hdfc_url)
data = response.json()

df = pd.DataFrame(data["data"])

df.to_csv(
    "data/raw/HDFC_Top100.csv",
    index=False
)

print("HDFC_Top100 downloaded")

schemes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for name, code in schemes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    data = response.json()

    df = pd.DataFrame(data["data"])

    df.to_csv(
        f"data/raw/{name}.csv",
        index=False
    )

    print(f"{name} downloaded")