from typing import Union
import requests
from fastapi import FastAPI
import pandas as pd
import matplotlib.pyplot as plt

app = FastAPI()

base_url="https://rickandmortyapi.com/api/character"

@app.get("/")
def read_characters():
    response= requests.get(base_url)
    data=response.json()
    df = pd.DataFrame(data['results'])
    df["status"].value_counts().plot.bar()

    print(df.head())
    return plt.show()
