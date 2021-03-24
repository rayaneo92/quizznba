

# QUESTIONS
NBA = [ " Quelle est l''équipe a gagné le plus de titres NBA ? " ]
NBA1 = [" Qui est le meilleur scoreur de la ligue ? (ALL TIME)  " ]
NBA2 = [" Quel joueur a marqué 100 points en un seul match ? "]

rp1 = [" 1 :Boston Celtics " ]
rp2 =[" 1 : Micheal Jordan " ]
rp444 = ["1 : Wilt Chamberlain "]

rp11 = [" 2 : L.A Lakers " ]
rp111 = [" 2 : Kobe Bryant"  ]
rp4444 = [" 2 : Kyrie Irving"]

rp3 = [" 3 : Brooklyn Nets " ]
rp33 = [" 3  : Kareem Abdul Jabbar" ]
rp555 = ["3 : Kevin Durant"]


# QUESTION 2

print(NBA)
print(rp1)
print(rp11)
print(rp3)

rep= int(input ("Entrez LA bonne réponse :  " ))
rpcorrecte = 2

if rep != rpcorrecte:
    print("FAUX")
else :
    print("Bien")

# QUESTION 2

print(NBA1)
print(rp2)
print(rp111)
print(rp33)

rep= int(input ("Entrez LA bonne réponse :  " ))
rpcorrecte = 3

if rep != rpcorrecte:
    print("FAUX")
else :
    print("Bien")


# QUESTION 3

print(NBA2)
print(rp444)
print(rp4444)
print(rp555)

reputilisateur = int(input ("Entrez LA bonne réponse :  " ))
rpcorrecte = 1


if reputilisateur != rpcorrecte:
    print("FAUX")
else :
    print("Bien")