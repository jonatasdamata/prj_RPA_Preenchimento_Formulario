# 🕷️ Automação Selenium – Desafio de Formulário  
Projeto feito para automatizar um formulário usando **Selenium**, leitura de arquivos **JSON**, orientação a objetos e uma estrutura de projeto limpa e escalável.

---

## 📌 Sobre o Projeto
Este bot acessa um site de desafio de Web Scraping, lê vários perfis de usuários a partir de um arquivo JSON e preenche automaticamente o formulário para cada um deles.

O foco principal é:

- ✔️ boas práticas de código  
- ✔️ organização em classes  
- ✔️ automação realista com Selenium  
- ✔️ projeto fácil de manter  

---

## 📁 Estrutura do Projeto

```text
projeto/
│
├── main.py                      # Arquivo principal que executa a automação
│
├── classes/                     # Classes organizadas por responsabilidade
│   └── site/
│       └── pagina_scraper.py    # Classe responsável pela automação da página
│
├── Json/                        # Onde ficam os dados usados na automação
│   └── desafio_1.json
│
└── README.md                    # Documentação do projeto
```

## 🚀 Como Rodar o Projeto

### 1 - Garanta que o ChromeDriver está funcionando  
O Selenium já utiliza o ChromeDriver automaticamente em versões recentes, mas você precisa ter o **Google Chrome instalado** na máquina.

### 2 - Execute o bot  
```bash
python main.py
```

## 🧠 Tecnologias Usadas

- Python 3  
- Selenium WebDriver  
- JSON  
- Orientação a Objetos  


---

## ✨ Autor

**Jonatas da Mata Oliveira**  
Desenvolvedor Python | RPA | Automação  

---


