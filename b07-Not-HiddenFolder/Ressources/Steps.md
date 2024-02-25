# B10-Not-HiddenFolder

## BREACH
PATH `http://192.168.56.110/.hidden/`

Pour cette faille nous commencons par afficher le fichier `robots.txt` qui est un fichier courant sur les sites web et qui fournit des informations interressantes.

```
User-agent: *
Disallow: /whatever
Disallow: /.hidden
```

On peux y voir un path `/.hidden` qui contient un README et plein de dossier avec des noms aleatoires

```
Index of /.hidden/
../
amcbevgondgcrloowluziypjdh/                        29-Jun-2021 18:15                   -
bnqupesbgvhbcwqhcuynjolwkm/                        29-Jun-2021 18:15                   -
ceicqljdddshxvnvdqzzjgddht/                        29-Jun-2021 18:15                   -
doxelitrqvhegnhlhrkdgfizgj/                        29-Jun-2021 18:15                   -
eipmnwhetmpbhiuesykfhxmyhr/                        29-Jun-2021 18:15                   -
ffpbexkomzbigheuwhbhbfzzrg/                        29-Jun-2021 18:15                   -
ghouhyooppsmaizbmjhtncsvfz/                        29-Jun-2021 18:15                   -
hwlayeghtcotqdigxuigvjufqn/                        29-Jun-2021 18:15                   -
isufpcgmngmrotmrjfjonpmkxu/                        29-Jun-2021 18:15                   -
jfiombdhvlwxrkmawgoruhbarp/                        29-Jun-2021 18:15                   -
kpibbgxjqnvrrcpczovjbvijmz/                        29-Jun-2021 18:15                   -
ldtafmsxvvydthtgflzhadiozs/                        29-Jun-2021 18:15                   -
mrucagbgcenowkjrlmmugvztuh/                        29-Jun-2021 18:15                   -
ntyrhxjbtndcpjevzurlekwsxt/                        29-Jun-2021 18:15                   -
oasstobmotwnezhscjjopenjxy/                        29-Jun-2021 18:15                   -
ppjxigqiakcrmqfhotnncfqnqg/                        29-Jun-2021 18:15                   -
qcwtnvtdfslnkvqvzhjsmsghfw/                        29-Jun-2021 18:15                   -
rlnoyduccpqxkvcfiqpdikfpvx/                        29-Jun-2021 18:15                   -
sdnfntbyirzllbpctnnoruyjjc/                        29-Jun-2021 18:15                   -
trwjgrgmfnzarxiiwvwalyvanm/                        29-Jun-2021 18:15                   -
urhkbrmupxbgdnntopklxskvom/                        29-Jun-2021 18:15                   -
viphietzoechsxwqacvpsodhaq/                        29-Jun-2021 18:15                   -
whtccjokayshttvxycsvykxcfm/                        29-Jun-2021 18:15                   -
xuwrcwjjrmndczfcrmwmhvkjnh/                        29-Jun-2021 18:15                   -
yjxemfsgdlkbvvtjiylhdoaqkn/                        29-Jun-2021 18:15                   -
zzfzjvjsupgzinctxeqtzzdzll/                        29-Jun-2021 18:15                   -
README                                             29-Jun-2021 18:15                  34
```

En regardant on voit que chaque dossier contiennent plein d'autres dossier et encore de meme pour les suivants

On comprend qu'un `fichier` doit contenir un flag donc on ecrit un petit script qui va scrap de maniere recursive le dossier .hidden pour recuperer tout les fichiers `README` et regarder si il y a un flag a l'interieur.

> [Script](parse.py)

Et en le lancant

```
➜  Darkly git:(main) ✗ python3 b10-hiddenfolder/Ressources/parse.py
http://192.168.56.110/.hidden/whtccjokayshttvxycsvykxcfm//igeemtxnvexvxezqwntmzjltkt//lmpanswobhwcozdqixbowvbrhw//README->Hey, here is your flag : d5eec3ec36cf80dce44a896f961c1831a05526ec215693c8f2c39543497d4466
```

## PATCH

Au lieu d'essayer de cacher un dossier, juste empeche a l'utilisateurs de faire des requetes sur cette route et comme ca il sera vraiment inaccessible.