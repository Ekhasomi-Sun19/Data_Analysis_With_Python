import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))
ts = ts.cumsum()

df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list("ABCD"))

df = df.cumsum()
plot = df.plot()

plt.figure()

df.plot()

plot = ts.plot()

plt.show()
