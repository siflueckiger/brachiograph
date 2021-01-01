from linedraw import *

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--imagename", type=str, required=True)
args = parser.parse_args()

IMAGE_NAME      = args.imagename
DRAW_CONTOURS   = int(input("draw contour (2): ") or "2")
DRAW_HATCH      = int(input("draw hatch (16): ") or "16")
REPEAT_CONTOURS = int(input("repeat contour (0): ") or "0")
REPEAT_HATCH 	= int(input("repeat hatch (0): ") or "0")

print("\n")
print("--> imagename:\t\t", IMAGE_NAME)
print("--> draw_contours:\t", DRAW_CONTOURS)
print("--> draw_hatch:\t\t", DRAW_HATCH)
print("--> repeat_contours:\t", REPEAT_CONTOURS)
print("--> repeat_hatch:\t", REPEAT_HATCH)
print("\n")

image_to_json(IMAGE_NAME, draw_contours=DRAW_CONTOURS, draw_hatch=DRAW_HATCH)

print("--> SVG and JSON succesfully generated.")
