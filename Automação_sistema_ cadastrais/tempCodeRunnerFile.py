1. Usar automação em Python sempre necessario se cadastrar e usar seu usuario e senha 
2. Extrair cada produto 
- clicar e digitar produto 
- clicar e digitar quantidade 
- clicar e digitar o preço 
- clicar em registarr
import pyautogui 
from  time import sleep 

# 1. Usar automação em Python sempre necessario se cadastrar e usar seu usuario e senha
pyautogui.click(1007,542,duration=2) 
pyautogui.write('carlos')

pyautogui.click(990,575,duration=2)  
pyautogui.write('123456')

pyautogui.click(855,615,duration=2) 
# 2. Extrair cada produto 
with open('produtos.txt','r') as file:
    for line in file:
       produto = line.split(',')[0]
       quantidade = line.split(',')[1]
       preco = line.split(',')[2]
# - clicar e digitar produto 
pyautogui.click(1018,531,duration=2) 
pyautogui.write(produto)
# - clicar e digitar quantidade 
pyautogui.click(1018,556,duration=2)
pyautogui.write(quantidade) 
# - clicar e digitar o preço 
pyautogui.click(1020,579,duration=2)
pyautogui.write(preco)
# - clicar em registrar 
pyautogui.click(901,736,duration=1)
sleep(1)
# 3. 
