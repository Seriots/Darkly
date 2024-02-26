# B08-UserAgentAndReferer-Albatroz

## BREACH

For this one, we have to click on the @BornToSec in the footer,

![image](https://github.com/Seriots/Darkly/assets/94530285/7aa978a8-b909-40c8-a2fa-085b902ebbe5)

We arrive on this page:

>`http://192.168.56.106/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f`

![image](https://github.com/Seriots/Darkly/assets/94530285/4a2a4016-f0d8-41b0-bca6-1694424e710b)

When we inspect the page we can find two informations,

![image](https://github.com/Seriots/Darkly/assets/94530285/f41e2b0a-4a35-4b75-a42c-013b8074e388)

![image](https://github.com/Seriots/Darkly/assets/94530285/e98f62d6-4eb2-4502-ae0a-c775521d9b51)

So we have to come from `https://www.nsa.gov/` and we have to use `ft_bornToSec`.

In web, the `previous page` is the `Referer` and the `used browser` is the `User-Agent`

So here we go on a virtual machine and use `BurpSuite` for `intercept` the `transmission` beetween the `home page` and ou `actual page`.

Doc here -> [BurpSuite](https://portswigger.net/burp/documentation/desktop/getting-started/intercepting-http-traffic)

![image](https://github.com/Seriots/Darkly/assets/94530285/03345f02-e51b-42fe-855a-e9aefb992be0)

So we have to change the User-Agent and the Referer,

![image](https://github.com/Seriots/Darkly/assets/94530285/839df6cf-f15e-408f-8d75-5bafc2a630cb)

And good job, we got the flag,

![image](https://github.com/Seriots/Darkly/assets/94530285/8ab1631a-2ed8-4560-bd08-13aebc6c8e89)



## PATCH

For prevent this exploit, you can ,

Use privacy protocols, TLS/SSL witch HTPPS server.

Do not use some variables of Header.

Don't allow the overwrite of Header.

https://owasp.org/www-chapter-ghana/assets/slides/HTTP_Header_Security.pdf

https://portswigger.net/web-security/host-header#how-to-prevent-http-host-header-attacks
