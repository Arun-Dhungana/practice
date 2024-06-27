# basic numpy array commands
import numpy
import pandas


# to create array of certain range integer take by default 8 bytes but you can change size using dtype parameter to int32 16 or 8  dtype='int8'
arr = numpy.array([100, 2], dtype=numpy.int8)
print(arr.itemsize)
print(arr)

# "npdim"
arr = numpy.array([[1000, 1], [1, 2]], dtype=complex)
print(arr.ndim)
print(arr)

# 0 initialization
# can create 1 dim or multi dim array
# reshape ravel all array cmd return new array you can capture and use it
arr = numpy.zeros((5, 2))
print(arr)
print(arr.shape)
arre = arr.reshape(2, 5)
print(arre)
print(arre.shape)
print(arre.ravel())
for i in arre.flatten():
    print(i)


arr = numpy.ones((5, 2), dtype=numpy.int16)
print(arr)
print(type(arr[0][0]))
#   to create array with liaer space
arr = numpy.linspace(1, 5, dtype=numpy.int32)
print(arr)
