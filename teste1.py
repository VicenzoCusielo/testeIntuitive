import urllib3
from bs4 import BeautifulSoup
import wget
import shutil
import os

#importar biblioteca urllib3 para requisitar get no site
varUrl = "https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude"
varConnect = urllib3.PoolManager()
varReturn = varConnect.request('get', varUrl)

#importar biblioteca Beautifulsoup para tratamento de dados de retorno
page = BeautifulSoup(varReturn.data,"html.parser")

#encontrando os links de interesse na página, eles são indereçados como internal-link, selecionando os Anexos, baixando e compactando
dados = []
local = 'anexos//'
#caso a pasta com endereço da variavel local não existir ele a pasta é criada
if not os.path.exists(local): 
    os.makedirs(local)
for link in page.find_all('a', class_='internal-link'):
    if 'Anexo' in link.get('href'):
        wget.download(link.get('href'),local)
shutil.make_archive('compactado', 'zip', local)


