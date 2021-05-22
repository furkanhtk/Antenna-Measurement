import Calculations
import Motor_control
import Measurement
import logging
import plot
def main():
    date_strftime_format = "%d-%b-%y %H:%M:%S"
    message_format = "%(asctime)s - %(levelname)s : %(message)s"
    logging.basicConfig(filename='log.log',level=logging.INFO,format=message_format, datefmt=date_strftime_format)
    LOGGER = logging.getLogger("main")
    Motor_control.rotate()
    Measurement.fun3()
    Calculations.fun1()
    plot.fun4()


    LOGGER.info('Master runs')

if __name__ == "__main__":
    main()