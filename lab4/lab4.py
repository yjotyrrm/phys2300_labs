'''
Assignment to learn how to interpolate data1
'''
import sys
import matplotlib.pyplot as plt
import numpy as np
# import scipy
# import pandas as pd

https://youtu.be/-zvHQXnBO6c
def read_wx_data(wx_file, harbor_data):
    """
    Read temperature and time data from file.
    Populates the harbor_data dictionary with two lists: wx_times and wx_temperatures
    :param wx_file: File object with data
    :param harbor_data: A dictionary to collect data.
    :return: Nothing
    """
    wx_time = []
    wx_temp = []
    with open(wx_file, 'r') as wx_data:
        next(wx_data)
        next(wx_data)
        for line in wx_data:
            info = wx_data.readline().split(',')
            wx_time.append(info[1].split(':'))
            wx_temp.append(info[3])
        wx_data.close()

        harbor_data['temp_times'] = int_time(wx_time)
        harbor_data['temps'] = wx_temp




def read_gps_data(gps_file, harbor_data):
    """
    Read gps and altitude data from file.
    Populates the harbor_data dictionary with two lists: gps_times and gps_altitude
    :param gps_file: File object with gps data
    :param harbor_data: A dictionary to collect data.
    :return: Nothing
    """

    gps_time = []
    gps_alt = []
    with open(gps_file, 'r') as gps_data:
        next(gps_data)
        next(gps_data)
        for line in gps_data:
            info = gps_data.readline().split('    ')
            gps_time.append((info[0],info[1],info[2]))
            gps_alt.append(info[6])
        gps_data.close()

        harbor_data['alt_times'] = int_time(gps_time)
        harbor_data['alts'] = gps_alt


def int_time(times):
    #changes times from 3 string tuple/list to int representing seconds since zero time
    int_times = []
    zero_hours = int(times[0][0])
    zero_minutes = int(times[0][1])
    zero_seconds = int(times[0][2])

    for t in times:
        t_hours = int(t[0]) - zero_hours
        t_minutes = int(t[1]) - zero_minutes
        t_seconds = int(t[2]) - zero_seconds

        int_time = (t_hours*3600) + (t_minutes*60) + (t_seconds)

        int_times.append(t)

    return t



def plot_figs(harbor_data):
    """
    Plot 2 figures with 2 subplots each.
    :param harbor_data: A dictionary to collect data.
    :return: nothing
    """
    pass


def main():
    """
    Main function
    :return: Nothing
    """
    harbor_data = {}
    wx_file = sys.argv[1]                   # first program input param
    gps_file = sys.argv[2]                  # second program input param

    read_wx_data(wx_file, harbor_data)      # collect weather data
    read_gps_data(gps_file, harbor_data)    # collect gps data
    plot_figs(harbor_data)                  # display figures


if __name__ == '__main__':
    main()
    exit(0)
