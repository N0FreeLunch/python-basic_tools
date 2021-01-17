
## findall
```
  import re
  example = '이동민 교수님은 다음과 같이 설명했습니다(이동민, 2019). 그런데 다른 교수님은 이 문제에 대해서 다른 견해를 가지고 있었습니다.(최재영, 2019). 또 다른 견해도 있었습니다(Lion, 2018)'

  result = re.findall(r'\([A-Za-z가-힣]+, \d+\)', example)
  result
```

## re.match
```
  pattern = r'life.'
  script = 'life1life2life3'
  re.match(pattern, script)
  re.match(pattern, script).group()
```

## one line expression
```
  re.match(r'life.', 'life1life2life3').group()
```

## no matching
```
  re.match(r'life', 'animal').group()
```
error
> AttributeError: 'NoneType' object has no attribute 'group'

## match function
```
  def refinder(pattern, script):
    if re.match(pattern, script):
      print('Match!');
    else:
      print('Not a match')
```
press enter enter


## use refinder (matched)
```
  pattern = r'Life'
  script = 'Life is so cool'
  refinder(pattern, script)
```

## use refinder (not matched)
```
  pattern = r'life'
  script = 'Life is so cool'
  refinder(pattern, script)
```


## can't find middle spell using re.match
```
  pattern = r'is'
  script = 'Life is so cool'
  refinder(pattern, script)
```
> Not a match

## re.search
```
  pattern = r'is'
  script = 'Life is so cool'
  re.search(pattern, script).group()
```

## assigned match express on argument
```
  re.search(r'Life', script).group()
  re.search(r'cool', script).group()
```

## when using re.match
error
```
  re.match(r'cool', script).group()
```

```
  re.match(r'Life', script).group()
```


express | description
------- | -----------
\d | 숫자와 매치, [0-9]와 동일한 표현식이다.
\D | 숫자가 아닌 것과 매치, [^0-9]와 동일한 표현식이다.
\s | whitespace 문자와 매치, [ \t\n\r\f\v]와 동일한 표현식이다. 맨 앞의 빈 칸은 공백문자(space)를 의미한다.
\S | whitespace 문자가 아닌 것과 매치, [^ \t\n\r\f\v]와 동일한 표현식이다.
\w | 문자+숫자(alphanumeric)와 매치, [a-zA-Z0-9_]와 동일한 표현식이다.
\W | 문자+숫자(alphanumeric)가 아닌 문자와 매치, [^a-zA-Z0-9_]와 동일한 표현식이다.


## \\\\ expression
```
  re.match(r'Life..', 'Life\d is so cool').group()
  re.match(r'Life\\d', 'Life\d is so cool').group()
```

## pattern without r
```
  re.match(r'Life\\d', 'Life\d is so cool').group()
  re.match('Life\\\d', 'Life\d is so cool').group()
```
error
```
  re.match('Life\\d', 'Life\d is so cool').group()
```

pattern without r : Life\\d <- string (code expression)
= pattern with r : Life\d <- raw string (result value)

error
```
  re.match(r'Life\d', 'Life\d is so cool').group()
```

## re.findall
```
  number = 'My number is 511223-1****** and yours is 521012-2******'
  re.findall('\d{6}', number)
```

## \. expression
```
  example1 = '저는 91년에 태어났습니다. 97년에는 IMF가 있었습니다. 지금은 2020년입니다.'
  re.findall(r'\d.+년', example1)
```


## \? expression
```
  re.match(r'Life\s?', 'Life is so cool').group()
  re.match(r'Life\s?', 'Life-is so cool').group()
  re.match(r'L?ife', 'Life is so cool').group()
  re.match(r'L?ife', 'ife is so cool').group()
```

## greed
```
  re.findall(r'\d.+?년', example1)
  re.search(r'\d.+?년', example1)
  re.findall(r'\d+.년', example1)
```

## greed
```
  example = '이동민 교수님은 다음과 같이 설명했습니다(이동민, 2019). 그런데 다른 교수님은 이 문제에 대해서 다른 견해를 가지고 있었습니다.(최재영, 2019). 또 다른 견해도 있었습니다(Lion, 2018)'

  result = re.findall(r'\(.+\)', example)
  result
```


## no greed
```
  result = re.findall(r'\(.+?\)', example)
  result
```


## split
```
  centence = 'I have a lovely dog, really. I am not telling a lie. What a pretty dog! I love this dog.'
  re.split(r'[.?!]', centence)
```


## split return array
```
  data='a:3; b:4; c:5'
  re.split(r';', data)
  for i in re.split(r';', data):
    print(re.split(r':',i))
```
