import httpx
from bs4 import BeautifulSoup

# Passo 1: Capturar o HTML da página principal
url = 'https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000596481-Linha-Winthor/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36',
}

with httpx.Client(headers=headers) as client:
    # Primeiro request para obter cookies
    client.get('https://centraldeatendimento.totvs.com/')
    
    # Segundo request com cookies para obter o conteúdo da página principal
    response = client.get(url)
    html_content = response.text

# Salvar o HTML completo em um arquivo para inspeção
output_file = '../data/files/whinthor_documentation.html'
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(html_content)

print(f'HTML content saved to {output_file}')

# Passo 2: Parsear o HTML para encontrar o link do "0 - Framework"
soup = BeautifulSoup(html_content, 'html.parser')
framework_link = soup.find('a', {'title': '0 - Framework'})['href']

# Construir a URL completa para o link do "0 - Framework"
framework_url = f'https://centraldeatendimento.totvs.com{framework_link}'

# Passo 3: Acessar o link do "0 - Framework" e capturar o HTML
with httpx.Client(headers=headers) as client:
    response = client.get(framework_url)
    framework_html_content = response.text

# Salvar o HTML do "0 - Framework" em um arquivo
framework_output_file = '../data/files/framework_documentation.html'
with open(framework_output_file, 'w', encoding='utf-8') as file:
    file.write(framework_html_content)

print(f'Framework HTML content saved to {framework_output_file}')
