import os
os.chdir(r'DIRECTORIO DE LAS FOTOS')  #Directorio de las fotos ejemplo: C:\Users\jose89fcb\Desktop\fotos
i=1
for file in os.listdir():
     src=file
     dst="Fotos"+str(i)+".png"  #El nombre "Fotos" lo puedes quitar y dejarlo en blanco
     os.rename(src,dst)
     i+=1
