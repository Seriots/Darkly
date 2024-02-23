# B10-HiddenFolder

PATH `http://192.168.56.110/admin/`

Pour cette faille nous commencons par afficher le fichier `robots.txt` qui est un fichier courant sur les sites web et qui fournit des informations interressantes.

```
User-agent: *
Disallow: /whatever
Disallow: /.hidden
```

On peux y voir un path `/whatever` qui contient un fichier `htpasswd`

```
Index of /whatever/
../
htpasswd                                           29-Jun-2021 18:09                  38
```

le fichier `htpasswd` contient quelque chose ressemblant a un login:password

```
root:437394baff5aa33daa618be47b75cb49
```

En utilisant `dirb` pour scanner notre site, on voit au'il y a une page `admin`

On suppose que le mot de passe est encrypter donc on utilise john pour le decrypter, on se connecte, et on obtient le flag.


1. use "dirb" to scan the website and get all common file
2. You can see a file named "whatever/htpasswd"
3. Open it and see something like login:password
4. Decode password (md5encrypt)
5. Dirb show us also an admin page, go on it
6. Enter le password decrypted and the login and get your flag