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

On suppose que le mot de passe est encrypter donc on le decrypt (MD5), on se connecte `root:qwerty123@`, et on obtient le flag.

> https://md5decrypt.net/

# PATCH

Pour patcher tout simplement ne pas laisser trainer des mot de passes accessible aux utilisateurs, utiliser des methodes d'encryption plus fortes, utiliser un mot de passe plus complexe ou encore autoriser la connection a la page admin uniquement depuis certaines IP.