from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

import time
import json
import logging

# Configuração dos logs
logging.basicConfig(level=logging.INFO,format='[%(levelname)s] %(message)s')

class PaginaScrapper:
    """
    Classe responsável por abrir a página do desafio e preencher o formulário
    automaticamente usando dados contidos em um arquivo JSON.
    """

    # Configura o Chrome para não fechar automaticamente após o script terminar
    options = Options()
    options.add_experimental_option("detach", True)

    # Inicializa o WebDriver
    var_webBot = webdriver.Chrome(options=options)

    # Caminho do arquivo JSON contendo os dados para preenchimento
    var_ArquivoJson = 'Json/desafio_1.json'

    @classmethod
    def abrir_navegador(cls):
        """
        Abre o navegador, acessa a página do desafio e maximiza a janela.

        :param cls: Referência à classe (método de classe)
        """

        cls.var_webBot.get('https://curso-web-scraping.pages.dev/#/desafio/1')
        cls.var_webBot.maximize_window()
        logging.info("Navegador aberto com sucesso!!")
        time.sleep(3) # dalay para aguardar a página carregar completamente

    @classmethod
    def preencher_formulario(cls):
        """
        Lê o arquivo JSON e utiliza os dados para preencher e enviar
        o formulário várias vezes (um envio para cada item da lista).

        :param cls: Referência à classe (método de classe)
        """

        # Lê o arquivo JSON
        with open(cls.var_ArquivoJson) as file:
            cls.var_strDadosJson = json.load(file)

        logging.info(f"Registros encontrados: {len(cls.var_strDadosJson)}")

        for index,item in enumerate(cls.var_strDadosJson, start=1):

            logging.info(f"Preenchendo registro {index}: {item['email']}")

            # Divide a data de nascimento (YYYY-MM-DD)
            var_strAnoNascimento, var_strMesNascimento, var_strDiaNascimento = item['data-de-nascimento'].split('-')

            # Remove zeros à esquerda (ex: 09 --> 9)
            var_strMesNascimento = str(int(var_strMesNascimento))
            var_strDiaNascimento = str(int(var_strDiaNascimento))

            # ------------ Preenche campos do formulário ---
            
            # Campo de e-mail
            input_campoUser = cls.var_webBot.find_element(By.NAME, 'email')
            input_campoUser.clear()
            input_campoUser.send_keys(item['email'])

            # Campo de senha
            input_campoSenha = cls.var_webBot.find_element(By.NAME, 'senha')
            input_campoSenha.clear()
            input_campoSenha.send_keys(item['senha'])

            # Preenche a data de nascimento (dia, mês, ano)
            Select(cls.var_webBot.find_element(By.NAME, 'dia')).select_by_visible_text(var_strDiaNascimento)
            Select(cls.var_webBot.find_element(By.NAME, 'mes')).select_by_visible_text(var_strMesNascimento)
            Select(cls.var_webBot.find_element(By.NAME, 'ano')).select_by_visible_text(var_strAnoNascimento)

            # Switch da newsletter (on/off)
            butn_NewsLetter = cls.var_webBot.find_element(By.ID, 'airplane-mode')
            switch_on = butn_NewsLetter.get_attribute('aria-checked') == 'true'

            # Altera apenas se estiver diferente do desejado
            if switch_on != item['newsletter']:
                butn_NewsLetter.click()

            # Botão de 'Enviar'
            btn_Enviar = cls.var_webBot.find_element(By.CSS_SELECTOR, 'form button[type="submit"]')
            btn_Enviar.click()

            logging.info(f"Formulário {index} enviado com sucesso!!!")
            # Espera um pouco para evitar problemas no envio repetido
            time.sleep(0.5)