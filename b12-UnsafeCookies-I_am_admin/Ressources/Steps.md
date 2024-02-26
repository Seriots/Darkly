# B12-UnsafeCookie-I_am_admin

## BREACH

En inspectant nos cookies sur le site nous pouvons voir un cookie nomme `I_am_admin`.

En le decryptant (MD5) on peux voir qu'il vaux `false`.

On peux alors le remplacer par le `hash MD5` de `true` soit `b326b5062b2f0e69046810717534cb09` via la page internet.

On obtient alors un flag.

## PATCH

On me peux pqs faire confiance au frontend. Les cookies peuvent etre modifie a volonte par l'utilisateurs donc des donnees importantes comme la connection d'un admin ne peuvent pas etre stocker comme ca.

A la place on encoder des donnees avec des hash plus complexe en mettant des data seulement connus du backend permettant une double verification de l'utilisateur.