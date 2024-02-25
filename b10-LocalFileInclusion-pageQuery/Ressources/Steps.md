# B10-LocalFileInclusion-pageQuery

## BREACH

PATH `http://192.168.55.3/?page=../../../../../../../etc/passwd`

Pour naviguer, le site web utilise la `query` page qui prend comme valeur la page qui veux etre affichee.

Cependant si des protections ne sont pas mit en place cela veux dire que n'importe qui peux theoriquement se balader dans la machine garce a cela.

En mettant des `../` dans la query on peux reculer des l'arbre de dossier pour sortir du site.

Pour tester si une `LFI(Local File Inclusion)` est possible on essaye d'afficher `/etc/passwd`.

Avec notre petit script on test de reculer au fur et a mesure dans la machine pour tomber a la racine et aller chercher `/etc/passwd`.

En reculant suffisament on y arrive et on obtient un flag.

```
<script>alert('Congratulaton!! The flag is : b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0 ');</script>
```

## PATCH

Pour patcher cela on peux isoler la machine dans un environnement completement isoler, cela empechera aux attaquants d'avoir acces a toutes la machine. On peux aussi filtrer la valeur de la query pour retirer tous ce qu'on veux interdire comme les `../` par exemple.
