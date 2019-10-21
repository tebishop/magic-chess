import requests
import board_parser
from time import sleep
from PIL import Image
import numpy as np

image_source_url = ''

fen_target_url = ''

# This isn't really a server, just a poller and an emitter hooked up to a while loop to process image data and spit out FENs

def rect_img(img):
  fixed_image = img

  return fixed_image

# Pings the raspberry PI for images, parses them, the forwards them to the frontend
def trawl():
  bp = board_parser.BoardParser()

  while True:
    img_req = requests.get(image_source_url)

    if img_req.status != 200:
      print("failed request")
      sleep(1)
      continue

    fen = bp.parse_board_image(rect_img(img))

    requests.get(fen_target_url + fen)

    sleep(1)
  pass


if __name__ == "__main__":
  trawl()
