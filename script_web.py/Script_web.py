import re
from colorama import Fore
import requests

website = "https://vulnhub.com/"
resultado = requests.get(website)
content = resultado.text

patron = r"/entry/ [\w-]*"
maquinas_repetidas =re.findall(patron,str(content))
sin_duplicados = list(set(maquinas_repetidas))

maquinas_final = []

for i in sin_duplicados:
    nombre_maquinas = i.replace("/entry/","")
    maquinas_final.append(nombre_maquinas)
    print(nombre_maquinas)


#####################

maquinas_noob = "noob-1"
existe_noob = False

for a in maquinas_final:
    if a == maquinas_noob:
        existe_noob = True
        break

color_verde = Fore.GREEN
color_amarillo = Fore.YELLOW

if existe_noob == True:
    print(color_verde + "no hay ninguna maquina nueva")
else:
    print( color_amarillo +"Hay maquina nueva")