write file
----------
make file a.txt
```
  f = open('a.txt', 'w')
  f.write('abc')
  f.close()
```

```
  f = open('a.txt', 'w')
  f.write('나는 오늘 학교에 간다')
  f.close()
```


double read
-----------
```
  f = open('a.txt', 'r')
  f.read()
  f.read()
  f.close()
```
> first f.read() result : 나는 오늘 학교에 간다
> second f.read() result : ''


read seek
---------
```
  f = open('a.txt', 'r')
  f.read()
  f.seek(0)
  f.close()
```



read not exist file
-------------------
```
  f = open('b.txt', 'r')
```
result

> Traceback (most recent call last):
>  File "<stdin>", line 1, in <module>
> FileNotFoundError: [Errno 2] No such file or directory: 'b.txt'


add more txt
------------
```
  f = open('a.txt', 'a')
  f.write('학교 가지 않을 날이 올까?')
  f.close()
```
check it
```
  f = open('a.txt', 'r')
  f.read()
  f.close()
```

not exist 'abcde.txt'
---------------------
```
  f = open('abcde.txt', 'w')
  f.write('I went to school today.')
  f.close()
```

use with
--------
:eyes: need indentation
```
  with open('text.txt', 'w') as f:
    f.write('오늘 나는 학교에 갔습니다.')
```
press enter


language codec
--------------
```
  import os, re
  os.chdir('./python_data')
  f = open('한글파일.txt', 'w')
  f.close()
  f=open('한글파일.txt', 'r')
  script1101=f.read()
```

if error do this. include language format
```
  import codecs
  f = codecs.open('한글파일.txt', 'r', 'utf-8')
  f.read()[:10]
```
