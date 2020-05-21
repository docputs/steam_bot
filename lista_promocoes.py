import requests
from bs4 import BeautifulSoup


def dividir_preco(precos):
    precos = precos.split('R$')

    preco1 = precos[1].strip()
    preco2 = precos[2].strip()

    return preco1, preco2


def extrair_promocoes():
    r = requests.get('https://store.steampowered.com/search/?specials=1').text
    soup = BeautifulSoup(r, 'lxml')

    jogos = soup.find('div', id='search_resultsRows')

    lista = ''

    for jogo in jogos.find_all('a'):

        nome = jogo.find('div', class_='col search_name ellipsis').span.text

        desconto = jogo.find('div', class_='col search_price_discount_combined responsive_secondrow')

        try:
            percentual = desconto.div.text[2:5]
            precos = desconto.find('div', class_='col search_price discounted responsive_secondrow').text
        except Exception as e:
            pass

        preco_inicio, preco_fim = dividir_preco(precos)

        lista += f'<strong>{nome}</strong>\n     {percentual} de desconto\n     de R${preco_inicio} por R${preco_fim}\n\n'

    return lista


if __name__ == '__main__':
    print(extrair_promocoes())