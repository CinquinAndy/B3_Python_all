import requests

# r = requests.get("https://hp-api.herokuapp.com/")
r_gryf = requests.get("https://hp-api.herokuapp.com/api/characters/house/gryffindor")
r_slyt = requests.get("https://hp-api.herokuapp.com/api/characters/house/slytherin")
r_huffle = requests.get("https://hp-api.herokuapp.com/api/characters/house/hufflepuff")
r_ravenclaw = requests.get("https://hp-api.herokuapp.com/api/characters/house/ravenclaw")

# name
# dateOfBirth
# wand


if r_gryf.status_code == 200:
    house = []
    result_gryffindor = r_gryf.json()
    result_slyt = r_slyt.json()
    result_huffle = r_huffle.json()
    result_ravenclaw = r_ravenclaw.json()
    house.append(result_gryffindor)
    house.append(result_slyt)
    house.append(result_huffle)
    house.append(result_ravenclaw)
    for hous in house:
        f = open(f"{hous[0]['house']}.txt", "a")
        for char in hous:
            if char['name'] != "":
                f.write(
                    f"name : {char['name']} ")
            if char['dateOfBirth'] != "":
                f.write(
                    f"| dateOfBirth : {char['dateOfBirth']} ")
            if char['wand']['wood'] != "" and char['wand']['core'] != "" and char['wand']['length'] != "":
                f.write(
                    f"| baguette: ")
                if char['wand']['wood'] != "":
                    f.write(
                        f"[materiel : {char['wand']['wood']} ")
                if char['wand']['core'] != "":
                    f.write(
                        f"| coeur : {char['wand']['core']} ")
                if char['wand']['length'] != "":
                    f.write(
                        f"| longueur : {char['wand']['length']}]")
            f.write("\n")
        f.close()
