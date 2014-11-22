| rank | ▲ | ✰ | vote | url |
|:-:|:-:|:-:|:-:|:-:|
|  57 | 386 | 107 | 665 | [url](http://stackoverflow.com/questions/510972/getting-the-class-name-of-an-instance-in-python) |

***

## 字典推导式

我喜欢列表推导式的语法.

它能不能用来创建字典?这样:

```python
mydict = {(k,v) for (k,v) in blah blah blah}  # doesn't work :(
```

***

在Python2.6或更早的版本,字典生成器可以接受迭代的键/值对:

```python
d = dict((key, value) for (key, value) in iterable)
```

从Python2.7或者3以后,你可以直接用[字典推导式语法](http://www.python.org/dev/peps/pep-0274/):

```python
d = {key: value for (key, value) in iterable}
```

当然,你可以用任何方式的迭代器(元组,列表,生成器..),只要可迭代对象的元素中有两个值.

```python
d = {value: foo(value) for value in sequence if bar(value)}

def key_value_gen(k):
   yield chr(k+65)
   yield chr((k+13)%26+65)
d = dict(map(key_value_gen, range(26)))
```
