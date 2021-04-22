from player import Player
from weapon import Weapon
#class Player:

    #pseudo = "Dragfy"
    #health = 50
    #attack = 5


#player1 = Player()
#print("Bienvenue au joueur", player1.pseudo)

#class Player:
    #constructeur
   # def __init__(self, pseudo, health, attack):
       # self.pseudo = pseudo
       # self.health = health
       # self.attack = attack
       # print("Bienvenue au joueur", pseudo, " / Points de vie: ", health, " / Attaque: ", attack)


#player1 = Player("DD", 50, 5)

#player2 = Player("EE", 50, 5)

knife = Weapon("Couteau", 3)


player1 = Player("DD", 50, 5)

player1.set_weapon(knife)

player2 = Player("EE", 50, 5)

player1.attackplayer(player2)
print(player1.get_pseudo(), 'attaque', player2.get_pseudo())
print("Bienvenue au joueur", player1.get_pseudo(), " / Points de vie: ", player1.get_health(), " / Attaque: ", player1.get_attack())
print("Bienvenue au joueur", player2.get_pseudo(), " / Points de vie: ", player2.get_health(), " / Attaque: ", player2.get_attack())