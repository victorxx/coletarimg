from playwright.sync_api import sync_playwright
import time

try:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Acessa a página do Pinterest
        url = 'https://pt.pinterest.com/lucinhacarreiro33/memes-engra%C3%A7ados/'
        page.goto(url, timeout=60000)
        page.wait_for_load_state('networkidle')

        hrefs = []

        # Faz scroll para carregar mais imagens
        for _ in range(10):
            page.mouse.wheel(0, 10000)
            time.sleep(1)

        # Coleta todas as imagens visíveis na página
        imagens = page.locator('img')
        contagem = imagens.count()

        for i in range(contagem):
            src = imagens.nth(i).get_attribute('src')
            final=f'"{src}"'
            hrefs.append(f'"{final}"')


        resultado = ','.join(hrefs)
        print(resultado)

        browser.close()

except Exception as e:
    print('Erro:', e)
