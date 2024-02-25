# B00-BruteForce

## BREACH
PATH `http://192.168.55.3/?page=signin&username={}&password={}&Login=Login#`

Pour cette faille nous avons une page de connection demandant un `username` et un `password` qui sont ensuite passer en `query arguments` pour faire une requete au backend.

Nous pouvons supposer qu'il doit y avoir des users par defaults tels que admin ou root

Nous pouvons donc essayer de bruteforce le mot de passe avec une liste des mots de passes les plus commun on prend `rockyou.txt`

On ecrit un petit script et on attend.

Le script nous trouve le mot de passe au bout de 20sec et nous pouvons nous connecter avec `admin:shadow`

## PATCH

Il y a diverses manieres d'empecher une attaque bruteforce mais l'idee principale est toujours la meme, empecher
l'attaquant de faire des milliers de requetes a la secondes. Pour cela on peux simplement bloquer l'IP d'un utilisateurs mettant des mot de passes faux en boucle pour une certaine duree, ou faire en sorte d'empecher une automatisations de la connections avec des CAPTCHAs. 