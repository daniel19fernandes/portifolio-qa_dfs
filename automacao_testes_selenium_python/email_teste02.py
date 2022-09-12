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
email = "daniel+.com>email"
senha = 123456789
mensagem_sucesso = "REGISTRO CONCLUÍDO COM SUCESSO"

time.sleep(2)

## EMAIL_TESTE02 - Este teste consiste em inputar um e-mail fora do formato correto para conferir se é aceito pelo sistema.
## Resultado esperado: "TESTE INVÁLIDO"


campo_email = navegador.find_element(By.XPATH, '//*[@id="form"]/div[2]/input').send_keys(email)

## Prenchimento do resto do formulário
campo_nome_completo = navegador.find_element(By.XPATH, '//*[@id="form"]/div[1]/input').send_keys(nome)
campo_senha = navegador.find_element(By.XPATH, '//*[@id="form"]/div[3]/input'). send_keys(senha)
campo_repita_senha = navegador.find_element(By.XPATH, '//*[@id="form"]/div[4]/input').send_keys(senha)
botao_enviar =  navegador.find_element(By.XPATH, '//*[@id="form"]/button').click()

time.sleep(2)

## Verificação de aceite

mensagem_de_sucesso = navegador.find_element(By.XPATH, '/html/body/div/h1')

if (mensagem_de_sucesso.text == mensagem_sucesso):
    print("TESTE VÁLIDO")
else:
    print("TESTE INVÁLIDO")



input('----------')

