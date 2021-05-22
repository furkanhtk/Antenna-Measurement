import logging
import numpy as np
import os
import csv

def recursive_sum(csv):
    """
    Calculates average of measurements in csv file

    :param csv: csv file that contain the measurement result
    :return: mean_list: average of measurement for each frequency counter_list: number of measurement for each frequency
    """
    LOGGER = logging.getLogger(__name__)
    LOGGER.info('Recursive_sum runs')
    raw_data = np.genfromtxt(csv, delimiter=',')
    dbm_data = raw_data.T[0]
    freq_data = raw_data.T[1]
    value_data = raw_data.T[2]
    mean_list = []
    counter_list = []
    try:
        mean = 0
        counter = 0
        for index,value in enumerate(freq_data):
            counter=counter+1
            mean = mean + value_data[index]
            if freq_data[index] != freq_data[index+1]:
                mean = (mean / counter)
                mean_list.append(mean)
                counter_list.append(counter)
                mean = 0
                counter = 0
    except IndexError:
        mean = (mean / counter)
        mean_list.append(mean)
        counter_list.append(counter)
        pass
    return mean_list,counter_list


def fun1():
    LOGGER = logging.getLogger(__name__)
    LOGGER.info('Calculations runs')
    csv_path = r'C:\Users\Furkan\Desktop\ANTENNA MEASUREMENT SYSTEM\csv'
    csvs = os.listdir(csv_path)
    #f_csv = open("datas.csv", 'w')
    with open('datas.csv', 'w') as f:
        # using csv.writer method from CSV package
        write = csv.writer(f)
        for file in csvs:
            dbm_value = file.split("_")
            average_dbms, number_of_dbms = recursive_sum(csv_path + "\\" + file)
            LOGGER.info('Calculating file : {}'.format(csv_path + "\\" + file))
            average_dbms.append(dbm_value[0])
            write.writerow(average_dbms)
    LOGGER.info('Calculated data saved on datas.csv')

