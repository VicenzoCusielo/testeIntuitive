import shutil
import os
import tabula
import pandas as pd
local = 'tabelaZip'
if not os.path.exists(local): 
    os.makedirs(local)
    
#extrair do anexoI a tabela em formato .csv
tabula.convert_into('anexos/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536_RN537_RN538_RN539_RN541_RN542_RN544_546_571_577.pdf', 'tabelaZip//Tabela.csv', pages='all', output_format='csv')

#substituir dados com a legenda
with open('tabelaZip//Tabela.csv') as arquivo:
    texto = arquivo.read()
texto = texto.replace('OD','Odontologica')
texto = texto.replace('AMB','Ambulatorial')
with open('tabelaZip//Tabela.csv', 'w') as filehandler_name:
    filehandler_name.write(texto)

#compactar em .zip
shutil.make_archive('Tabela', 'zip',local)
