

# QUESTIONS
NBA = [ " Quelle est l''équipe a gagné le plus de titres NBA ? " ]
NBA1 = [" Qui est le meilleur scoreur de la ligue ? (ALL TIME)  " ]
NBA2 = [" Quel joueur a marqué 100 points en un seul match ? "]
NBA3 = ["Dans quelle ville jouent les Golden State Warriors"]

rp1 = [" 1 :Boston Celtics " ]
rp2 =[" 1 : Micheal Jordan " ]
rp444 = ["1 : Wilt Chamberlain "]
rp6 = [" 1 : San Diego "]

rp11 = [" 2 : L.A Lakers " ]
rp111 = [" 2 : Kobe Bryant"  ]
rp4444 = [" 2 : Kyrie Irving"]
rp66 = [" 2 : Oakland "]

rp3 = [" 3 : Brooklyn Nets " ]
rp33 = [" 3  : Kareem Abdul Jabbar" ]
rp555 = ["3 : Kevin Durant"]
rp661 = ["3 : San José "]

# QUESTION 1

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

# QUESTION 4

print(NBA3)
print(rp6)
print(rp66)
print(rp661)

reputilisateur = int(input ("Entrez LA bonne réponse :  " ))
rpcorrecte = 2


if reputilisateur != rpcorrecte:
    print("FAUX")
else :
    print("Bien")
