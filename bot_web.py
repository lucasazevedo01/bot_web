from webbrowser import Chrome
from selenium import webdriver
from datetime import date, datetime
import pyautogui
import time

#Variavel que contém a data atual sendo convertida em string
today = datetime.today()
today2 = today.strftime("%d/%m/%Y")

#Variavel com a descrição da nota fiscal
descricao_nota = 'REFERENTE A MANUTENÇÃO E REPARO DE OUTRAS MÁQUINAS E EQUIPAMENTOS PARA USOS'\
    ' INDUSTRIAIS. Em conformidade com a LEI Nº 12.741, o valor aproximado dos tributos incidentes'\
    ' nesta nota é de R$ 1250,00.'


navegador = webdriver.Chrome()
navegador.get("https://nfse.vitoria.es.gov.br/")

#Fazer login
navegador.find_element_by_xpath('//*[@id="login"]').send_keys("aluizio-azevedo1@hotmail.com")
navegador.find_element_by_xpath('//*[@id="senha"]').send_keys("LIMA2010")
navegador.find_element_by_xpath('//*[@id="formEntrada"]/div[2]/span/span/input').click()

#Entrar na empresa
time.sleep(2)
navegador.find_element_by_xpath('//*[@id="DataTables_Table_0"]/tbody/tr/td[1]').click()

#Emitir NF
time.sleep(2)
navegador.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[1]/div[1]/div[1]/div[1]/div/div/div[1]/h3/a').click()

#Criar nova
navegador.find_element_by_xpath('//*[@id="btNova"]/a/img').click()

#Preenchimento NF
navegador.find_element_by_xpath('//*[@id="formNovo"]/div[1]/div[2]/input[2]').click()
navegador.find_element_by_xpath('//*[@id="formNovo"]/div[2]/div[2]/input').send_keys("04.999.675/0001-47")
navegador.find_element_by_xpath('//*[@id="formNovo"]/div[3]/div[2]/input').send_keys("29160450")
navegador.find_element_by_xpath('//*[@id="formNovo"]/div[4]/div[2]/input[1]').send_keys("506")
navegador.find_element_by_xpath('//*[@id="formNovo"]/div[5]/div[2]/select').send_keys("BRASIL")
navegador.find_element_by_xpath('//*[@id="formNovo"]/div[2]/div[4]/input').click()

#Preencher prestação de serviço linha 39 preenchimento da data
navegador.find_element_by_xpath('//*[@id="formNovo"]/div[8]/div[2]/input').send_keys(today2)
time.sleep(3)
#click para abrir o primeiro label
navegador.find_element_by_xpath('//*[@id="formNovo"]/div[10]/div[2]/select').click()
time.sleep(3)
navegador.find_element_by_xpath('//*[@id="formNovo"]/div[10]/div[2]/select/option[2]').click()
#Click para fechar o label
navegador.find_element_by_xpath('//*[@id="formNovo"]/h4[3]').click()
#click para abrir o segundo label
navegador.find_element_by_xpath('//*[@id="formNovo"]/div[11]/div[2]/select').click()
time.sleep(3)
navegador.find_element_by_xpath('//*[@id="formNovo"]/div[11]/div[2]/select/option[123]').click()
#Click para fechar o label
navegador.find_element_by_xpath('//*[@id="formNovo"]/h4[3]').click()

#inserir a descrição da nota
navegador.find_element_by_xpath('//*[@id="formNovo"]/p[1]/textarea').send_keys(descricao_nota)

navegador.find_element_by_xpath('//*[@id="formNovo"]/div[12]/div[2]/input').send_keys('125000')

#Preencher a aliquota
navegador.find_element_by_xpath('//*[@id="dvSelectAliquota"]/select').click()
time.sleep(3)
navegador.find_element_by_xpath('//*[@id="dvSelectAliquota"]/select/option[3]').click()
#Click para fechar o label da aliquota
navegador.find_element_by_xpath('//*[@id="formNovo"]/h4[6]').click()

#Click para emitir a NF
#navegador.find_element_by_xpath('//*[@id="btEncerrar"]/a/img').click()

#click no pop-up de confirmação
#pyautogui.click(768, 244)