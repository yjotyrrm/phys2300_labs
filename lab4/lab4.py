'''
Assignment to learn how to interpolate data1
'''
import sys
import matplotlib.pyplot as plt
import numpy as np
# import scipy
# import pandas as pd


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
            wx_temp.append(float(info[3]))
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
            gps_alt.append(int(info[6]))
        gps_data.close()

        harbor_data['alt_times'] = int_time(gps_time)
        harbor_data['alts'] = gps_alt


def int_time(times):
    #changes times from 3 string tuple/list to int representing seconds since zero time
    int_times = []
    zero_hours = float(times[0][0])
    zero_minutes = float(times[0][1])
    zero_seconds = float(times[0][2])

    for t in times:
        t_hours = float(t[0]) - zero_hours
        t_minutes = float(t[1]) - zero_minutes
        t_seconds = float(t[2]) - zero_seconds

        int_time = (t_hours*3600) + (t_minutes*60) + (t_seconds)

        int_times.append(t)

    return t

def split_data(harbor_data, ascent_data, descent_data)
    """
    splits the data into ascending and descending
    :param harbor_data: dictionary for collecting data
    :param ascent_data: dictionary for collecting data of ascent
    :param descent_data: dictionary for collecting data of descent
    """

    #find the index at which altitude began dropping
    for i, v in enumerate(harbor_data['alts']):

         if harbor_data['alts'][i+1] < v:
            drop_index = i
            break
    else:
        print('what went up did not come down')

    drop_alt_time = harbor_data['alt_times'][drop_index]

    for i, t in enumerate(harbor_data['temp_times']):
        if(t > drop_alt_time):
            drop_temp_index = (i-1)
        elif(t == drop_alt_time):
            drop_temp_index = i

    else:
        print("something went wrong comparing times")

    ascent_data['alts'] = harbor_data['alts'][:drop_index +1]
    ascent_data['alt_times'] = harbor_data['alt_times'][:drop_index + 1]
    ascent_data['temps'] = harbor_data['temps'][:drop_temp_index +1]
    ascent_data['temp_times'] = harbor_data['temp_times'][:drop_temp_index + 1]

    descent_data['alts'] = harbor_data['alts'][drop_index:]
    descent_data['alt_times'] = harbor_data['alt_times'][drop_index:]
    descent_data['temps'] = harbor_data['temps'][drop_temp_index:]
    descent_data['temp_times'] = harbor_data['temp_times'][drop_temp_index:]



def interpolate_data(data):
    """
    :param data: a dictionary of altitude and temperature data as well as their respective times
    :return: two lists, of the same length, of corresponding temperatures and altitudes
    """
    temps = data['temps']
    alts = []
    for t in data['temp_times']:
        if(t in data['alt_times']):
            alts.append(data['alts'][data['alt_times'].index(t)])
        else:
            ind1, ind2 = get_nearest_times(data['alt_times'], t)
            alts.append(interpolate(data['alts'][ind1], data['alts'][ind2], data['alt_times'][ind1], data['alt_times'][ind2], t))

    return temps, alts




def get_nearest_times(times, t):
    """
    gets the two closest values in times to t, one above and one below, time must be a sorted list
    :param times: the list of time values
    :param t: the specific time you are trying to find
    :return: two list indices, containing the two closest time values to t
    """

    for i in times:
        #as list is sorted, the first value for which t < i is the closest value larger than i
        #in my use case, t cannot equal i, so the last value in a sorted list will be the closest value smaller than i
        if(t < i):
            return i-1 , i
            break
    else:
        #if there is no value greater than t in the list, interpolate using the last two values of the list
        return -1, -2







def interpolate(alt_1, alt_2, time_1, time_2, t):
    """
    interpolates altitude at time t given two other time/altitude pairs to compare to
    all parameters should be floats
    :param alt_1: the first altitude value
    :param alt_2: the second altitude value
    :param time_1: the first time value
    :param time_2: the second time value
    :param t: the time at which you want an altitude value
    :return: the approximate altitude at time t
    """

    #get the slope between the two indexes, altitude vs time
    slope = (alt_1 - alt_2)/(time_1 - time_2)

    dtime = t - time_1

    dalt = dtime * slope

    return alt_1 + dalt








def plot_figs(ascent_data, descent_data, harbor_data):
    """
    Plot 2 figures with 2 subplots each.
    :param harbor_data: A dictionary to collect data.
    :return: nothing
    """
    plt.figure()
    plt.subplot(2, 1, 1)
    plt.title("temperature vs time")
    plt.plot(harbor_data['temp_times'], harbor_data['temps'])
    plt.ylabel("Temperature, F")
    plt.xlabel("mission elapsed time, seconds")

    plt.subplot(2, 1, 2)
    plt.title("altitude vs time")
    plt.plot(harbor_data['alt_times'], harbor_data['alts'])
    plt.ylabel("altitude, ft")
    plt.xlabel("mission elapsed time, seconds")

    plt.show()


    plt.figure()
    plt.subplot(2, 1, 1)
    plt.title("temperature vs altitude on ascent")
    plt.plot(interpolate_data(ascent_data))
    plt.ylabel("Altitude, ft")
    plt.xlabel("Temperature, F")

    plt.subplot(2, 1, 2)
    plt.title("temperature vs altutude on descent")
    plt.plot(interpolate_data(descent_data))
    plt.ylabel("Altitude, ft")
    plt.xlabel("Temperature, F")

    plt.show()






def main():
    """
    Main function
    :return: Nothing
    """
    harbor_data = {}
    ascent_data = {}
    descent_data = {}
    wx_file = sys.argv[1]                   # first program input param
    gps_file = sys.argv[2]                  # second program input param

    read_wx_data(wx_file, harbor_data)      # collect weather data
    read_gps_data(gps_file, harbor_data)    # collect gps data
    plot_figs(harbor_data)                  # display figures


if __name__ == '__main__':
    main()
    exit(0)
