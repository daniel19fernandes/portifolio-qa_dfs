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
# senha = 123456789
mensagem_sucesso = "REGISTRO CONCLUÍDO COM SUCESSO"

time.sleep(2)

## REPETIR_SENHA_TESTE03 - Este teste consiste em verificar se, após inserida uma repetição de senha errada, aparece uma mensagem de erro "as senhas devem ser iguais".
## Resultado esperado: TESTE VÁLIDO

campo_repita_senha = navegador.find_element(By.XPATH, '//*[@id="form"]/div[4]/input').send_keys("123456789")


## Prenchimento do resto do formulário
campo_nome_completo = navegador.find_element(By.XPATH, '//*[@id="form"]/div[1]/input').send_keys(nome)
campo_email = navegador.find_element(By.XPATH, '//*[@id="form"]/div[2]/input').send_keys(email)
campo_senha = navegador.find_element(By.XPATH, '//*[@id="form"]/div[3]/input'). send_keys("abcdfghij")
botao_enviar =  navegador.find_element(By.XPATH, '//*[@id="form"]/button').click()

time.sleep(2)

## Verificação de aceite

mensagem_erro_esperada = "as senhas devem ser iguais"

mensagem_erro_real = navegador.find_element(By.XPATH, '//*[@id="form"]/div[4]/span')


if (mensagem_erro_real.text == mensagem_erro_esperada):
    print("TESTE VÁLIDO")
else:
    print("TESTE INVÁLIDO")



input('----------')


