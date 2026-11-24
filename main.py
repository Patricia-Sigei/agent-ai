
from datetime import date
import pandas as pd
from schedule import send_email



def load():
    df = pd.read_csv("payments.csv", 
     parse_dates= ["due_date", "reminder_date"], 
     dayfirst=True)
    return df

df = load()

print(df)


def query(df):
    today = pd.Timestamp.today().normalize()

    query = df[
        (df["has_paid"].str.strip().str.lower() == "no") &
        (df["reminder_date"] <= today) &
        (df["reminder_sent"].str.strip().str.lower() == "no")
    ]

    return query

