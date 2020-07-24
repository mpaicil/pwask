# Python essentials

## Primer archivo python 

Escribir en un archivo llamado `hello.py`:

``` python
print('hello cloud world')
```

Para ejecutar:

```
> python3 hello.py
> hello cloud world
```

## Programación por procedimientos 

La programación por procedimiento es la generación ordenada de instrucciones a procesar por la pc.

```python
>>> i = 3
>>> j = i + 1
>>> i + j
7
```

## Variables

```python
>>> dog_name = 'spot'
>>> dog_name
'spot'

>>> dog_name = 'rex'
>>> dog_name
'rex'

>>> dog_name = 't-' + dog_name
>>> dog_name
't-rex'
```

Las variable en python son del tipo dinamica, esto quiere decir que se le puede reasignar valores de diferente tipo o clase:

```python
>>> big = 'large'
>>> big
'large'

>>> big = 1000*1000
>>> big
1000000

>>> big = {}
>>> big
{}
```

## Operaciones Matemáticas básicas

```python
>>> 1 + 1
2

>>> 3 - 4
–1

>>> 2*5
10

>>> 2/3
0.6666666666666666
```

Ahora unas operaciones especiales, por ejemplo usar `//` nos brindará la parte entera de la división solamente, `**` nos permite calcular el valor exponencial y `%` nos permite calcular el módulo.

```python
>>> 5/2
2.5

>>> 5//2
2

>>> 3**2
9

>>> 5%2
1
```

## Comentarios

Simples

```python 
 # This is a comment
 1 + 1 # This comment follows a statement
 ```

Multilinea

```python
"""
This statement is a block comment.
It can run for multiple lines
"""

'''
This statement is also a block comment
'''
```

## Funciones integradas

Existen dos funciones integradas que son bastantes usadas, `print` y `range`

```python
>>> range(10)
range(0, 10)

>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> list(range(5, 10))
[5, 6, 7, 8, 9]

>>> list(range(5, 10, 3))
[5, 8]

>>> mylist = list(range(5))
>>> print(*mylist)
0 1 2 3 4
```

## Control de flujo

### `if/elif/else`

```python
>>> i = 45
>>> if i == 45:
...     print('i is 45')
...
...
i is 45
```

```python
>>> i = 35
>>> if i == 45:
...     print('i is 45')
... elif i == 35:
...     print('i is 35')
...
...
i is 35
```

```python
>>> i = 0
>>> if i == 45:
...     print('i is 45')
... elif i == 35:
...     print('i is 35')
... elif i > 10:
...     print('i is greater than 10')
... elif i%3 == 0:
...     print('i is a multiple of 3')
... else:
...     print("I don't know much about i...")
...
...
i is a multiple of 3

```

```python
>>> cat = 'spot'
>>> if 's' in cat:
...     print("Found an 's' in a cat")
...     if cat == 'Sheba':
...         print("I found Sheba")
...     else:
...         print("Some other cat")
... else:
...     print(" a cat without 's'")
...
...
Found an 's' in a cat
Some other cat

```

## Ciclos `for`

```python
>>> for i in range(10):
...     x = i*2
...     print(x)
...
...
0
2
4
6
8
10
12
14
16
18
```

## `continue`

```python
>>> for i in range(6):
...     if i == 3:
...         continue
...     print(i)
...
...
0
1
2
4
5
```

## Ciclos `while`

```python
>>> count = 0
>>> while count < 3:
...     print(f"The count is {count}")
...     count += 1
...
...
The count is 0
The count is 1
The count is 2
>>>
```