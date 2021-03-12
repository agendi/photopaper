#!/usr/bin/python3
# -*- coding:utf-8 -*-
# STD LIBS
import json
import logging
import os
from PIL import Image,ImageDraw,ImageFont
from random import randrange
import sys
import time
import traceback

logging.basicConfig(level=logging.DEBUG)

# 3RD PARTY LIBS
libdir = '../e-Paper/RaspberryPi_JetsonNano/python/lib/'
try:
    sys.path.append(libdir)
    from waveshare_epd import epd7in5_HD
except OSError:
    logging.warning("Waveshare epaper not attached! Using virtual diaplay")
except ModuleNotFoundError:
    logging.warning("Waveshare library not installed see README")
finally:
    from VirtualDisplay.virtualdisplay import epd7in5_HD


# CONFIG
MINIMUM_REFRESH = 10
picdir = '/home/george/Pictures/'
reload = 60

def main():

    logging.info("main entered")
    check_config(reload)

    epd = epd7in5_HD.EPD()

    initialise_display(epd, picdir, reload)

def check_config(reload):
    print(reload)
    if reload < MINIMUM_REFRESH:
        logging.warning("Refresh frequency shorter than the screen refresh rate (%s)" % MINIMUM_REFRESH)
        reload = MINIMUM_REFRESH

def initialise_display(epd, picdir, timeout):
    logging.debug("initialising")
    print("Init")
    # force a picture directory listing
    photos = []
    try:
        while True:
            if len(photos) == 0:
                # generate new list of photos from directory
                photos = create_photo_list(picdir)

            epd.init()
            display(epd, photos)
            time.sleep(timeout)

    except IOError as e:
        logging.info(e)
    except KeyboardInterrupt:
        logging.info("ctrl + c:")
        epd7in5_HD.epdconfig.module_exit()
        exit()

def create_photo_list(path):
        logging.info("Creating new list from '%s'" % (path))
        files = os.listdir(path)
        photos = []
        for f in files:
            if f.endswith(".bmp"):
                logging.info("Adding: {0}{1}".format(path,f))
                photos.append(path + f)

        return photos

def get_photo(photos):
        logging.info("selecting bmp file")
        size = len(photos)
        logging.info(size)
        return photos.pop(randrange(size))


def display(epd, photos):
        epd.Clear()

        fname = get_photo(photos)

        logging.info("displaying %s" % (fname))
        #Himage = Image.open(fname)
        with Image.open(fname) as Himage:
            epd.display(epd.getbuffer(Himage))
        time.sleep(2)

        logging.info("Goto Sleep...")
        epd.sleep()

def cleanup():
    logging.info("Beginning clean up")
    exit()

if __name__ == '__main__':
        main()
