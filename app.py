from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
import pyautogui

i = 0

def domicilioE():
    servico = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    prefs = {'download.prompt_for_download': True,
             'download.directory_upgrade': True,
             'plugins.always_open_pdf_externally' : False
            }
    options.add_experimental_option('prefs', prefs)
    navegador = webdriver.Chrome(service=servico, options=options)

    navegador.get("https://sso.cloud.pje.jus.br/auth/realms/pje/protocol/openid-connect/auth?client_id=domicilio-eletronico-frontend&redirect_uri=https%3A%2F%2Fdomicilio-eletronico.pdpj.jus.br%2Fhome&state=796038f1-2a7b-4b4e-8aea-2ee2463752b7&response_mode=fragment&response_type=code&scope=openid&nonce=8bf993c6-c1fd-4814-92d4-14ecd86d8956")
    navegador.maximize_window()
    time.sleep(3)
    
    pyautogui.click(x=1549, y=1048)
    time.sleep(1)
    pyautogui.click(x=1547, y=841, button='right')
    time.sleep(1)
    pyautogui.click(x=1394, y=626)
    time.sleep(3)

    pyautogui.press('tab', presses=4)
    time.sleep(2)
    pyautogui.press('down', presses=i)
    time.sleep(2)
    pyautogui.keyDown('ctrl')
    pyautogui.press('tab')
    pyautogui.keyUp('ctrl')
    pyautogui.press('space')
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(12)
    navegador.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div[1]/div/div/form/div/div/div/div[7]/a/span[2]').click()
    time.sleep(5)
    try:
        ## Aceite de termo de início
        navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-assinatura-termo/app-termo/div/mat-card/div[3]/mat-checkbox/label/span[2]').click()
        navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-assinatura-termo/app-termo/div/mat-card/div[4]/button[2]').click()
        time.sleep(8)
        navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-confirmacao-dados/div/app-confirma-dados-pj/form/mat-card/mat-card-content/div[2]/div[2]/div/mat-form-field/div/div[1]/div[3]/input').send_keys("cargo")    
        navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-confirmacao-dados/div/app-confirma-dados-pj/form/mat-card/mat-card-content/div[5]/button').click()
        time.sleep(3)
        navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-confirmacao-dados/div/app-administrador-geral/mat-card/mat-card-content/form/div[1]/div/mat-form-field/div/div[1]/div[3]/input').send_keys("Nome")
        time.sleep(2)
        navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-confirmacao-dados/div/app-administrador-geral/mat-card/mat-card-content/form/div[2]/div[1]/mat-form-field/div/div[1]/div[3]/input').send_keys("email")
        time.sleep(2)
        navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-confirmacao-dados/div/app-administrador-geral/mat-card/mat-card-content/form/div[2]/div[2]/mat-form-field/div/div[1]/div[3]/input').send_keys("telefone")
        time.sleep(2)
        navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-confirmacao-dados/div/app-administrador-geral/mat-card/mat-card-content/form/div[2]/div[3]/mat-form-field/div/div[1]/div[3]/input').send_keys("cargo")
        time.sleep(2)
        navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-confirmacao-dados/div/app-administrador-geral/mat-card/mat-card-content/form/div[3]/div[2]/button').click()
        time.sleep(2)
        navegador.find_element('xpath', '/html/body/div[3]/div[2]/div/mat-dialog-container/app-cadastro-erro-modal/div/button').click()
        time.sleep(2)
        
        ## Aceito de coligada
        navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-home/div/div[1]/div/div/div/div[1]/p/a').click()
        time.sleep(2)
        navegador.find_element('xpath', '/html/body/div[3]/div[2]/div/mat-dialog-container/app-aceite-vinculacao/div[2]/button[2]').click()
        time.sleep(2)
        #ADMINISTRADORES
        navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-home/div/div[3]/mat-card[4]/mat-card-header/div/mat-card-title').click()
        time.sleep(2)
        navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-usuarios-list/div/mat-card/div[1]/button').click()
        time.sleep(2)
        navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-add-usuario/app-cadastro-usuario/div/mat-card[1]/mat-card-content/form/div[1]/div[1]/div/div/mat-form-field/div/div[1]/div[3]/input').send_keys("cpf")
        time.sleep(2)
        navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-add-usuario/app-cadastro-usuario/div/mat-card[1]/mat-card-content/form/div[2]/div[1]/mat-form-field/div/div[1]/div[3]/input').send_keys("email")
        time.sleep(2)
        navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-add-usuario/app-cadastro-usuario/div/mat-card[1]/mat-card-content/form/div[2]/div[1]/mat-form-field/div/div[1]/div[3]/input').clear()
        navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-add-usuario/app-cadastro-usuario/div/mat-card[1]/mat-card-content/form/div[2]/div[1]/mat-form-field/div/div[1]/div[3]/input').send_keys("email")
        time.sleep(2)
        navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-add-usuario/app-cadastro-usuario/div/mat-card[1]/mat-card-content/form/div[3]/div/mat-form-field/div/div[1]/div[3]/input').send_keys("Cargo")
        time.sleep(2)
        navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-add-usuario/app-cadastro-usuario/div/mat-card[1]/mat-card-content/form/div[4]/div/mat-form-field/div/div[1]/div[3]/mat-select/div/div[2]').click()
        time.sleep(2)
        navegador.find_element('xpath', '/html/body/div[3]/div[2]/div/div/div/mat-option[1]').click()
        time.sleep(2)
        navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-add-usuario/app-cadastro-usuario/div/mat-card[1]/mat-card-content/form/div[4]/div[2]/mat-form-field/div/div[1]/div[3]/input').send_keys("OAB")
        time.sleep(2)
        navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-add-usuario/app-cadastro-usuario/div/mat-card[1]/mat-card-content/form/div[4]/div[3]/mat-form-field/div/div[1]/div[3]/mat-select/div/div[2]').click()
        time.sleep(2)
        navegador.find_element('xpath', '/html/body/div[3]/div[2]/div/div/div/mat-option[25]').click()
        time.sleep(2)
        navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-add-usuario/app-cadastro-usuario/div/mat-card[1]/mat-card-content/form/div[6]/div/div[4]/div/mat-checkbox/label/span[2]').click()
        time.sleep(2)
        navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-add-usuario/app-cadastro-usuario/div/mat-card[3]/div/div[2]/button').click()
        time.sleep(3)
        navegador.find_element('xpath', '/html/body/div[3]/div[2]/div/mat-dialog-container/app-sucesso-modal/div/button').click()
        time.sleep(2)
    except:
        try:
            ## Aceito de coligada
            navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-home/div/div[1]/div/div/div/div[1]/p/a').click()
            time.sleep(2)
            navegador.find_element('xpath', '/html/body/div[3]/div[2]/div/mat-dialog-container/app-aceite-vinculacao/div[2]/button[2]').click()
            time.sleep(2)
            try:
                #ADMINISTRADORES
                navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-home/div/div[3]/mat-card[4]/mat-card-header/div/mat-card-title').click()
                time.sleep(2)
                navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-usuarios-list/div/mat-card/div[1]/button').click()
                time.sleep(2)
                navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-add-usuario/app-cadastro-usuario/div/mat-card[1]/mat-card-content/form/div[1]/div[1]/div/div/mat-form-field/div/div[1]/div[3]/input').send_keys("CPF")
                time.sleep(2)
                navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-add-usuario/app-cadastro-usuario/div/mat-card[1]/mat-card-content/form/div[2]/div[1]/mat-form-field/div/div[1]/div[3]/input').send_keys("email")
                time.sleep(2)
                navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-add-usuario/app-cadastro-usuario/div/mat-card[1]/mat-card-content/form/div[2]/div[1]/mat-form-field/div/div[1]/div[3]/input').clear()
                navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-add-usuario/app-cadastro-usuario/div/mat-card[1]/mat-card-content/form/div[2]/div[1]/mat-form-field/div/div[1]/div[3]/input').send_keys("Email")
                time.sleep(2)
                navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-add-usuario/app-cadastro-usuario/div/mat-card[1]/mat-card-content/form/div[3]/div/mat-form-field/div/div[1]/div[3]/input').send_keys("Cargo")
                time.sleep(2)
                navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-add-usuario/app-cadastro-usuario/div/mat-card[1]/mat-card-content/form/div[4]/div/mat-form-field/div/div[1]/div[3]/mat-select/div/div[2]').click()
                time.sleep(2)
                navegador.find_element('xpath', '/html/body/div[3]/div[2]/div/div/div/mat-option[1]').click()
                time.sleep(2)
                navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-add-usuario/app-cadastro-usuario/div/mat-card[1]/mat-card-content/form/div[4]/div[2]/mat-form-field/div/div[1]/div[3]/input').send_keys("OAB")
                time.sleep(2)
                navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-add-usuario/app-cadastro-usuario/div/mat-card[1]/mat-card-content/form/div[4]/div[3]/mat-form-field/div/div[1]/div[3]/mat-select/div/div[2]').click()
                time.sleep(2)
                navegador.find_element('xpath', '/html/body/div[3]/div[2]/div/div/div/mat-option[25]').click()
                time.sleep(2)
                navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-add-usuario/app-cadastro-usuario/div/mat-card[1]/mat-card-content/form/div[6]/div/div[4]/div/mat-checkbox/label/span[2]').click()
                time.sleep(2)
                navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-add-usuario/app-cadastro-usuario/div/mat-card[3]/div/div[2]/button').click()
                time.sleep(3)
                navegador.find_element('xpath', '/html/body/div[3]/div[2]/div/mat-dialog-container/app-sucesso-modal/div/button').click()
                time.sleep(2)
            except:
                try:
                    navegador.find_element('xpath', '/html/body/div[3]/div/div/snack-bar-container/div/div/app-snackbar/div/div[2]/button').click()
                    time.sleep(2)
                except:
                    navegador.find_element('xpath', '/html/body/div[3]/div[3]/div/mat-dialog-container/app-erro-form-modal/div/button').click()
                    time.sleep(2)
        except:
            try:
                #ADMINISTRADORES
                navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-home/div/div[3]/mat-card[4]/mat-card-header/div/mat-card-title').click()
                time.sleep(2)
                navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-usuarios-list/div/mat-card/div[1]/button').click()
                time.sleep(2)
                navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-add-usuario/app-cadastro-usuario/div/mat-card[1]/mat-card-content/form/div[1]/div[1]/div/div/mat-form-field/div/div[1]/div[3]/input').send_keys("cpf")
                time.sleep(2)
                navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-add-usuario/app-cadastro-usuario/div/mat-card[1]/mat-card-content/form/div[2]/div[1]/mat-form-field/div/div[1]/div[3]/input').send_keys("email")
                time.sleep(2)
                navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-add-usuario/app-cadastro-usuario/div/mat-card[1]/mat-card-content/form/div[2]/div[1]/mat-form-field/div/div[1]/div[3]/input').clear()
                navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-add-usuario/app-cadastro-usuario/div/mat-card[1]/mat-card-content/form/div[2]/div[1]/mat-form-field/div/div[1]/div[3]/input').send_keys("Email")
                time.sleep(2)
                navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-add-usuario/app-cadastro-usuario/div/mat-card[1]/mat-card-content/form/div[3]/div/mat-form-field/div/div[1]/div[3]/input').send_keys("cargo")
                time.sleep(2)
                navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-add-usuario/app-cadastro-usuario/div/mat-card[1]/mat-card-content/form/div[4]/div/mat-form-field/div/div[1]/div[3]/mat-select/div/div[2]').click()
                time.sleep(2)
                navegador.find_element('xpath', '/html/body/div[3]/div[2]/div/div/div/mat-option[1]').click()
                time.sleep(2)
                navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-add-usuario/app-cadastro-usuario/div/mat-card[1]/mat-card-content/form/div[4]/div[2]/mat-form-field/div/div[1]/div[3]/input').send_keys("OAB")
                time.sleep(2)
                navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-add-usuario/app-cadastro-usuario/div/mat-card[1]/mat-card-content/form/div[4]/div[3]/mat-form-field/div/div[1]/div[3]/mat-select/div/div[2]').click()
                time.sleep(2)
                navegador.find_element('xpath', '/html/body/div[3]/div[2]/div/div/div/mat-option[25]').click()
                time.sleep(2)
                navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-add-usuario/app-cadastro-usuario/div/mat-card[1]/mat-card-content/form/div[6]/div/div[4]/div/mat-checkbox/label/span[2]').click()
                time.sleep(2)
                navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/div[2]/app-add-usuario/app-cadastro-usuario/div/mat-card[3]/div/div[2]/button').click()
                time.sleep(3)
                navegador.find_element('xpath', '/html/body/div[3]/div[2]/div/mat-dialog-container/app-sucesso-modal/div/button').click()
                time.sleep(2)
            except:
                try:
                    navegador.find_element('xpath', '/html/body/div[3]/div/div/snack-bar-container/div/div/app-snackbar/div/div[2]/button').click()
                    time.sleep(2)
                except:
                    navegador.find_element('xpath', '/html/body/div[3]/div[3]/div/mat-dialog-container/app-erro-form-modal/div/button').click()
                    time.sleep(2)

    # SAIR DA CONTA
    navegador.find_element('xpath', '/html/body/app-root/uikit-layout/mat-sidenav-container/mat-sidenav-content/uikit-header/mat-toolbar/span[2]/uikit-userinfo/button/span[1]/div/div[2]/span').click()
    time.sleep(3)
    try:
        navegador.find_element('xpath', '/html/body/div[3]/div[2]/div/div/div/mat-list/mat-action-list/a/div').click()
        time.sleep(3)
    except:
        navegador.find_element('xpath', '/html/body/div[3]/div[3]/div/div/div/mat-list/mat-action-list/a/div').click()
        time.sleep(3)
    
    navegador.close()
    print(f"Processo concluído no certificado {i + 1}")
    
while i < 2:
    domicilioE()
    i += 1
