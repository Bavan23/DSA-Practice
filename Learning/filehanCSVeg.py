import csv

employee = [
    ["Name", "Age", "Job"],
    ["Bavan", 21, "SDE"],
    ["Guru", 21, "SDE"],
    ["Shashank", 21, "AI Engineer"],
]

file_path = "detailsofallemployee.csv"

try:
    with open(file_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(employee)
        print("CSV file was created successfully.")
except Exception as e:
    print(f"Error occurred while writing the file: {e}")

try:
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
except Exception as e:
    print(f"Error occurred while reading the file: {e}")
