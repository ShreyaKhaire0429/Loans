# from celery import shared_task
# import pandas as pd
# from .models import Customer, Loan
# from datetime import timedelta, date

# @shared_task
# def ingest_data():
#     customer_df = pd.read_excel('customer_data.xlsx')
#     loan_df = pd.read_excel('loan_data.xlsx')

#     for _, row in customer_df.iterrows():
#         Customer.objects.create(
#             id=row['customer_id'],
#             first_name=row['first_name'],
#             last_name=row['last_name'],
#             phone_number=row['phone_number'],
#             monthly_income=row['monthly_salary'],
#             approved_limit=row['approved_limit'],
#             current_debt=row['current_debt']
#         )

#     for _, row in loan_df.iterrows():
#         Loan.objects.create(
#             customer_id=row['customer_id'],
#             loan_amount=row['loan_amount'],
#             tenure=row['tenure'],
#             interest_rate=row['interest_rate'],
#             monthly_installment=row['monthly repayment (emi)'],
#             emis_paid_on_time=row['EMIs paid on time'],
#             start_date=row['start date'],
#             end_date=row['end date'],
#         )

# from celery import shared_task

# @shared_task
# def ingest_data():
#     # your Excel processing logic here
#     return "Data Ingested"


from celery import shared_task
import pandas as pd
from .models import Customer, Loan
from django.utils.dateparse import parse_date
from decimal import Decimal
import os

@shared_task
def import_initial_data():
    base = os.path.join(os.getcwd(), 'data')
    cust_path = os.path.join(base, 'customer_data.xlsx')
    loan_path = os.path.join(base, 'loan_data.xlsx')
    if os.path.exists(cust_path):
        df = pd.read_excel(cust_path)
        for _, row in df.iterrows():
            Customer.objects.update_or_create(
                phone_number=str(row['phone_number']),
                defaults={
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'monthly_salary': Decimal(row['monthly_salary']),
                    'approved_limit': int(row.get('approved_limit') or 0),
                    'current_debt': Decimal(row.get('current_debt') or 0)
                }
            )
    if os.path.exists(loan_path):
        df = pd.read_excel(loan_path)
        for _, r in df.iterrows():
            try:
                cust = Customer.objects.get(customer_id=r['customer id'])
            except Customer.DoesNotExist:
                continue
            Loan.objects.update_or_create(
                loan_id=r['loan id'],
                defaults={
                    'customer': cust,
                    'loan_amount': Decimal(r['loan amount']),
                    'tenure': int(r['tenure']),
                    'interest_rate': Decimal(r['interest rate']),
                    'monthly_installment': Decimal(r['monthly repayment (emi)']),
                    'emi_paid_on_time': int(r.get('EMIs paid on time') or 0),
                    'start_date': parse_date(str(r['start date'])) if r.get('start date') else None,
                    'end_date': parse_date(str(r['end date'])) if r.get('end date') else None,
                }
            )
    return "imported"
