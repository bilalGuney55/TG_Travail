 # ex 2

velib = {"id":1210, "typ":"electrique", "station": "place d'Italie","statut":"en panne"}
velib["statut"] = "disponible"


#ex 2(bis)

velo1 = {"id":59 , "typ":"classique" , "station":"champs élysées" , "statut": "dispo"}
velo2 = {"id":494 , "typ": "electrique" , "station": "châtelet" , "statut": "dispo"}
velo3 = {"id":767 , "typ": "electrique", "station":"arc de triomphe" , "statut": "en panne"}

parc_velib = []
parc_velib.append(velo1)
parc_velib.append(velo2)
parc_velib.append(velo3)


def recherche_velo(parc_velib):
    for velo in parc_velib:
        if velo["statut"] == "dispo":
            return True
    return False


def recherche_velo_v2(parc_velib):
    for velo in parc_velib:
        if velo["statut"] == "dispo":
            return velo["station"]
    return None


# ex 3


positions = {}
positions[(48.853585, 2.301490)] = "Paris"
positions[(11.611358, 43.147752)] = "Djibouti"
positions[(37.023113, -8.996601)] = "Fortaleza de Sao Vicente"
positions[(7.677989,-5.025387)] = "Bouaké"


def loc_photo(positions)