
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


