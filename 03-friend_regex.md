##open file
```
  import os, re, codecs
  path = os.getcwd()
```

## go to folder include friends101.txt file
```
os.chdir(path)
```

## load friends101.txt
```
  f = codecs.open('friends101.txt', 'r', encoding='utf-8')
  script101 = f.read()
```


## 1 letter ~ 100 letter
```
  print(script101[:0])
  print(script101[:1])
  print(script101[:2])
  print(script101[:3])
  print(script101[:100])
  print(type(script101[:100]))
  print(len(script101[:100]))
```

## string and list
```
  babo = "babo"
  print(type(babo))
  print(babo[0] + babo[1] + babo[2] + babo[3])
  print(len(babo))
```

## get monica message
```
  Line = re.findall(r'Monica:.+', script101)
  print(re.search(r'Monica:.+', script101))
  print(re.search(r'Monica:.+', script101).group())
  print(Line[:3])
```


## return type of re.findall

```
  print(type(Line[:3]))
  for item in Line[:3]:
    print(item)
```

## file close
```
  f.close()
```


## make file
```
  f = open('monica.txt', 'w', encoding = 'utf-8')
```

## set string to save to file
```
  monica = ''
  for i in Line:
    monica += i

```

(enter)

## make and write file
```
  f.write(monica)
  print(len(script101))
  f.close()
```

## check line number
```
  confirm = codecs.open('monica.txt', 'r', encoding='utf-8')
  print(len(confirm.read()))

```

## newline in linux. OSX
```
  monica = '';
  for i in Line:
    monica += i + '\n'
```

## save file newline applied in linux. OSX
```
  f = open('monica.txt', 'w', encoding = 'utf-8')
  f.write(monica)
  f.close()
```

## Carriage Return
```
  test = open('test.txt', 'w', encoding = 'utf-8')
  test.write('1\r2\r3\r4')
  test.close()
```

## Line Feed
```
  test = open('test.txt', 'w', encoding = 'utf-8')
  test.write('1\n2\n3\n4')
  test.close()
```

## get name
```
  char = r'[A-Z][a-z]+:'
  char = re.compile(r'[A-Z][a-z]+:')
  re.findall(char, script101)
```


## re.compile
```
  compiledChar = re.compile(r'[A-Z][a-z]+:')
  compiledChar.findall(script101)
```


##
```
  a = [1,2,3,4,5,2,2]
  set(a)
```
