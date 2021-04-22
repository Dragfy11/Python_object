class Player:
    #constructeur
    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.weapon = None
        print("Bienvenue au joueur", pseudo, " / Points de vie: ", health, " / Attaque: ", attack)
# methode

    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack
#dégat

    def domage(self, damage):
        self.health -= damage
# attaquer un joueur

    def attackplayer(self, target_player):
        damage = self.attack

        #si le joueur a une arme
        if self.has_weapon():
            #ajout les dégàts de l'arme au point d'attaque du joueur
            damage += self.weapon.get_damage_amount()
        
        target_player.damage(damage)
