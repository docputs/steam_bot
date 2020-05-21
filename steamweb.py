from steam.webapi import WebAPI


def meusjogos(user_id=None):
    api = WebAPI(key='C20F32188B2E214DB83F1A3626E34889')

    jogos = 'Sua lista de jogos:\n\n'

    level = api.IPlayerService.GetSteamLevel(steamid=user_id)
    recentes = api.IPlayerService.GetRecentlyPlayedGames(steamid=user_id, count=0)
    amigos = api.ISteamUser.GetFriendList(steamid=user_id)
    return amigos


if __name__ == '__main__':
    print(meusjogos(76561198067139679))
