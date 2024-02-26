# B10-LocalFileInclusion-pageQuery

## BREACH

PATH `http://192.168.55.3/?page=../../../../../../../etc/passwd`

To navigate, the website uses the `page` query parameter, which takes the value of the page to be displayed.

However, if protections are not in place, it means that anyone can theoretically navigate through the machine using this method.

By adding `../` in the query parameter, one can traverse up the directory tree to exit the site.

To test if a Local File Inclusion (LFI) is possible, we try to display `/etc/passwd`.

With our small script, we attempt to traverse the directory structure gradually to reach the root and access `/etc/passwd`.

By traversing sufficiently, we succeed and obtain a flag.


```
<script>alert('Congratulaton!! The flag is : b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0 ');</script>
```

## PATCH

To patch this, one approach is to isolate the machine in a completely isolated environment, preventing attackers from gaining access to the entire machine. Another approach is to filter the value of the query parameter to remove anything we want to forbid, such as `../`.
