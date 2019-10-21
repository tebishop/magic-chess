import board_parser
import matplotlib.pyplot as plt
from time import sleep
from PIL import Image
import numpy as np

#fp's
cpaib_rel_path = 'Chess-Playing-AI-Bot/'
test_data_path = 'test_data/new_'
test_iter = '0'

parser = board_parser.BoardParser()
board = np.zeros((800,800,3))

# Tests the chess board classifier
for test_iter in range(0, 8):
  # test_iter cycles over available test images
  for r in range(1,65):
    img = Image.open(cpaib_rel_path + test_data_path + str(test_iter) + '/opencv_frame1_'+str(r)+'.jpg')
    img = np.array(img)
    img = np.reshape(img,(100,100,3))
    #y = image.img_to_array(img)

    #print(y.shape)
    #print(img.shape)

    # plt.imshow(img)
    # plt.show()
    img = np.reshape(img,(1,100,100,3))
    # print(img.shape)

    
    #pred = parser.parse_single_square(img)
    #print(pred)

    x = ((r-1) // 8 + 1) * 100
    y = ((r-1) % 8 + 1) * 100

    board[x-100:x, y-100:y] = img

  pred = parser.parse_board_image(board)
  print(pred)