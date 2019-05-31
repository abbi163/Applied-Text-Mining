import matplotlib.pyplot as plt

# Plotting specgram !!

def spectogram(x, Fs, NFFT): 

    plot.title('Plot of Spectrogram ')

    plot.subplot(211)
    plot.plot(x)

    plot.xlabel('Sample')
    plot.ylabel('Amplitude')

    plot.subplot(212)
    plot.specgram(x, Fs=Fs, NFFT = NFFT)

    plot.xlabel('Time')
    plot.ylabel('Frequency')
    plot.show()
    