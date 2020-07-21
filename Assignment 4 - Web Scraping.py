'''
In this exercise we will handle some file operations, web requests and basic data cleansing.

Your task consists of 4 operations, writing the 3 below functions and implementing a main function.

If you view https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports
you will see that it has a number of csv files. We're interested in the dates between March 1 to March 21st

We want to write a script that:
  1. Loops over the set of dates
  2. Downloads the csv string from a requested date
  3. Cleans the strings so that they all look the same (to be implemented last)
  4. Writes the string to a file in the data directory called YYYY-MM-dd.csv

'''

from datetime import date, timedelta
from pathlib import Path
from csv import DictReader, DictWriter

import requests

baseurl = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/"


def CreateDataDirectory() -> str:
    """
    Ensures that a directory called "data" exists in the same directory that 
    you call the script from.
    Args:   
        None
    Returns:
        Returns the path string.
    Raises:
        None
    """
    baseDirectory = Path(__file__).resolve().parent
    dataPath = baseDirectory / 'data'

    if(not Path.exists(dataPath)):
        Path.mkdir(dataPath)

    return dataPath


def GetWebCSV(thisDate: date) -> str:
    """
    Returns the csv text from the specific web location
    Args:   
        thisDate: the date that you want returned from the baseurl 
    Returns:
        the csv content of that date
    Raises:
        None
    """
    # from csv import

    this_url = baseurl + thisDate.strftime('%m-%d-%Y') + '.csv'
    this_url
    results = requests.get(this_url)
    return results.text


def CleanCSVString(data: str) -> str:
    """
    Cleans the CSV string with any rules required
    Args:   
        data: csv data returned from the web url 
    Returns:
        the cleanedd csv content
    Raises:
        None
    """
    cleanData = data.encode().decode('utf-8-sig')
    cleanData = cleanData.replace('\r\n','\n')
    return cleanData


def WriteCSVtoFolder(dataPath: str, thisDate: date, data: str):
    """
    Writes the csv to the data path with the specified date
    Args:
        dataPath: path that data will be writen to
        thisDate: date of the file
        data: cleaned csv data returned from the web url 
    Returns:
        None
    Raises:
        None
    """
    writefile = str(dataPath) + '\\' + (thisDate.strftime("%m-%d-%Y") + '.csv')

    with open(writefile, 'w') as f:
        f.write(data)

    #mode = 'w'

    # if mode not in 'wa':
    #   raise ValueError("mode should be either 'w' or 'a'")
    # with open(path,mode) as f:
    #   writer = DictWriter(f,fieldnames=data[0].keys())
    #   if mode =='w':
    #     writer.writeheader()

    #   for row in data:
    #     writer.writerow(row)

    #   pass


def daterange(startDate: date, endDate: date) -> date:
    """
    Generator for returning the days bewteen startDate and endDate
    Args:
        startDate: first date returned from the generator
        endDate: last date returned from the generator
    Returns:
        date between the start and end
    Raises:
        None
    """
    for n in range(int((endDate - startDate).days)+1):
        yield startDate + timedelta(n)


def main():
    """
    Main function
    """
    dataPath = CreateDataDirectory()
    # THE REST OF YOUR MAIN FUNCTION GOES HERE
    startDate = date(2020, 3, 1)
    endDate = date(2020, 3, 21)

    for singleday in daterange(startDate, endDate):
        thisCSV = GetWebCSV(singleday)
        CleanCSV = CleanCSVString(thisCSV)
        WriteCSVtoFolder(dataPath, singleday, CleanCSV)


if __name__ == "__main__":
    main()
