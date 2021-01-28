## call file
```
  import csv, os
  f = open('a.csv','r')
  f
```

## call file (for utf8)
```
  f = open('a.csv', 'r', encoding="utf-8")
```


## read file
```
  new = csv.reader(f)
  new
```
> <_csv.reader object at 0x7f3519026350>

## print csv data
```
  for i in new:
      print(i)
```

## convert csv obj to list
```
  a_list = []
  for i in new:
    print(i)
    a_list.append(i)
```
(enter)
```
  a_list
```


## make opencsv function
```
  def opencsv(filename):
    f = open(filename, 'r')
    reader = csv.reader(f)
    output = []
    for i in reader:
      output.append(i)
    return output
```


## read example2.csv
```
  opencsv('example2.csv')
```

## write csv
```
  a = [['구', ' 전체', ' 내국인', ' 외국인'], ['관악구', ' 519864', ' 502089', ' 1775'], ['강남구', ' 547602', ' 542498', ' 5104'], ['송파구', ' 686181', ' 679247', ' 6934'], ['강동구', ' 428547', ' 424235', ' 4312']]
  f = open('abc.csv', 'w', newline = '')
  csvobject = csv.writer(f, delimiter = ',')
  csvobject.writerows(a)
  f.close()
```

## writecsv function, use with instead of f.open and f.close
```
  def writecsv(filename, the_list):
    with open(filename, 'w', newline = '') as f:
      a = csv.writer(f, delimiter = ',')
      a.writerows(the_list)
```

##
```
  writecsv('abc1.csv', a)

```


##
```
  import os, usecsv
  import numpy as np
  quest = np.array(usecsv.switch(usecsv.opencsv('quest.csv')))
  quest
```
