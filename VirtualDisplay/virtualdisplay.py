import logging
from PIL import Image

logging.basicConfig(level=logging.DEBUG)

class VConfig:
    def module_exit(self):
        logging.info("exiting virtual display")

class epd7in5_HD:
    def EPD():
        return VirtDisplay()

    epdconfig = VConfig()


# create a virtual display that uses imagemagick
class VirtDisplay:
    @staticmethod
    def init():
        logging.info("initialising virutal display")

    @staticmethod
    def Clear():
        logging.info("clearing virtual display")

    @staticmethod
    def getbuffer(img):
        return img

    @staticmethod
    def display(img):
            logging.info("displaying virtual image")
            img.show()

    @staticmethod
    def sleep():
        logging.info("virtual display sleeping")
