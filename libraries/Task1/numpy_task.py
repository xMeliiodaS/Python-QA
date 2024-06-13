import numpy


class NumPyTask:

    def __init__(self, days: int):
        self.days = days

    def rand_temp_numpy(self) -> list:
        """
        Generate a NumPy array of random temperatures for the specified number of days

        Returns:
            list: An array of random integers between 20 and 30
        """
        return numpy.random.randint(20, 30, self.days)
