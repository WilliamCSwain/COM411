import csv

def read(file_path):
    with open(file_path) as file:
        csv_reader = csv.reader(file)

        headings = next(csv_reader)
        print(f"Headings:\n{heaings}")

        print("Values:")
        for values in csv_reader:
            print(valus)

def run()
    read("bots.csv")

if __name__ == "__main__":
    run()