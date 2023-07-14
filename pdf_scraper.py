# 2) For the pdf bill, please write a python script to read from the pdf the Electric meter number (06067013) and the Electric Tax total amount (-1.41).
import pdfplumber
import re
def get_meter_number(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        first_page = pdf.pages[2]
        text = first_page.extract_text()
        meter_number = None
        pattern = r'Meter Number:\s+(\d+)'
        match = re.search(pattern, text)
        if match:
            meter_number = match.group(1)
    return meter_number

def get_total_taxes_fees(pdf_path):
    with pdfplumber.open(pdf_path) as f:
        page = f.pages[2]
        text = page.extract_text()
        total_taxes_fees = None
        for line in text.split('\n'):
            if 'Total Taxes & Fees on Electric Charges' in line:
                total_taxes_fees = line.split('-')[1].strip()
                break
    return total_taxes_fees

pdf_file = 'sdge_bill.pdf'
meter_number = get_meter_number(pdf_file)
total_taxes_fees = get_total_taxes_fees(pdf_file)

print("Meter Number:", meter_number)
print("Total Taxes & Fees on Electric Charges:", total_taxes_fees)
