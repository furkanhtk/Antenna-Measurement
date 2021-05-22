import numpy as np
import matplotlib.pyplot as plt
import logging
import os


def reformat_csv():
    raw_data = np.genfromtxt("datas.csv", delimiter=',')
    temp = raw_data[6]
    raw_data = np.delete(raw_data,6,0)
    raw_data = np.insert(raw_data, 0, temp, axis=0)
    raw_data = np.delete(raw_data,-1,1)
    raw_data = np.transpose(raw_data)
    return raw_data


def plot(datas):
    x_dbm=[0, -10, -20, -30, -40, -50, -60]
    plt.plot(x_dbm, datas[0], 'r', label='0.5Ghz')
    plt.plot(x_dbm, datas[1], 'b', label='1Ghz')
    plt.plot(x_dbm, datas[2], 'g', label='2Ghz')
    plt.plot(x_dbm, datas[3], 'k', label='3Ghz')
    plt.plot(x_dbm, datas[4], 'y', label='4Ghz')
    plt.xlabel('Input Power (dBm)')
    plt.ylabel('ADC Code')
    plt.title('CN0150 Test')
    plt.legend()
    plt.grid(b=True, which='major', color='k', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='--', alpha=0.9)
    #plt.show()
    plt.savefig('CN0150 Test.png')


def fun4():
    LOGGER = logging.getLogger(__name__)
    LOGGER.info('Plotting runs')
    datas=reformat_csv()
    LOGGER.info('Datas reformated runs')
    plot(datas)
    LOGGER.info('Data plotted')



