# b06-RecoverPassword

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

```
<input type="hidden" name="mail" value="lgiband@student.42.fr" maxlength="15">
```

On test en clickant sur submit et on obtient le flag.

```
THE FLAG IS : 1D4855F7337C0C14B6F44946872C4EB33853F40B2D54393FBE94F49F1E19BBB0
```