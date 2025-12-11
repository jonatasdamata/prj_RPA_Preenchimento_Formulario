"""
Arquivo principal do projeto.

Responsável por iniciar o fluxo da automação:
1. Abrir o navegador
2. Executar o preenchimento do formulário no site
"""

from classes.site.pagina_scraper import PaginaScrapper


def main():
    """
    Função principal da aplicação.

    Executa as etapas principais:
    - Abre o navegador via classe PaginaScrapper
    - Preenche o formulário com os dados do JSON
    """
    PaginaScrapper.abrir_navegador()
    PaginaScrapper.preencher_formulario()


if __name__ == "__main__":
    main()
