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
nome = "Da"
email = "daniel@email.com"
senha = 123456789
mensagem_sucesso = "REGISTRO CONCLUÍDO COM SUCESSO"


time.sleep(2)

## NOME_COMPLETO_TESTE 04 - Este teste consiste em verificar se, quando houver uma entrada de uma palavra que não atenda os requisitos, aparece o erro com a seguinte frase "o nome deve ter no mínimo 3 letras".
## Resultado esperado: TESTE VÁLIDO.

## Preenchimento do campo "Nome Completo" com a palavra "Da"
campo_nome_completo = navegador.find_element(By.XPATH, '//*[@id="form"]/div[1]/input')
campo_nome_completo.send_keys(nome)

## Prenchimento do resto do formulário
campo_email = navegador.find_element(By.XPATH, '//*[@id="form"]/div[2]/input').send_keys(email)
campo_senha = navegador.find_element(By.XPATH, '//*[@id="form"]/div[3]/input'). send_keys(senha)
campo_repita_senha = navegador.find_element(By.XPATH, '//*[@id="form"]/div[4]/input').send_keys(senha)
botao_enviar =  navegador.find_element(By.XPATH, '//*[@id="form"]/button').click()

time.sleep(2)

## Verificação de aceite

mensagem_erro_esperada = "o nome deve ter no mínimo 3 letras"

mensagem_erro_real = navegador.find_element(By.XPATH, '//*[@id="form"]/div[1]/span')

if (mensagem_erro_esperada == mensagem_erro_real.text):
    print("TESTE VÁLIDO")
else:
    print("TESTE INVÁLIDO")







input('----------')