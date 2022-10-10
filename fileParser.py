import csv
import os
import json

# Statement headers from different banks
# For now, use to recognize bank
bank_of_america_headers = ['\ufeffStatus', 'Date', 'Original Description', 'Split Type', 'Category', 'Currency'
                            , 'Amount', 'User Description', 'Memo', 'Classification', 'Account Name'
                            , 'Simple Description']

city = ['Status', 'Date', 'Description', 'Debit', 'Credit', 'Member Name']

apple = ['Transaction Date', 'Clearing Date', 'Description', 'Merchant', 'Category', 'Type'
        , 'Amount (USD)', 'Purchased By']


outcomeData = {}


def get_file_list():
    # temporary use path to file. Will be getting from user input later
    entries = os.listdir('datafiles/')
    statements = {}
    csv_statements = []
    pdf_statements = []
    txt_statements = []

    for entry in entries:
        if entry.endswith(".csv"):
            csv_statements.append(f"datafiles/{entry}")
        elif entry.endswith(".pdf"):
            csv_statements.append(f"datafiles/{entry}")
        elif entry.endswith(".txt"):
            csv_statements.append(f"datafiles/{entry}")

    statements['csv'] = csv_statements
    statements['pdf'] = pdf_statements
    statements['txt'] = txt_statements

    return statements


def define_bank(file_path):
    with open(file_path, 'r') as data_file:
        reader = csv.DictReader(data_file)
        header = reader.fieldnames

        if header == bank_of_america_headers:
            return "BOFA"
        elif header == city:
            return "CITY"
        elif header == apple:
            return "APPLE"
        else:
            return "Unknown"


# parse BofA statement
def parse_bofa(file_path):
    outcome_data= {}
    with open(file_path, 'r') as data_file:
        reader = csv.DictReader(data_file)

        counter = 0
        for row in reader:
            transaction_id = 'trId_' + str(counter)
            counter += 1

            # remove comma from Amount for huge spending
            row['Amount'] = row['Amount'].replace(',', '')
            if float(row['Amount']) < 0:
                transaction_type = 'spending'
            else:
                transaction_type = 'income'

            outcome_data[transaction_id] = {'Status': row['\ufeffStatus'], 'Date': row['Date']
                                            , 'Transaction Type': transaction_type, 'Bank Category': row['Category']
                                            , 'Description': row['Original Description']
                                            , 'Amount': row['Amount'], 'Payer': row['Account Name']}

    return outcome_data


def parse_city(file):
    outcome_data = {}
    with open(file, 'r') as data_file:
        reader = csv.DictReader(data_file)

        counter = 0
        for row in reader:
            transaction_id = 'trId_' + str(counter)
            counter += 1

            row["Debit"] = row["Debit"].replace(',', '')
            row["Credit"] = row["Credit"].replace(',', '')
            amount = ''
            if row['Debit'] is not None:
                row["Transaction type"] = 'spending'
                amount = row['Debit']
            if row['Credit'] is not None and "payment" in row['Description'].lower():
                row['Transaction type'] = 'payment for credit card'
                amount = row["Credit"]

            outcome_data[transaction_id] = {'Status': row['Status'], 'Date': row['Date']
                                            , 'Transaction Type': row['Transaction type']
                                            , 'Description': row['Description'], 'Amount': amount
                                            , 'Payer': row['Member Name']}

    return outcome_data


def parse_apple(file):
    outcome_data = {}

    with open(file, 'r') as data_file:
        reader = csv.DictReader(data_file)

        counter = 0
        for row in reader:
            transaction_id = 'trId_' + str(counter)
            counter += 1

            row['Amount (USD)'] = row['Amount (USD)'].replace(',', '')

            if row['Type'] == 'Payment' and 'DEPOSIT INTERNET TRANSFER FROM ACCOUNT' in row['Description']:
                row['Type'] = 'payment for credit card'

            outcome_data[transaction_id] = {'Date': row['Transaction Date'], 'Transaction Type': row['Type']
                                            , 'Description': row['Description'], 'Amount': row['Amount (USD)']
                                            , 'Payer': row['Purchased By'], 'Bank Category': row['Category']}
    return outcome_data


def get_final_json():
    files = get_file_list()
    banks_statement = {}
    for file in files['csv']:
        if define_bank(file) == "BOFA":
            banks_statement["BOFA"] = parse_bofa(file)
        if define_bank(file) == "CITY":
            banks_statement["CITY"] = parse_city(file)
        if define_bank(file) == "APPLE":
            banks_statement["APPLE"] = parse_apple(file)

    return json.dumps(banks_statement, indent=4)












