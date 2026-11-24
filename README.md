# Automated Payment Reminder System

A Python-based payment reminder automation tool that reads customer payment records from a CSV file, identifies unpaid invoices with scheduled reminder dates, and sends personalised email reminders automatically.

## Features

- Reads customer payment records from CSV files using Pandas.
- Parses due dates and reminder dates.
- Identifies customers with outstanding payments whose reminder dates have arrived.
- Sends personalised email reminders using Gmail SMTP.
- Tracks sent reminders to avoid repeatedly emailing the same customer.
- Counts successfully sent emails.
- Stores sensitive email credentials in environment variables.

## Technologies Used

- **Python** – Application logic and automation.
- **Pandas** – Reading, processing and filtering CSV records.
- **SMTP** – Sending email reminders.
- **Python-dotenv** – Managing environment variables.

## Project Structure

```text
scheduling/
├── venv/
├── .env
├── .gitignore
├── main.py
├── email_sender.py
├── payments.csv
├── payments.example.csv
├── requirements.txt
└── README.md
```

## CSV Data Format

The application expects a CSV file named `payments.csv` with the following columns:

| Column | Description |
|---|---|
| name | Customer's name |
| email | Customer's email address |
| amount | Outstanding invoice amount |
| invoice_no | Invoice reference |
| due_date | Payment due date |
| reminder_date | Scheduled reminder date |
| has_paid | Payment status (`yes` or `no`) |
| reminder_sent | Whether a reminder has already been sent (`yes` or `no`) |

Dates should use the `DD/MM/YYYY` format.

A fictional sample dataset is provided in `payments.example.csv`. Copy it to `payments.csv` before running the application.

## Setup and Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd agent-ai
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
EMAIL=your_email@gmail.com
PASSWORD=your_gmail_app_password
```

For Gmail SMTP authentication, use a Google App Password rather than your regular Gmail password.

### 5. Prepare the payment records

Copy the example CSV:

```bash
cp payments.example.csv payments.csv
```

Update the records with your test payment data.

Keep real customer records private and do not commit `payments.csv` to version control.

### 6. Run the application

```bash
python3 main.py
```

## Application Workflow

1. Load customer payment records from the CSV file.
2. Parse due dates and reminder dates.
3. Identify customers who:
   - Have not paid.
   - Have reached their scheduled reminder date.
   - Have not already received a reminder.
4. Generate and send personalised email reminders.
5. Update the `reminder_sent` field after successful email sending.
6. Save the updated payment records back to the CSV file.
7. Display the total number of emails sent.

## Security

- Email credentials are stored in a `.env` file.
- Sensitive configuration files are excluded from version control.
- Real customer payment records are kept private.
- Fictional sample records are used for demonstration and testing.
- Service account credentials, if introduced for a future Google Sheets integration, should never be committed to the repository.


## Author

Patricia Chelang'at
