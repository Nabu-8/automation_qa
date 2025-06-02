import csv
from datetime import datetime

def normalize_text(text):
    return ' '.join(word.capitalize() for word in text.strip().split())

def normalize_date(date_str):
    for fmt in ("%d/%m/%Y", "%d.%m.%Y", "%Y-%m-%d"):  # поддержка всех возможных форматов
        try:
            return datetime.strptime(date_str.strip(), fmt).strftime("%m/%d/%Y")
        except ValueError:
            continue
    return date_str.strip()

with open("random.csv", newline='') as file1:
    reader1 = list(csv.reader(file1))
    headers = reader1[0]
    data1 = reader1[3:]

with open("random-michaels.csv", newline='') as file2:
    reader2 = list(csv.reader(file2))
    data2 = reader2[1:]
    data2 = [row[:len(headers)] for row in data2]

combined = data1 + data2
clean_combined = []

for row in combined:
    row = [cell.strip() for cell in row]
    if any('skip' in cell.lower() and 'parse' in cell.lower() for cell in row):
        continue
    if len(row) > 3:
        row[1] = normalize_text(row[1])
        row[2] = normalize_text(row[2])
        row[3] = normalize_text(row[3])
    if len(row) > 13:
        row[4] = normalize_date(row[13])
        row[13] = normalize_date(row[13])
    clean_combined.append(row)

unique_rows = list({tuple(row) for row in clean_combined})
unique_rows.sort()

with open("result_Bubynina.csv", 'w', newline='', encoding='utf-8') as file3:
    writer = csv.writer(file3)
    writer.writerow(headers)
    writer.writerows(unique_rows)