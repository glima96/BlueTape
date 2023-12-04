from time import sleep
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd


def seleciona_moda(navegador):

    navegador.execute_script("window.scrollBy(0, 1300);")

    xpath='//*[@id="homeRankings"]/div/div[2]/nav/div[2]/button[2]'

    for i in range(15):
        print(i + 1)
        try:
            navegador.find_element(By.XPATH, xpath).click()
            print("OK")
            break
        except:
            ("NÃO")
        sleep(1)




def get_percentuais(link):




    try:

        navegador = inicia_pagina(link)
        navegador.execute_script("window.scrollBy(0, 500);")
        xpath = '//*[@id="reputation"]/div[2]/div[1]/div[1]/span'
        xpath = '//*[@id="reputation"]/div[2]/div[1]/div[1]/span'
        respondidas = navegador.find_element('xpath', xpath)
        respondidas = respondidas.text

        xpath = '//*[@id="reputation"]/div[2]/div[1]/div[2]/span'
        voltaria_negociar = navegador.find_element('xpath', xpath)
        voltaria_negociar = voltaria_negociar.text

        xpath = '//*[@id="reputation"]/div[2]/div[1]/div[3]/span'
        indice_solucao = navegador.find_element('xpath', xpath)
        indice_solucao = indice_solucao.text

        xpath = '//*[@id="reputation"]/div[2]/div[1]/div[4]/span'
        nota_consumidor = navegador.find_element('xpath', xpath)
        nota_consumidor = nota_consumidor.text

        Notas = [respondidas, voltaria_negociar, indice_solucao, nota_consumidor]
        navegador.quit()

        return Notas

    except Exception as e:

        navegador = inicia_pagina(link)
        xpath = '//*[@id="reputation"]/div[3]/div[1]/div[1]/span'
        respondidas = navegador.find_element('xpath', xpath)
        respondidas = respondidas.text

        xpath = '//*[@id="reputation"]/div[3]/div[1]/div[2]/span'
        voltaria_negociar = navegador.find_element('xpath', xpath)
        voltaria_negociar = voltaria_negociar.text

        xpath = '//*[@id="reputation"]/div[3]/div[1]/div[3]/span'
        indice_solucao = navegador.find_element('xpath', xpath)
        indice_solucao = indice_solucao.text

        xpath = '//*[@id="reputation"]/div[3]/div[1]/div[4]/span'
        nota_consumidor = navegador.find_element('xpath', xpath)
        nota_consumidor = nota_consumidor.text
        Notas = [respondidas, voltaria_negociar, indice_solucao, nota_consumidor]

        navegador.quit()

        return Notas


def get_dados(xpath,navegador):
    tamanho_do_vetor=0
    vet=[]
    for i in range(15):
        print(i + 1)
        try:
            empresa = navegador.find_element('xpath', xpath)
            link = empresa.get_attribute("href")
            vet = empresa.text.split('\n')
            print("OK")
            break
        except:
            ("NÃO")
        sleep(1)





    nome=vet[1]

    nota=vet[2]

    if tamanho_do_vetor==4:
        nome = vet[2]

        nota = vet[3]



    percentuais=get_percentuais(link)

    print(percentuais)

    Empresa=[nome,nota,percentuais[0],percentuais[1],percentuais[2],percentuais[3]]


    return Empresa


def inicia_pagina(link):
#identifica versao do chrome atual e instala o driver correspondente
    servico = Service(ChromeDriverManager().install())

    navegador = webdriver.Chrome(service=servico)

    navegador.get(link)


    return navegador




link="https://www.reclameaqui.com.br"
navegador=inicia_pagina(link)
seleciona_moda(navegador)


print("--------------------------------")

xpath='//*[@id="homeRankings"]/div/div[2]/div[3]/div/div[1]/a[1]'
TopOne= get_dados(xpath,navegador)
print(TopOne)


print("--------------------------------")

xpath='//*[@id="homeRankings"]/div/div[2]/div[3]/div/div[1]/a[2]'
TopTwo= get_dados(xpath,navegador)
print(TopTwo)

print("--------------------------------")

xpath='//*[@id="homeRankings"]/div/div[2]/div[3]/div/div[1]/a[3]'
TopThree= get_dados(xpath,navegador)
print(TopThree)

print("--------------------------------")


xpath='//*[@id="homeRankings"]/div/div[2]/div[3]/div/div[2]/a[1]'
WorstOne= get_dados(xpath,navegador)
print(WorstOne)


print("--------------------------------")

xpath='//*[@id="homeRankings"]/div/div[2]/div[3]/div/div[2]/a[2]'
WorstTwo= get_dados(xpath,navegador)
print(WorstTwo)

print("--------------------------------")

xpath='//*[@id="homeRankings"]/div/div[2]/div[3]/div/div[2]/a[3]'
WorstThree= get_dados(xpath,navegador)
print(WorstThree)


navegador.quit()

legenda = ['Nome', 'Nota', 'Percentutal Respondido','Percentual Voltaria Negociar','Indice Solução','Nota Consumidor']
dados = pd.DataFrame({
    'Legenda': legenda,
    'Top1': TopOne,
    'Top2': TopTwo,
    'Top3': TopThree,
    'Worst1': WorstOne ,
    'Worst2': WorstTwo,
    'Worst3': WorstThree
})


nome_arquivo_excel = 'dados.xlsx'
if os.path.exists(nome_arquivo_excel):

    os.remove(nome_arquivo_excel)
dados.to_excel(nome_arquivo_excel, index=False)





input("Pressione <enter> para continuar")

