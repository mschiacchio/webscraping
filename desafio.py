# coding = UTF-8

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

#Lista de URLs
urls = ['https://www.ofertaesperta.com/','https://www.globo.com/','https://autoesporte.globo.com/',
       'https://www.escolavirtual.gov.br/curso/213','https://www.mg.superesportes.com.br/',
       'https://medium.com/data-hackers/web-scraping-com-python-para-pregui%C3%A7osos-unindo-beautifulsoup-e-selenium-parte-2-8cfebf4f34e',
       'https://filmow.com/listas/200-filmes-obrigatorios-para-cinefilos-l56792/']

#Palavras-chave
palavras_chave = ['carro','política','tecnologia','globo','verdade','python', 'web scraping', 'auto', 'sonho',
                  'luta', 'esportes', 'busca']

#Instanciando o navegador(Google Chrome)
driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

#DataFrame Pandas para alocar os resultados 
dados = pd.DataFrame(columns=['URL', 'Palavra-chave', 'Localizada'])

#Loop pelas URLs
for url in urls:
    driver.get(url)

    #Utiliza o BeautifulSoup pra analisar o HTML da página
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    #Localiza as palavras-chave
    for palavra_chave in palavras_chave:
        localizada = False
        if palavra_chave in soup.get_text().lower():
            localizada = True

        #Aloca os resultados no DataFrame
        dados = dados.append({'URL': url, 'Palavra-chave': palavra_chave, 'Localizada': localizada}, ignore_index = True)

#Aloca os resultados em uma planilha Excel
dados.to_excel('resultados.xlsx', index = False)