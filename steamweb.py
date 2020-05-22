from steam.webapi import WebAPI
from csv import DictReader


def find_steamid(userid):
    with open('database.csv', 'r') as db:
        dados = DictReader(f=db)
        for linha in dados:
            if linha['userid'] == str(userid):
                steamid = linha['steamid']
                return steamid


def meulevel(steamid=None):
    api = WebAPI(key='C20F32188B2E214DB83F1A3626E34889')

    level = api.IPlayerService.GetSteamLevel(steamid=steamid)
    level = level['response']['player_level']

    return level


def meusjogos(steamid=None):
    api = WebAPI(key='C20F32188B2E214DB83F1A3626E34889')

    jogos = '\U00002B07 Sua lista de jogos \U00002B07\n\n'

    lista = api.IPlayerService.GetOwnedGames(steamid=steamid, include_appinfo=True,
                                             include_played_free_games=False, appids_filter=False,
                                             include_free_sub=False)

    for jogo in lista['response']['games']:
        jogos += f'\U0001F535 <strong>{jogo["name"]}</strong>\n' \
                 f'     {round(jogo["playtime_forever"]/60)} horas jogadas\n\n'

    return jogos


if __name__ == '__main__':
    print(meusjogos(76561198067139679))
