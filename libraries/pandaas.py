import pandas as pd


class MyPandas:

    def __init__(self):
        self._data = [1, 2, 3, 4, 5]

    def create_series_data(self) -> pd.Series:
        """
        Creates a Pandas Series from the internal data list

        :return: A Pandas Series object containing the data.
        """
        return pd.Series(self._data)


panda_series = MyPandas()
print(panda_series.create_series_data())
