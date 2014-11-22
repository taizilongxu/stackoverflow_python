| rank | ▲ | ✰ | vote | url |
|:-:|:-:|:-:|:-:|:-:|
|  23  |  644 | 117 | 879 | [url](http://stackoverflow.com/questions/1024847/add-to-a-dictionary-in-python) |

***

## 字典里添加元素的方法

当一个字典被创建了,能不能在字典里计入一个键?好像没有`.add()`的方法.

***

```python
>>> d = {'key':'value'}
>>> print d
{'key': 'value'}
>>> d['mynewkey'] = 'mynewvalue'
>>> print d
{'mynewkey': 'mynewvalue', 'key': 'value'}
```

***

```python
>>> x = {1:2}
>>> print x
{1: 2}

>>> x.update({3:4})
>>> print x
{1: 2, 3: 4}
```
