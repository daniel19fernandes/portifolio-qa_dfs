from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
import time
url = "file:///C:/Users/danie/Desktop/Portif%C3%B3lio/html-css/index.html"
navegador.get(url)

## Definições
nome = "Daniel"
email = "daniel@email.com"
senha = 123456789
mensagem_sucesso = "REGISTRO CONCLUÍDO COM SUCESSO"

time.sleep(2)

## BOTAO_TESTE02 - Este teste consiste no não preenchimento de nenhum campo obrigatório e o click o "enviar", esperando como resultado o não submit da página.
## Resultado esperado: TESTE INVÁLIDO



## botão "enviar"
botao_enviar =  navegador.find_element(By.XPATH, '//*[@id="form"]/button').click()

time.sleep(2)

## Verificação de aceite

mensagem_de_sucesso = navegador.find_element(By.XPATH, '/html/body/div/h1')

if (mensagem_de_sucesso.text == mensagem_sucesso):
    print("TESTE VÁLIDO")
else:
    print("TESTE INVÁLIDO")



input('----------')


