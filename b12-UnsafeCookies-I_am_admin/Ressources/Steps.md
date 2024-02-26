# B12-UnsafeCookie-I_am_admin

## BREACH

Upon inspecting our cookies on the website, we can see a cookie named `I_am_admin`.

By decrypting it (MD5), we can see that its value is `false`.

We can then replace it with the MD5 hash of `true`, which is `b326b5062b2f0e69046810717534cb09`, via the webpage.

We then obtain a flag.

## PATCH

We cannot trust the frontend. Cookies can be modified at will by the user, so important data such as the admin's login status cannot be stored like this.

Instead, we encode data with more complex hashes, using data known only to the backend, allowing for double verification of the user.