| rank | ▲ | ✰ | vote | url |
|:-:|:-:|:-:|:-:|:-:|
|  75 | 343 | 88 | 324 | [url](http://stackoverflow.com/questions/1952464/in-python-how-do-i-determine-if-an-object-is-iterable) |

***

## 在Python中如何直达搜一个对象是可迭代的?

有没有一个`isiterable`的方法?我找到的解决方法:

```python
hasattr(myObj, '__iter__')
```

但是我不知道这是不是最好的.

***

### 鸭子类型

```python
try:
    iterator = iter(theElement)
except TypeError:
    # not iterable
else:
    # iterable

# for obj in iterator:
#     pass
```

### 类型检查

用[抽象基类](http://docs.python.org/library/abc.html).至少Python2.6以上而且只针对新式类.

```python
import collections

if isinstance(theElement, collections.Iterable):
    # iterable
else:
    # not iterable
```
