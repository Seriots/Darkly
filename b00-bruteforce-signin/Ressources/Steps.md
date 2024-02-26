# B00-BruteForce

## BREACH
PATH `http://192.168.55.3/?page=signin&username={}&password={}&Login=Login#`

For this vulnerability, we have a login page asking for a `username` and a `password`, which are then passed as query arguments to make a request to the backend.

We can assume that there are default users such as admin or root.

So, we can try to brute-force the password using a list of common passwords like `rockyou.txt`.

We write a small script and wait.

The script finds the password after 20 seconds, and we can log in with `admin:shadow`.

## PATCH

There are various ways to prevent a brute-force attack, but the main idea is always the same: prevent the attacker from making thousands of requests per second. To do this, we can simply block the IP of a user who enters incorrect passwords repeatedly for a certain duration, or prevent automation of login attempts with CAPTCHAs.