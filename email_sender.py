import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path
import ssl 
from dotenv import load_dotenv


PORT = 465
EMAIL_SERVER = "smtp.gmail.com"

current_dir = Path(__file__).resolve().parent if __file__ in locals() else Path.cwd()

vars = current_dir / ".env"
load_dotenv(vars)


sender_email = os.getenv("EMAIL")
password_email = os.getenv("PASSWORD")


print("Email loaded:", bool(sender_email))
print("Password loaded:", bool(password_email))
print("Email address:", sender_email)



def send_email(subject, receiver_email, name, due_date, invoice_no, amount):
    msg= EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("Patricia", f"{sender_email}"))
    msg["To"] = receiver_email
    msg["BCC"] = sender_email

    msg.set_content(
    f"""\
    Dear {name},

    This is a friendly reminder that payment for invoice
    {invoice_no}, amounting to KES {amount},
    is due on {due_date}.

    Kindly ensure that the payment is made by the due date.

    If you have already made the payment, please disregard
    this reminder.

    Should you have any questions or require assistance,
    please feel free to contact us.

    Thank you for your continued business.

    Kind regards,
    Accounts Department
    """
    )

    msg.add_alternative(
    f"""
    <html>
        <body>
            <h1>Payment Reminder</h1>

            <p>Dear {name},</p>

            <p>
                This is a friendly reminder that payment for invoice
                <strong>{invoice_no}</strong>, amounting to KES {amount},
                is due on <strong>{due_date}</strong>.
            </p>

            <p>
                Kindly ensure that the payment is made by the due date.
            </p>

            <p>
                If you have already made the payment, please disregard
                this reminder.
            </p>

            <p>
                Should you have any questions or require assistance,
                please feel free to contact us.
            </p>

            <p>Thank you for your continued business.</p>

            <p>
                Kind regards,<br>
                Accounts Department
            </p>
        </body>
    </html>
    """, 
    subtype="html",
   )

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(
    EMAIL_SERVER,
    PORT,
    context=context,
    timeout=30
) as server:

     server.login(sender_email, password_email)
     server.send_message(msg)

if __name__== "__main__":
    send_email(
            subject= "Payment Reminder", 
            name= "Patricia", 
            receiver_email= "chelangat.patriciasigei@gmail.com", 
            due_date= "24/11/2026",
            invoice_no= "INV-11-2026", 
            amount= "200", 
        )
