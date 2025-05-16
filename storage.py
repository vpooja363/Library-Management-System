import csv
import os

def read_csv(filename):
    path = os.path.join("data", filename)
    if not os.path.exists(path):
        return []
    with open(path, newline='') as f:
        return list(csv.DictReader(f))

def append_csv(filename, row, fieldnames):
    path = os.path.join("data", filename)
    exists = os.path.exists(path)
    with open(path, "a", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not exists:
            writer.writeheader()
        writer.writerow(row)

def write_csv(filename, rows, fieldnames):
    path = os.path.join("data", filename)
    with open(path, "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)