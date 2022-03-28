<Software pro zpracování naměřených dat>
Copyright (C) <2022> <Klečka, Kadlubcová>
Tento program je svobodný software: můžete jej šířit a upravovat podle ustanovení Obecné veřejné licence GNU (GNU General Public Licence), vydávané Free Software Foundation a to buď podle 3. verze této Licence, nebo (podle vašeho uvážení) kterékoli pozdější verze.
Tento program je rozšiřován v naději, že bude užitečný, avšak BEZ JAKÉKOLIV ZÁRUKY. Neposkytují se ani odvozené záruky PRODEJNOSTI anebo VHODNOSTI PRO URČITÝ ÚČEL. Další podrobnosti hledejte v Obecné veřejné licenci GNU.
Kopie a český překlad Obecné veřejné licence GNU je k dispozici spolu s tímto programem na Sharepointu. Pokud se tak nestalo, originál licence najdete zde: <http://www.gnu.org/licenses/>.
Kontakt na autora: miriam.kadlubcova@vsb.cz 

import matplotlib
import matplotlib.pyplot as plt
import os,re,glob
import pathlib
import pandas as pd
import collections
import statistics
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.patches as mpatches
import csv

#################################################################################################
i=0
x=[]
poleP=[]
poleK=[]
poleN=[]
Hrom_Pole =[]
Nas_Prum1=[]
Nas_Prum2=[]
Nas_Prum3=[]
Tisk=[]
fin=[]
tin=[]
kin=[]
P1=[]
P2=[]
P3=[]
P4=[]
path = r'E:\Ĺ kola+Python+data\PlotMiriam\Miriam_plot\vodni clona\2020.10.19\zelena\tryska B2\25mm'
path2 = r'E:\Ĺ kola+Python+data\PlotMiriam\Miriam_plot\vodni clona\2020.10.19\zelena\tryska B2\50mm'
path3 = r'E:\Ĺ kola+Python+data\PlotMiriam\Miriam_plot\vodni clona\2020.10.19\zelena\tryska B2\75mm'
cislo = re.compile(r'(\d+)')
#####################nacteni souboru a vypis###################################################

def numericalSort(value):
    parts = cislo.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts


###########################################################################################################
#for nact_soubory in sorted(glob.glob(os.path.join(path, '*C1_B1_25_*.txt')),key=numericalSort):
 #   print ('Current File Being Processed is: ' + nact_soubory) #informace, ktery soubor se zpracovava

nact_soubory1= sorted(glob.glob(os.path.join(path, '*C1_B2_25_*.txt')),key=numericalSort)
pocet_souboru1 = collections.Counter(p.suffix for p in pathlib.Path(path).glob('*C1_B2_25_*'))

nact_soubory2= sorted(glob.glob(os.path.join(path2, '*C1_B2_50_*.txt')),key=numericalSort)
pocet_souboru2 = collections.Counter(p.suffix for p in pathlib.Path(path).glob('*C1_B2_50_*'))

nact_soubory3= sorted(glob.glob(os.path.join(path3, '*C1_B2_75_*.txt')),key=numericalSort)
pocet_souboru3 = collections.Counter(p.suffix for p in pathlib.Path(path).glob('*C1_B2_75_*'))


##########################################################################################################
#for file in os.listdir(path):
#    if file.endswith('.txt'):
#       print(file)
#       x.append(file)                  #pocitani souboru
#        i+=1
#print('celkem pocet souboru:' +str(i)) 
#######################Strukturovani dat####################################################################

for soubory1 in nact_soubory1:
        hodnoty_X1 = pd.read_csv(soubory1, sep = ',', skiprows=5,usecols = [1], header=None, squeeze=True)
        fin = pd.DataFrame.mean(hodnoty_X1)
        poleP.append(fin)



Nas_Prum1 = pd.array(poleP)
P1 = (Nas_Prum1[0:1])
P2 = (Nas_Prum1[1:5]*0.005)
P3 = (Nas_Prum1[5:14]*0.0005)
P4 = (Nas_Prum1[14:33]*0.00005)
Hrom_Pole = np.concatenate((P1,P2,P3,P4), axis=0)


for soubory2 in nact_soubory2:
        hodnoty_X2 = pd.read_csv(soubory2, sep = ',', skiprows=5,usecols = [1], header=None, squeeze=True)
        tin = pd.DataFrame.mean(hodnoty_X2)
        poleK.append(tin)


