import logging
# import time
# import spidev


def fun3():
    LOGGER = logging.getLogger(__name__)
    LOGGER.info('fun3 runs')
    bus = 0
    device = 0
    # spi = spidev.SpiDev()
    # spi.open(bus, device)
    # spi.max_speed_hz = 500000
    # spi.mode = 0
    # msg = [0x01]
    #
    # dbm = input("dBm:")
    # f_csv = open("{}_dBm.csv".format(dbm), 'w')
    # while True:
    #     try:
    #         freq = input("Frequency:")
    #         for x in range(25):
    #             time.sleep(0.5)
    #             spi.writebytes(msg)
    #             reply = spi.readbytes(2)
    #             result = reply[0] << 8 | reply[1]
    #             f_csv.write("{},{}\n".format(result, angle))
    #     except KeyboardInterrupt:
    #         f.close()
    #         f_csv.close()
    #         break

