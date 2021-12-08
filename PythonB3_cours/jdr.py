class Personnage:
    nom = "DEFAULT"
    attaque = 20
    pdv = 200
    defense = 10
    catchphrase = "ATTRAPE LA PHRASE"

    def __init__(self, nom, attaque, pdv, defense, catchphrase):
        self.nom = nom
        self.attaque = attaque
        self.pdv = pdv
        self.defense = defense
        self.catchphrase = catchphrase

    def attaquer(self, personnage):
        if isinstance(personnage, Personnage):
            personnage.pdv -= self.attaque - self.defense
            print(f"ATTAQUE, boum : -{self.attaque} à {personnage.nom}")

    def sePresenter(self, personnage):
        if isinstance(personnage, Personnage):
            print(f"BONJOUR, je suis : {self.nom}")
            print(f"{self.catchphrase}")


class Guerrier(Personnage):
    def __init__(self, nom, attaque, pdv, defense, catchphrase):
        super().__init__(nom, attaque, pdv, defense, catchphrase)
        print("init guerrier")

    def criDeGuerre(self):
        print("CRIS DE GUERRE AHHHH !")
        print(str.upper(self.catchphrase))


class Clerc(Personnage):
    def __init__(self, nom, attaque, pdv, defense, catchphrase):
        super().__init__(nom, attaque, pdv, defense, catchphrase)
        print("init Clerc")

    def seSoigner(self):
        self.pdv = 200


class Paladin(Guerrier, Clerc):
    def __init__(self, nom, attaque, pdv, defense, catchphrase):
        super().__init__(nom, attaque, pdv, defense, catchphrase)
        print("init Paladin")


class Archer(Guerrier):
    def __init__(self, nom, attaque, pdv, defense, catchphrase):
        super().__init__(nom, attaque, pdv, defense, catchphrase)
        print("init Archer")

    def tirer(self, personnage):
        if isinstance(personnage, Personnage):
            personnage.pdv -= self.attaque * 2 - self.defense
            print(f"ATTAQUE, boum  (de loin) : -{self.attaque} à {personnage.nom}")


class Mage(Personnage):
    mana = 200

    def __init__(self, nom, attaque, pdv, defense, catchphrase):
        super().__init__(nom, attaque, pdv, defense, catchphrase)
        print("init Mage")

    def jeterUnSort(self, personnage):
        if isinstance(personnage, Personnage):
            if self.mana > 0:
                personnage.pdv -= self.attaque * 3 - self.defense
                print(f"ATTAQUE, boum  (de loin mais de la magie) : -{self.attaque} à {personnage.nom}")
                self.mana -= 50
            else:
                print(f"IL A PLUS DE MANA CHEH !")
