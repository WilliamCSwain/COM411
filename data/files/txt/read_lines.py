def search(file_path):
    print("Searching..")
    with open(file_path) as file:
        for location in file:
            print(f"Looked in {location.strip()}")
    print("Done!")

def run():
    search("library.txt")

if __name__ == "__main__":
    run()