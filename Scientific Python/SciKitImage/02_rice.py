import numpy as np
import matplotlib.pyplot as plt
import PIL.Image as Image
import skimage.measure as measure
import skimage.morphology as morphology
import scipy.ndimage as nd

def load_image( infilename ) :
    img = Image.open( infilename )
    img.load()
    data = np.asarray( img, dtype="int32" )
    return data

def set_title(title):
    figure = plt.gcf()
    figure.canvas.set_window_title(title)

def enhanceImage(image, threshold):
    image[ image[:,:] <= threshold ] = 0
    image[ image[:,:]  > threshold ] = 1
    
rice = load_image("images/rice.jpg")
print "Shape of raw image: {}".format(rice.shape)

# algorithms work with monochrome images
rice = rice[:,:,0]
print "Shape of red image: {}".format(rice.shape)
set_title("monchrome image")
plt.imshow(rice, interpolation="none", cmap="gray")
plt.show()

enhanceImage(rice, 120)
set_title("enhanced image")
plt.imshow(rice, interpolation="none", cmap="gray")
plt.show()

# remove small objects (they must be labelled)
set_title("removed small objects")
labelled = measure.label(rice)
labelled = morphology.remove_small_objects(labelled)
# remove labelling (objects -> 1, non objects -> 0)
rice = np.copy(labelled)
enhanceImage(rice, 1)
plt.imshow(rice, interpolation="none", cmap="gray")
plt.show()

set_title("close objects and fill holes")
rice = nd.binary_fill_holes(rice).astype(int)
# rice = morphology.binary_closing(rice)
plt.imshow(rice, interpolation="none", cmap="gray")
plt.show()

# look at object properties
rice = measure.label(rice)
props = measure.regionprops(rice, ['FilledArea', 'Label'])
for item in props:
    y = item.centroid[0]
    x = item.centroid[1]
    message = str(item.label)
    plt.text(x, y, message, color="white")
set_title("labelling {} objects".format(len(props)))
plt.imshow(rice, interpolation = "none", cmap = "jet")
plt.show()

