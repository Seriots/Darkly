# B10-PasswordFileAccessible-Admin

## BREACH

PATH `http://192.168.56.110/admin/`

For this vulnerability, we start by displaying the `robots.txt` file, which is a common file on websites and provides interesting information.

```
User-agent: *
Disallow: /whatever
Disallow: /.hidden
```

We can see a path `/whatever` that contains a file `htpasswd`.

```
Index of /whatever/
../
htpasswd           29-Jun-2021 18:09        38
```

The `htpasswd` file contains something resembling a login:password pair.

```
root:437394baff5aa33daa618be47b75cb49
```

Using `dirb` to scan our site, we see that there is an `admin` page.

We assume that the password is encrypted, so we decrypt it (MD5), log in with `root:qwerty123@`, and obtain the flag.

> https://md5decrypt.net/

## PATCH

To patch, simply do not leave passwords accessible to users, use stronger encryption methods, use a more complex password, or allow access to the admin page only from certain IPs.