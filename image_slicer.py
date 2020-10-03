import numpy as np

class tile:

    def __init__(self, img,  x_pos, y_pos, img_name = "None", label = 0):

        self.img_ = img
        self.x_ = x_pos
        self.y_ = y_pos
        self.name_ = img_name
        self.label_ = label

    def get_coords(self):

        return self.x,self.y



def slice_image(img, img_name = "None", size = 128, reslice = False):

    '''
    Chops up an image in tiles objects. Tiles are simply images
    that have their original coordinates included. 
    '''

    y_px,x_px = img.shape

    n_x = np.floor(x_px/size)
    n_y = np.floor(y_px/size)

    print(n_x)

    tiles_list  = []

    img_pad = np.zeros([y_px+size, x_px+size])
    img_pad[:y_px,:x_px] = img

    for x_num in range(n_x):
        for y_num in range(n_y):

            x_pos = x_num * size
            y_pos = y_num * size

            # copy size x size square from current location
            sub_img = img_pad[y_pos:y_pos+size,x_pos:X_pos+size]

            new_tile = tile(img = sub_img, x_pos = x_pos, y_pos = y_pos,img_name = img_name)

            tiles_list.append(new_tile)

    return tiles_list