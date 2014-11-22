| rank | ▲ | ✰ | vote | url |
|:-:|:-:|:-:|:-:|:-:|
|  36  |  511 | 136 | 405 | [url](http://stackoverflow.com/questions/1712227/how-to-get-the-size-of-a-list) |

***

## 在Python里怎么读取stdin?

我在做[code golf](http://en.wikipedia.org/wiki/Code_golf)挑战,但是所有的问题都需要读取stdin的值.在Python里应当怎么做?

***

这是我从 Stack Overflow 中学到的:

```python
import fileinput

for line in fileinput.input():
    pass
```

`fileinput`将会迭代在命令行参数给出的文件名的每一行,如果没有给参数,则默认为stdin.
