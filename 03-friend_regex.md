## open file
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

## get names
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


## set
```
  a = [1,2,3,4,5,2,2]
  set(a)
  set(re.findall(char, script101))
```


## remove colon using sub
```
  rachel = 'Rache:'
  rachel = re.sub(':', '', rachel)
```


##  remove colon using slicing
```
  rachel[:-1]
```


## remove colon
```
  y = set(re.findall(char,  script101))
  z = list(y)
  character = []
  for i in z:
    character += [i[:-1]]
```


## List comprehension
```
  rawNames = list(set(re.findall(r'[A-Z][a-z]+:', script101)))
  rawNames
  character = [x[:-1] for x in rawNames]
```


## get discription
```
  re.findall(r'\([A-Za-z].+[a-z|\.]\)', script101)[:6]
```

## test getting discription regexp
```
  test = "(They all stare, bemused.) (adwdkald.)     (adjwdioa)"
  re.findall(r'\([A-Za-z].+[a-z|\.]\)', test)[:6]
```


## seek
```
  import os, re
  os.chdir(r'./')
  f = open('friends101.txt', 'r')
  f.read(100)
  f.read(100)
  f.seek(0)
  f.read(100)
```

## readlinesfirst
```
f.seek(0)
sentences = f.readlines()
sentences[:3]
```

## first line ~ 20th line without empty line
```
  f.seek(0)
  for i in sentences[:20]:
    if re.match(r'[A-Z][a-z]+:', i):
      print(i)
```

## List comprehension
```
  lines = [i for i in sentences if re.match(r'[A-Z][a-z]+:',i)]
  lines[:10]
```

## get sentence include 'world' word
```
  world = [i for i in sentences if re.match(r'[A-Z][a-z]+:', i) and re.search('world', i)]

  world
```

## get sentence include 'take' word
```
  take = [i for i in sentences if re.match(r'[A-Z][a-z]+:', i) and re.search('take', i)]

  take

  for i in take:
    print(i)
```

## save sentences include 'would' word
```
  would = [i for i in sentences if re.match(r'[A-Z][a-z]+:', i) and re.search('would', i)]

  newf = open('would.txt', 'w')
  newf.writelines(would)
  newf.close()
```
