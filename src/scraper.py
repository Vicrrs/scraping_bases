import httpx

url = 'https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000596481-Linha-Winthor/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36',
}

with httpx.Client(headers=headers) as client:
    # Primeiro request para obter cookies
    client.get('https://centraldeatendimento.totvs.com/')
    
    # Segundo request com cookies
    response = client.get(url)
    html_content = response.text

output_file = '../data/files/whinthor_documentation.html'
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(html_content)

print(f'HTML content saved to {output_file}')
