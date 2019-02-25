'''
--------------------------------------------------------------------------------
G e n e r a l I n f o r m a t i o n
--------------------------------------------------------------------------------
Name: weather.py

Usage: python datafile

Description: Code to analyze weather data

Inputs: name of data file containing weather data

Outputs: plots and analysis

Auxiliary Files: None

Special Instructions: None

--------------------------------------------------------------------------------
'''
import sys
import matplotlib.pylab as plt
import numpy as np

# Pseudocode:
# 1) get the name of the data file from the user on the command line
# 2) open the data file
# 3) read the first line of data and throw it away (it is the header info the computer doesn't need)
#       from all the remaining lines:
#       read in the date (index 2) and temperature (index 3)
#       parse the date string into year, month, day
#       convert year, month, day into decimal years for plotting (this would make a great function!)
#       (need to pay attention to leap years here!)
# 4) make two lists for the time series - the decimal year list and the temperature list
# 5) sort the data by month so we can average it and take the standard deviation later
# 6) Plot the results


def parse_data(infile):
    """
    Function to parse weather data
    :param infile: weather data input file
    :return: two lists. One list with the information from the third column (date)
                        One list with the information from the fourth column (temperature)
    """
    wdates = []             # list of dates data
    wtemperatures = []      # list of temperarture data

    file = open(infile, "r")
    next(file)
    for line in file:
        info = file.readline().split()
        wdates.append(info[2])
        wtemperatures.append(float(info[3]))

    file.close()

    #split the date strings
    for i,date in enumerate(wdates):
        year = int(date[:4])
        month = int(date[4:6])
        day = int(date[5:])

        wdates[i] = {"year": year,
                "month": month,
                "day": day}



    return wdates, wtemperatures


def calc_mean_std_dev(wdates, wtemp):
    """
    Calculate the mean temperature per month
    Calculate the standard deviation per month's mean
    :param wdates: dictionary with dates fields
    :param wtemp: temperature per month
    :return: means, std_dev: months_mean and std_dev lists
    """
    means = []
    std_dev = []

    months = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
        10: [],
        11: [],
        12: [],
    }

    for i, date in enumerate(wdates):
        print(date["month"])
        months[date["month"]].append(float(wtemp[i]))

    for month in months:
        means.append(np.mean(np.asarray(months[month])))
        std_dev.append(np.std(np.asarray(months[month])))


    return means, std_dev


def year_truncator(wdates):
    wyear = []
    for date in wdates:
        wyear.append(date["year"])

    return wyear






def plot_data_task1(wyear, wtemp, month_mean, month_std):
    """
    Create plot for Task 1.
    :param: wyear: list with year (in decimal)
    :param: wtemp: temperature per
    :param: month_mean: list with month's mean values
    :param: month_std: list with month's mean standard dev values
    """
    # Create canvas with two subplots
    plt.figure()
    plt.subplot(2, 1, 1)                # select first subplot
    plt.title("Temperatures at Ogden")
    plt.plot(wyear, wtemp, "bo")
    plt.ylabel("Temperature, F")
    plt.xlabel("Decimal Year")

    plt.subplot(2, 1, 2)                # select second subplot
    plt.ylabel("Temperature, F")
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    monthNumber = list(range(1, 13, 1))
    plt.xlim([0.7, 13])
    plt.ylim([0, 90])
    width = 0.8
    plt.bar(monthNumber, month_mean, yerr=month_std, width=width,
            color="lightgreen", ecolor="black", linewidth=1.5)
    plt.xticks(monthNumber, months)
    plt.show()      # display plot


def plot_data_task2(maxtemps, mintemps, years):
    pass


def main(infile):
    weather_data = infile    # take data file as input parameter to file
    wdates, wtemperatures = parse_data(weather_data)
    # Calculate mean and standard dev per month
    month_mean, month_std = calc_mean_std_dev(wdates, wtemperatures)
    wyear = year_truncator(wdates)

    print(len(wyear), wyear)
    print(len(wtemperatures), wtemperatures)
    plot_data_task1(wyear, wtemperatures, month_mean, month_std)





if __name__ == "__main__":
    # infile = 'data/CDO6674605799016.txt'  # for testing
    # Note: the 0th argument is the program itself.
    infile = sys.argv[1]
    main(infile)
    exit(0)
