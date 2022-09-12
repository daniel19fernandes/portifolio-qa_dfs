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
# nome = "Daniel"
# email = "daniel@email.com"
# senha = 123456789
# mensagem_sucesso = "REGISTRO CONCLUÍDO COM SUCESSO"

time.sleep(2)

## BOTAO_TESTE02 - Este teste consiste no não preenchimento de nenhum campo obrigatório e o click no "enviar", testando se todas as mensagens de erro aparecem no seu respectivo campo (Nome completo "o nome deve ter no mínimo 3 letras
# " / e-mail: "digite um e-mail válido" / senha: "digite uma senha com no mínimo 8 caracteres" / repita sua senha: "as senhas devem ser iguais")
# Resultado esperado: TESTE VÁLIDO


## botão "enviar"

botao_enviar =  navegador.find_element(By.XPATH, '//*[@id="form"]/button').click()

time.sleep(2)

## Verificação de aceite


# Mensagem de erro do campo "Nome completo"
erro_nome_completo = "o nome deve ter no mínimo 3 letras"
mensagem_erro_nome_completo = navegador.find_element(By.XPATH, '//*[@id="form"]/div[1]/span')

if (erro_nome_completo == mensagem_erro_nome_completo.text):
    print("TESTE VÁLIDO - nome_completo")
else:
    print("TESTE INVÁLIDO - nome_completo")


# Mensagem de erro do campo "E-mail"
erro_email = "digite um e-mail válido"
mensagem_erro_email = navegador.find_element(By.XPATH, '//*[@id="form"]/div[2]/span')

if (erro_email == mensagem_erro_email.text):
    print("TESTE VÁLIDO - email")
else:
    print("TESTE INVÁLIDO - email")


# Mensagem de erro do campo "Senha"
erro_senha = "digite uma senha com no mínimo 8 caracteres"
mensagem_erro_senha = navegador.find_element(By.XPATH, '//*[@id="form"]/div[3]/span')

if (erro_senha == mensagem_erro_senha.text):
    print("TESTE VÁLIDO - senha")
else:
    print("TESTE INVÁLIDO - senha")


# Mensagem de erro do campo "Repita sua senha"
erro_rep_senha = "as senhas devem ser iguais"
mensagem_erro_rep_senha = navegador.find_element(By.XPATH, '//*[@id="form"]/div[4]/span')

if (erro_rep_senha == mensagem_erro_rep_senha.text):
    print("TESTE VÁLIDO - senha")
else:
    print("TESTE INVÁLIDO - senha")


input('----------')