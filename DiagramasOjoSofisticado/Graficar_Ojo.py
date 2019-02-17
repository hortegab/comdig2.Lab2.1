from eyediagram.mpl import eyediagram
import matplotlib.pyplot as plt
import scipy 
import numpy as np

# Configuracion del Diagrama de Ojo
# Ndat: Es el numero de datos a graficar
# Sps: El numero de muestras por simbolo del archivo generado en gnuradio
Ndat=10000 
Sps = 8 

# Leemos el archivo producido por gnuradio
f_rect=scipy.fromfile(open("Senal_Rect"), dtype=scipy.float32) 
f_nyq=scipy.fromfile(open("Senal_Nyquist"), dtype=scipy.float32) 
f_rc=scipy.fromfile(open("Senal_RC"), dtype=scipy.float32)
f_rrc=scipy.fromfile(open("Senal_RRC"), dtype=scipy.float32)


#Escogemos una porcion de datos para graficar
fp_rect=(f_rect[0:Ndat])
fp_nyq=(f_nyq[0:Ndat])
fp_rc=(f_rc[0:Ndat])
fp_rrc=(f_rrc[0:Ndat])

#Grafica para Rectangular
plt.subplot(221)
eyediagram(fp_rect, 2*Sps, offset=16, cmap=plt.cm.coolwarm)
plt.title("Pulsos de Forma Rectangular")
#plt.ylabel("Amplitud")
#plt.xlabel("Tiempo")
#plt.show()

#Grafica para Nyquist
plt.subplot(222)
eyediagram(fp_nyq, 2*Sps, offset=16, cmap=plt.cm.coolwarm)
plt.title("Pulsos de Forma de Nyquist")
#plt.show()


#Grafica para RC
plt.subplot(223)
eyediagram(fp_rc, 2*Sps, offset=16, cmap=plt.cm.coolwarm)
plt.title("Pulsos de Forma Coseno Alzado")
#plt.show()

#Grafica para RRC
plt.subplot(224)
eyediagram(fp_rrc, 2*Sps, offset=16, cmap=plt.cm.coolwarm)
plt.title("Pulsos de Forma Raiz de Coseno Alzado")
plt.show()



