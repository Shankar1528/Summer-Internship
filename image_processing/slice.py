import numpy as np
from PIL import Image

src = np.array(Image.open('im.jpg').resize((128, 128)))
dst = np.array(Image.open('im.jpg').resize((256, 256))) // 4

dst_copy = dst.copy()
dst_copy[64:128, 128:192] = src[32:96, 32:96]

Image.fromarray(dst_copy).save('im_numpy_paste.jpg')

dst_copy = dst.copy()
dst_copy[64:192, 64:192] = src

Image.fromarray(dst_copy).save('im_numpy_paste_all.jpg')
