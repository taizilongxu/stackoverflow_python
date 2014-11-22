| rank | ▲ | ✰ | vote | url |
|:-:|:-:|:-:|:-:|:-:|
| 4 | 1266 | 285 | 929 | [url](http://stackoverflow.com/questions/82831/check-if-a-file-exists-using-python) |

***

## 用Python如何一个文件是否存在?

不用`try:`语句可以一个文件存在

***

如果不确定文件存不存在,可以这样做:

```python
import os.path
os.path.isfile(fname)
```
