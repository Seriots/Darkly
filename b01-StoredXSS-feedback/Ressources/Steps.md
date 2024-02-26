# B01-StoredXSS-feedback

## BREACH

PATH `http://192.168.56.110/index.php?page=feedback`

For this breach we have a feedback field where we can perform some input with a `name` and a `message`.

to perform a XSS attack we try to send `JS code` to the input and check if he can be executed

Here we end this

```
<script>alert()</script>
```

We put this in the two field and we get the flag.

```
THE FLAG IS : 0FBB54BBF7D099713CA4BE297E1BC7DA0173D8B3C21C1811B916A3A86652724E
```

After some other test this flag is broke because if we just put a part of `alert` the flag is provided but the breach is here.

## PATCH

To patch XSS attack a conbination of thing is needed. First limit the damage of an XSS attack with disabling `HTTP TRACE` (debug) from everywhere. Also you need to filter the input and never interpret it as code but as string. You can encode input to prevent it from being interpreted directly or if not possible you can sanitize it and get just string.