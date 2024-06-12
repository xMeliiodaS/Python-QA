import random
import pandas as pd


class PandasTask:

    def __init__(self):
        self._temps = [random.randint(20, 30) for _ in range(7)]

        self._data = {"Days": ["Sunday", "Monday", "Tuesday", "Wednesday",
                               "Thursday", "Friday", "Saturday"],
                      "Temperature": self._temps}

        self._df = pd.DataFrame(self._data)

    @property
    def df(self):
        return self._df


data_frame_gen = PandasTask()
print(data_frame_gen.df)
