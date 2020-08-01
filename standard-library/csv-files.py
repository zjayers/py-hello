import csv

#  Write CSV
with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["transaction_id", "product_id", "price"])
    writer.writerow([1000, 1, 5])

# Read CSV
with open("data.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)