import random

import pandas as pd


temps = [random.randint(20, 30) for _ in range(7)]
data = {"Days": ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
        "Temperature": temps}

df = pd.DataFrame(data)

print(df)
