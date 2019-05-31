
from matplotlib.pyplot import specgram
import pandas as pd
from signal import plot

#print(specgram.__doc__)

# NFFT = 128 ( I need 1 minute of data)
# x is 1 d array
# window = func:`window_hanning`, :func:`window_none`,
#     :func:`numpy.blackman`, :func:`numpy.hamming`,
#     :func:`numpy.bartlett`, :func:`scipy.signal`,
#     :func:`scipy.signal.get_window`, etc. The default is
#     :func:`window_hanning`

folder = '/home/abhijeet/Project/Project Sleep Detection/'
file = 'Data/ncce/NP01_001/NP01_001_EEG.csv'
dataframe = pd.read_csv(folder + file, skiprows = 4)
dataset = dataframe.values
channel_1 = dataset[:,0]
channel_2 = dataset[:,1]
print(channel_1)
