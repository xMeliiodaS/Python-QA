import pandas as pn


class MyPandas:

    def __init__(self):
        self.data = [1, 2, 3, 4, 5]

    def create_series_data(self):
        return pn.Series(self.data)


asd = MyPandas()
print(asd.create_series_data())
