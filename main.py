
from datetime import date
import pandas as pd
from email_sender import send_email



def load():
    df = pd.read_csv("payments.csv", 
     parse_dates= ["due_date", "reminder_date"], 
     dayfirst=True)
    return df


def query(df):
    today = pd.Timestamp.today().normalize()

    query = df[
        (df["has_paid"].str.strip().str.lower() == "no") &
        (df["reminder_date"] <= today) &
        (df["reminder_sent"].str.strip().str.lower() == "no")
    ]

    return query


def send_reminders(df):
    email_counter = 0

    reminders = query(df)

    for index, row in reminders.iterrows():

        send_email(
            subject="Payment Reminder",
            receiver_email=row["email"],
            name=row["name"],
            due_date=row["due_date"].strftime("%d/%m/%Y"),
            invoice_no=row["invoice_no"],
            amount=row["amount"]
        )

        email_counter += 1

        df.loc[index, "reminder_sent"] = "yes"

    df.to_csv("payments.csv", index=False)

    print(f"Total emails sent: {email_counter}")

df = load()

send_reminders(df)