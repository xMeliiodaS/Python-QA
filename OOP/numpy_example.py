import numpy


class NumPyExample:

    def __init__(self, numpy_array):
        self.my_num = numpy.array(numpy_array)

    def mul_numpy(self, mul):
        return self.my_num * mul


my_num_obj = NumPyExample([1, 2, 3])
print(my_num_obj.mul_numpy(4))
