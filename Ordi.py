from python_speech_features import logfbank
from python_speech_features import mfcc
from python_speech_features import delta
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import svm


def leer_audio(signal):
     (rate, sig) = wav.read(signal)
     return rate, sig

def ver_senial(signal):
    x = np.linspace(1, 4096, 4096)
    plt.figure('señal original')
    plt.plot(x,signal[0:4096])
    plt.show()

def segmentar(signal):
    for i in range(len(signal)):
        t= i+100
        muestras= list(signal[0:t])
    return muestras

def zrc(signal):
    zero_crosses = np.nonzero(np.diff(signal > 0))[0]
    return zero_crosses
#def obtener_caracteristicas(signal):


rango, senial = leer_audio('perro1.wav')
print(senial)
print("Tamaño de la muestra: ",rango)
#sen2= np.ndarray(senial)
#sacar las caracteristicas del audio
#Tam_mues= senial[:1]
#print(Tam_mues)

ver= ver_senial(senial)

muestras1= segmentar(senial)

zrc1= zrc(senial)
zrc2= list(zrc1)
tam= len(zrc2)
print("Veces que se cruza en cero: ", tam)
