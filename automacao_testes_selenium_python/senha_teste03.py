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
senha = 1234567
mensagem_sucesso = "REGISTRO CONCLUÍDO COM SUCESSO"

time.sleep(2)

## SENHA_TESTE03 - Este teste consiste em inputar uma senha com 7 caracteres para conferir se é aceita pelo sistema.
## Resultado esperado: "TESTE INVÁLIDO"


campo_senha = navegador.find_element(By.XPATH, '//*[@id="form"]/div[3]/input'). send_keys(senha)


## Prenchimento do resto do formulário
campo_nome_completo = navegador.find_element(By.XPATH, '//*[@id="form"]/div[1]/input').send_keys(nome)
campo_email = navegador.find_element(By.XPATH, '//*[@id="form"]/div[2]/input').send_keys(email)
campo_repita_senha = navegador.find_element(By.XPATH, '//*[@id="form"]/div[4]/input').send_keys(senha)
botao_enviar =  navegador.find_element(By.XPATH, '//*[@id="form"]/button').click()

time.sleep(2)

## Verificação de aceite

mensagem_erro_esperada = "digite uma senha com no mínimo 8 caracteres"

mensagem_erro_real = navegador.find_element(By.XPATH, '//*[@id="form"]/div[3]/span')

if (mensagem_erro_esperada == mensagem_erro_real.text):
    print("TESTE VÁLIDO")
else:
    print("TESTE INVÁLIDO")



input('----------')


