import sys
import pandas as pd


def main():
    """ 
    A function to load in a CSV passed as parameter into a dataframe. 
    Remove the time from datetime field and drop other unwanted columns.
    Tidy up the 'Status' field to standardise contents.
    Upon completion writes the file back to orgianl location with 'Cleaned' prefix. 
    """
    data = pd.read_csv(sys.argv[1])
    data[["Created", "Time"]] = data["Created"].str.split(' ', expand=True)
    data[["Updated", "Time2"]] = data["Updated"].str.split(' ', expand=True)
    data.loc[data["Status"] == "In progress - 1st / 2nd Line"] = "In Progress"
    data.drop(["Issue Type", "Issue id", "Priority", "Time", "Time2"], inplace=True, axis=1)
    data.to_csv("Cleaned_" + sys.argv[1], index=False)


if __name__ == "__main__":
    main()
