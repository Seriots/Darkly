# B11-RedirectWebsite

## BREACH

Go on the footer of home page for this one,

`http://192.168.56.106/`

and we have three social network logos,

![image](https://github.com/Seriots/Darkly/assets/94530285/eb397872-fa86-49e8-90cf-45266497f575)

we can see they are redict for the good social network,

![image](https://github.com/Seriots/Darkly/assets/94530285/f6bcc745-f4c5-44e2-80d7-bed3bf0ff434)

So let's try to use the `redirect` query string for exploit,

>`http://192.168.56.106/index.php?page=redirect&site=toto`

![image](https://github.com/Seriots/Darkly/assets/94530285/ad1d0886-269a-472b-8545-1e21f68fe3ce)

This one was easy, good job !


## PATCH

Furthermore, the use of redirection can also make the website vulnerable to phishing attacks,

where attackers can create fake pages that mimic the original page and steal user credentials.

It is important to ensure that the redirected page is legitimate and secure before redirecting users to it.

In terms of web safety, it is recommended to implement proper input validation and sanitization techniques to prevent injection attacks,

such as SQL injection or cross-site scripting (XSS). It is also important to keep the web server and software up-to-date with security patches and to use secure protocols,

such as HTTPS, to protect data in transit.

Regular security audits and testing can also help identify and address any vulnerabilities in the web application.

https://www.invicti.com/learn/unvalidated-redirects-and-forwards/
