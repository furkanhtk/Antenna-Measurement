import logging


def rotate(angle=1,direction=0,speed=1):
    """

    The function that rotates the mechanical system up to the desired degree in the desired direction at the desired speed.

    :param angle: the amount of angle to rotate
    :param direction: Clockwise and Counterclockwise
    :param speed: Rotating speed
    :return:
    """
    LOGGER = logging.getLogger(__name__)
    if isinstance(direction, int) and isinstance(angle, int) and isinstance(speed, int):
        if angle <= 0 or angle > 360 or (direction != 1 and direction != 0) or speed <= 0:
            LOGGER.error("Out of range")
        else:
            if direction == 0:
                LOGGER.info('Rotating {} degrees in clockwise direction with speed {}'.format(angle, speed))
            elif direction == 1:
                LOGGER.info('Rotating {} degrees in counter clockwise direction with speed {}'.format(angle, speed))
    else:
        LOGGER.error("Inputs are not integer")