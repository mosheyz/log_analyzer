import csv

def load_csv(path):
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        lines = [line for line in reader]
        return lines
