import sys
import pandas as pd

def main():
    
    data = pd.read_csv(sys.argv[1])
    data.drop("Issue Type", inplace=True, axis=1)
    data.drop("Issue id",  inplace=True, axis=1)

    #data["Created"] = pd.to_datetime(data["Created"]).dt.date
    #data["Time"] = pd.to_datetime(df["date"]).dt.time
    data.info()
if __name__ == "__main__":
    main()