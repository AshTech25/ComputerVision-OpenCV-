import cv2
import imutils
import dropbox
import json
import argparse
import warnings

ap=argparse.ArgumentParser()
ap.add_argument("-c","--conf",required=True,help="Describe Path to json")
args=vars(ap.parse_args())
warnings.filterwarnings("ignore")
details=json.load(open(args["conf"]))
client=None