import pandas as pd
import os

folder = "data/raw"

for file in os.listdir(folder):

    if file.endswith(".csv"):

        path = os.path.join(folder, file)

        df = pd.read_csv(path)

        print("\nFile:", file)
        print("Shape:", df.shape)
        print("\nData Types:",df.dtypes)
        print(df.head())
        print("\nMissing Values:")
        print(df.isnull().sum())
        