Nas_Prum2 = pd.array(poleK)
K1 = (Nas_Prum2[0:1])
K2 = (Nas_Prum2[1:5]*0.005)
K3 = (Nas_Prum2[5:14]*0.0005)
K4 = (Nas_Prum2[14:33]*0.00005)
Hrom_Pole2 = np.concatenate((K1,K2,K3,K4), axis=0)

for soubory3 in nact_soubory3:
        hodnoty_X3 = pd.read_csv(soubory3, sep = ',', skiprows=5,usecols = [1], header=None, squeeze=True)
        kin = pd.DataFrame.mean(hodnoty_X3)
        poleN.append(kin)


Nas_Prum3 = pd.array(poleN)
N1 = (Nas_Prum3[0:1])
N2 = (Nas_Prum3[1:5]*0.005)
N3 = (Nas_Prum3[5:14]*0.0005)
N4 = (Nas_Prum3[14:33]*0.00005)
Hrom_Pole3 = np.concatenate((N1,N2,N3,N4), axis=0)

#print('PrĹŻmÄ›ry ze souborĹŻ:',Nas_Prum)
#print(Hrom_Pole)
with open('B2.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=';')
    csv_writer.writerow('25mm')
    csv_writer.writerow(Hrom_Pole)
    csv_writer.writerow('50mm')
    csv_writer.writerow(Hrom_Pole2)
    csv_writer.writerow('75mm')
    csv_writer.writerow(Hrom_Pole3)
    

##################Tisk grafu#################################################################################
DP = mpatches.Patch(color='tab:blue', label='25mm')
P = mpatches.Patch(color='tab:green', label='50mm')
SP = mpatches.Patch(color='tab:orange', label='75mm')

x1 = range(len(Hrom_Pole))
y1 = Hrom_Pole

x2 = range(len(Hrom_Pole2))
y2 = Hrom_Pole2

x3 = range(len(Hrom_Pole3))
y3 = Hrom_Pole3

fig,((ax,ax2),(ax3,ax4),) = plt.subplots(2,2,sharex=False, sharey=False)
fig.suptitle('Tryska B2-ZelenĂˇ dioda (532 nm)')


ax.plot(x1,y1,'.',color='tab:blue')
ax.plot(x2,y2,'.',color='tab:green')
ax.plot(x3,y3,'.',color='tab:orange')
#ax.set_label('B1 25mm 50mm 75mm')
ax.legend(handles =[DP,P,SP])
ax.set_yscale('log')
ax.set_xticks(np.arange(min(x1), max(x1)+1, 1.0),'linear')
#ax.grid(axis='x',which='both')
ax.set_xlabel('ÄŚĂ­slo kroku')
ax.set_ylabel('Apmlituda')
#ax.legend()
#ax.xaxis.set_ticks(len(x))

ax2.plot(x1,y1,'.',color='tab:blue')
#ax2.set_title('25mm')
ax2.legend(handles =[DP])
ax2.set_yscale('log')
ax2.set_xticks(np.arange(min(x1), max(x1)+1, 1.0),'linear')
ax2.set_xlabel('cisloslo kroku')
ax2.set_ylabel('Apmlituda')             


ax3.plot(x2,y2,'.',color='tab:green')
ax3.legend(handles =[P])
#ax3.set_title('50mm')
ax3.set_yscale('log')
ax3.set_xticks(np.arange(min(x1), max(x1)+1, 1.0),'linear')
ax3.set_xlabel('cisl kroku')
ax3.set_ylabel('Apmlituda')
              
ax4.plot(x3,y3,'.',color='tab:orange')
#ax4.set_title('75mm')
ax4.legend(handles =[SP])
ax4.set_yscale('log')
ax4.set_xticks(np.arange(min(x1), max(x1)+1, 1.0),'linear')
ax4.set_xlabel('cislo kroku')
ax4.set_ylabel('Apmlituda')
               
#fig.tight_layout()
plt.show()
#plt.rcParams['pdf.fonttype'] = 42
#plt.rcParams['font.family'] = 'Calibri'

#with PdfPages('B1Yell.pdf') as pdf:
 #   plt.plot([1,4,3])
  #  pdf.savefig()