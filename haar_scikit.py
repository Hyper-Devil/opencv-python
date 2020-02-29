import numpy as np
from skimage.transform import integral_image
from skimage.feature import haar_like_feature
img = np.ones((5, 5), dtype=np.uint8)
img_ii = integral_image(img)
feature = haar_like_feature(img_ii, 0, 0, 5, 5, 'type-3-x')
print(feature)
