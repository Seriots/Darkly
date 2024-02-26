# B10-Not-HiddenFolder

## BREACH
PATH `http://192.168.56.110/.hidden/`

For this vulnerability, we start by displaying the `robots.txt` file, which is a common file on websites and provides interesting information.


```
User-agent: *
Disallow: /whatever
Disallow: /.hidden
```

We can see a path `/.hidden` that contains a README and many folders with random names.


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

Looking at it, we see that each folder contains many other folders, and so on for the subsequent ones.

We understand that a `file` must contain a flag, so we write a small script that will recursively scrape the .hidden folder to retrieve all the `README` files and check if there is a flag inside.

> [Script](parse.py)

And by running it

```
➜  Darkly git:(main) ✗ python3 b10-hiddenfolder/Ressources/parse.py
http://192.168.56.110/.hidden/whtccjokayshttvxycsvykxcfm//igeemtxnvexvxezqwntmzjltkt//lmpanswobhwcozdqixbowvbrhw//README->Hey, here is your flag : d5eec3ec36cf80dce44a896f961c1831a05526ec215693c8f2c39543497d4466
```

## PATCH

Instead of trying to hide a folder, just prevent users from making requests to this route, making it truly inaccessible.
