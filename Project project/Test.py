import numpy as np
import nrrd

# Some sample numpy data
data = np.zeros((64, 64, 64, 64))
filename = '/Volumes/WD SSD/Incoming Annotations/9001400 Annotated/9001400.seg.nrrd'

RefDs = nrrd.read_data(filename)
# Write to a NRRD file
nrrd.write(filename, data)

# Load dimensions based on the number of rows, columns, and slices (along the Z axis)
ConstPixelDims = (int(RefDs.Rows), int(RefDs.Columns), len(filename))

# Load spacing values (in mm)
ConstPixelSpacing = (float(RefDs.PixelSpacing[0]), float(RefDs.PixelSpacing[1]), float(RefDs.SliceThickness))

# The array is sized based on 'ConstPixelDims'
ArrayNRRD = np.zeros(ConstPixelDims, dtype=RefDs.pixel_array.dtype)

for filenameDCM in filename:
    # read the file
    ds = nrrd.read_file(filename)
    # store the raw image data
    ArrayNRRD[:, :, filename.index(filenameDCM)] = ds.pixel_array

print(ArrayNRRD)