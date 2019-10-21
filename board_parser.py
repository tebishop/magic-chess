import keras
import os
import numpy as np

root_dir = os.path.dirname(__file__)

cpaib_abs_path = root_dir + '/Chess-Playing-AI-Bot/'
# Takes a 800x800x3 image and spits out FEN codes

class BoardParser:
  def __init__(self):
    self.opt = keras.optimizers.Adadelta(lr=1.0, rho=0.95, epsilon=None, decay=0.0)
    self.piece_detection_model = keras.models.load_model(cpaib_abs_path + 'saved_models/trained_model_final_bs32_225_dg.h5')

    self.piece_detection_model.compile(
      loss='binary_crossentropy',
      optimizer=self.opt,
      metrics=['accuracy'])

    self.piece_detection_model.summary()


  def parse_board_image(self, board_image):
    """
    Pass me a 800x800x3 and I'll give you a FEN
    """
    fen_code = ''


    # assume that image is oriented 8:1 and a:h
    for x in range (1, 9):
      empty_ctr = 0
      for y in range(1, 9):
        square_img = np.reshape(board_image[x*100 - 100:x*100, y*100 -100: y*100], (1,100,100,3))
        occupant = self.parse_single_square(square_img)
        if occupant == 'E':
          empty_ctr += 1
          if y<8:
            continue
        if empty_ctr:
          fen_code += f'{empty_ctr}'
          empty_ctr = 0
        if occupant != 'E':
          fen_code += f'{occupant}'
      if x < 8:
        fen_code += '/'

    # Extra bit of starting code to 
    first_move_trailer = ' w KQkq - 0 1'
    fen_code += first_move_trailer
    
    return fen_code

  def parse_single_square(self, square_image):
    classes = None

    y = self.piece_detection_model.predict_classes(square_image)


    if y==0:
      classes='E' # Empty
    elif y==1:
      classes='B'
    elif y==2:
      classes='K'
    elif y==3:
      classes='N'
    elif y==4:
      classes='P'
    elif y==5:
      classes='Q'
    elif y==6:
      classes='R'
    elif y==7:
      classes='b'
    elif y==8:
      classes='k'
    elif y==9:
      classes='n'
    elif y==10:
      classes='p'
    elif y==11:
      classes='q'
    else:
      classes='r' # rook? 

    return classes
