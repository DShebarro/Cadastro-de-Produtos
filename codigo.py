# 1 - Entrar no sistema da empresa (https://dlp.hashtagtreinamentos.com/python/intensivao/login)
import pyautogui
import time
import pandas  

pyautogui.PAUSE = 0.9 # um intervalo para o codigo não atropelar a execução da linhas

# Abrir o Navegador
#Apertar a tecla do WINDOWS  

pyautogui.press('win')
pyautogui.write('brave')
pyautogui.press('enter')

time.sleep(2)
# 2 - Fazendo o login 
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)
pyautogui.press('enter')

time.sleep(3) # esperar por 3 segundos para pausar o codigo

# Localizando o posição de onde o mouse está na tela para clicar
pyautogui.click(x=557, y=370)
pyautogui.write('davyshebarrosouza18@gmail.com')

# Passar para o proximo campo usando o TAB

pyautogui.press('tab')
pyautogui.write('x20ds019@')
pyautogui.press('tab')
pyautogui.press('enter')

# 3 - importar a base de dados

import pandas

tabela = pandas.read_csv('produtos.csv')
print(tabela)

# 4 - Cadastrar 1 produto 

 
#para cada linha da minha tabela ele execute os comandos abaixo:
for linha in tabela.index:

    pyautogui.click(x=674, y=285)

    # Código
    codigo = tabela.loc[linha, 'codigo'] #cordenadas de localização da meu dataset 
    pyautogui.write(str(codigo)) # Usando a localização do meu produto e transformando ele em string
    pyautogui.press('tab')

    # Marca
    marca = tabela.loc[linha, 'marca']
    pyautogui.write(str(marca))
    pyautogui.press('tab')

    # Tipo de Produto
    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(str(tipo))
    pyautogui.press('tab')

    # Categoria de Produto
    categoria = tabela.loc[linha, 'categoria']
    pyautogui.write(str(categoria))
    pyautogui.press('tab')

    # Preço Unitário
    preco = tabela.loc[linha, 'preco_unitario']
    pyautogui.write(str(preco))
    pyautogui.press('tab')

    # Custo de Produto
    custo = tabela.loc[linha, 'custo']
    pyautogui.write(str(custo))
    pyautogui.press('tab')

    # Observação
    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press('tab')

    #Clicar para enviar para cadastro

    pyautogui.press('enter')
    pyautogui.scroll(5000)

    # 5 - Repetir o processo de cadastro até até acabar os produtos 