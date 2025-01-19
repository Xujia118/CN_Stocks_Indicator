from module_decide_holding_stocks import decide_holding_stocks
from module_decide_candidates import scan_candidates
import smtplib
from datetime import date
import pandas as pd
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()

frame = pd.read_csv('Candidates_CSI300.csv')

def scan_decide():

    # Get results from functions
    holding_stocks_result = decide_holding_stocks()
    candidates_result = scan_candidates(frame)
    current_date = date.today()

    # Email configuration
    sender_email = os.getenv("SENDER_EMAIL")
    password = os.getenv("PASSWORD")
    receiver_email = '773977192@qq.com'
    subject = 'Daily report'

    # Email content
    email_text = f"Decision Holding Stocks: {holding_stocks_result}\n" \
                 f"Decision Candidates: {candidates_result}\n" \
                 f"Date: {current_date}"

    em = EmailMessage()
    em['From'] = sender_email
    em['to'] = receiver_email
    em['Subject'] = subject
    em.set_content(email_text)
    
    with smtplib.SMTP_SSL('smtp.163.com', 465) as server:
        server.login(sender_email, password)
        server.send_message(em)

if __name__ == '__main__':
    scan_decide()