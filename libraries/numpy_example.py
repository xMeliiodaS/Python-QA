import numpy


class NumPyExample:

    def __init__(self, numpy_array: list):
        self.my_num = numpy.array(numpy_array)

    def mul_numpy(self, mul : int) -> list:
        """
        Multiply the internal NumPy array by a scalar value.

        :param mul: The scalar value to multiply the NumPy array by
        :return: A NumPy array resulting from the multiplication
        """
        return self.my_num * mul


my_num_obj = NumPyExample([[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 9]])
print(my_num_obj.mul_numpy(2))
