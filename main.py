from loader import Fileloader 

if __name__ == "__main__":
    Loader = Fileloader("/Users/vakimov/Desktop/currentTransaction_5953.csv", {"Date": 1, "Payee": 3, "Amount": 5})
    Loader.load()
    for item in Loader.transactions:
        print(item)