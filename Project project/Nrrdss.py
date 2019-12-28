import numpy as np
import nrrd

# Some sample numpy data
data = np.zeros((64, 64, 64, 64))
filename = '/Volumes/WD SSD/Incoming Annotations/9001400 Annotated/9001400.seg.nrrd'

# Write to a NRRD file
nrrd.write(filename, data)

# Read the data back from file
readdata, header = nrrd.read(filename)
print(readdata.shape)
print(header)
