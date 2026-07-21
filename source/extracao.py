from playwright.sync_api import sync_playwright
from pathlib import Path

index_html = INDEX_HTML = Path(r"C:\\Users\\Turma02\\Git\\HyperAutomationPortalFake\\portal_fake\\index.html")
url = "file:///" + str(index_html).replace("\\", "/")


def extrair_dados():

    with sync_playwright() as p:

        navegador = p.chromium.launch(headless=False)

        pagina = navegador.new_page()

        # Abrir Portal Fake
        pagina.goto(url)

        # Clicar no botão Novo Cadastro
        pagina.click("#btnNovo")

        # Esperar a tela de cadastro carregar
        pagina.wait_for_timeout(1000)

        pagina.screenshot(path='tela_cadastro.png')
        print('Screenshot da tela de cadastro salvo.')

        # Extrair dados dos campos
        dados = { "Nome": pagina.locator("#f_nome").input_value(), "Sobrenome": pagina.locator("#f_sobrenome").input_value(), "CPF": pagina.locator("#f_cpf").input_value(), "E-mail": pagina.locator("#f_email").input_value(), "Telefone": pagina.locator("#f_telefone").input_value(), "Nascimento": pagina.locator("#f_nascimento").input_value(), "Endereco": pagina.locator("#f_endereco").input_value()
        }

        print("Dados extraídos:")
        for campo, valor in dados.items():
            print(f"{campo}: {valor}")

        navegador.close()

if __name__ == "__main__":
    extrair_dados()