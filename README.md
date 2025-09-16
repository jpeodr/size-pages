## Tecnologias utilizadas

- Python 3.10 ou superior
- [Selenium](https://www.selenium.dev/)
- [Matplotlib](https://matplotlib.org/)
- [chromedriver-autoinstaller](https://pypi.org/project/chromedriver-autoinstaller/)

---

## Instalação

```bash
# 1. Clone o repositório
git clone https://github.com/jpeodr/size-pages.git
cd size-pages

# 2. (Opcional) Crie e ative um ambiente virtual
python -m venv venv
# No Windows
venv\Scripts\activate
# No Linux/macOS
source venv/bin/activate

# 3. Instale as dependências
pip install -r requirements.txt
```
## Utilização

- No momento, é necessário inserir as URLs dos sites no código na **linha 11**, exemplo abaixo:

```bash
websites = [
      "https://https://developer.hashicorp.com/terraform",
      "https://www.google.com",
      "https://https://www.cisco.com/"
  ]
```

- Execute o script com o comando:
  ```bash
  python app.py
  ```
