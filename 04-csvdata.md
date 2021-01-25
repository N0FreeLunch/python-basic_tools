
### install python package
```
  pip install numpy
  pip install pandas
  pip install matlotlib
```

## module import
```
  import numpy as np
```

## array
```
  a = np.array([[2,3],[5,2]])
  a
```


## 2 dimension array
```
  d = np.array([[1,2,3,4,5], [2,4,5,6,7], [5,7,8,9,9]])
  d
```

## array divide
```
  d[1][2]
  d[1, 2]
  d[1:, 3:]
```

> [1, 2, 3,|4, 5]
> ---------|-----
> [2, 4, 5,|6, 7]
> [5, 7, 8,|9, 9]



## shape
metrix (NxM)
```
  d = np.array([2,3,4,5,6])
  d
  d.shape
  e = np.array([[1,2,3,4], [3,4,5,6]])
  e
  e.shape
```

## all type check
```
  d.dtype
```
> dtype('int64')

## convert all element type
```
  data = np.arange(1,5)
  data.dtype
  data.astype('float64')
  data.astype('int32')
```
#### ref.
int(32,64)
uint(32,64)
float(32,64)
complex
bool
string
object
unicode


## np.zeros
(NxM) all element value 0
```
  np.zeros((2, 10))
```

## np.ones
(NxM) all element value 1
```
  np.ones((2, 10))
```

## np.arange
> [2,3,4,....,9]
```
  np.arange(2, 10)
```

## np.ones
```
  a = np.ones((2,3))
```


## np.transpose
```
  a = np.ones((2,3))
  a
  b = np.transpose(a)
  b
```
> [1., 1., 1.]
> [1., 1., 1.]
> transpose
> [1., 1.]
> [1., 1.]
> [1., 1.]


## array multiplication
## array division

```
  arr1 = np.array([[2,3,4],[6,7,8]])
  arr2 = np.array([[12,23,14],[36,47,58]])
  arr1 * arr2
  arr1 / arr2
```


## array addition

```
arr3 = np.array([100,200,300])
```

```
  arr1.shape
  arr3.shape
  arr1 + arr3
```
[2, 3, 4]
[6, 7, 8]
+
[100, 200, 300]
=
[102, 203, 304]
[106, 207, 308]

----------------


[2, 3, 4]
[6, 7, 8]
+
[100, 200, 300]
[100, 200, 300]
=
[102, 203, 304]
[106, 207, 308]


## can't operate
```
  arr4 = np.array([1,2,3,4,5,6,7,9,10])
  arr4.shape
  arr1.shape
  arr1 + arr4
```


## check shape before operation
```
  arr5 = np.array([[9],[3]])
  arr5.shape
  arr1
  arr5 + arr1
```

## the difference python list and numpy array
```
d = np.array([[1,2,3,4,5],[2,4,5,6,7],[5,7,8,9,9]])
d_list = [
        [1,2,3,4,5],
        [2,4,5,6,7],
        [5,7,8,9,9]
      ]
d_list
```

##
```
  arr4 = np.arange(10)
  arr4.shape
  arr1.shape
  arr1 + arr4
```

```
  arr5 = np.array([[9],[3]])
  arr5.shape
  arr1
  arr5 + arr1
```
