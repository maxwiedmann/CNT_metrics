

class tile:

    def __init__(self, imput_img,  x_pos, y_pos, img_name = "None"):


    self.img = imput_img
    self.x = x_pos
    self.y = y_pos
    self.name = img_name



def slice_image(img, size = 128, reslice = False)

    y_px,x_px = img.shape

    