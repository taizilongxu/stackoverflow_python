| rank | ▲ | ✰ | vote | url |
|:-:|:-:|:-:|:-:|:-:|
|  18  |  766 | 373 | 952 | [url](http://stackoverflow.com/questions/273192/check-if-a-directory-exists-and-create-it-if-necessary) |

***

## `if __name__ == "__main__":`是干嘛的?

```python
# Threading example
import time, thread

def myfunction(string, sleeptime, lock, *args):
    while 1:
        lock.acquire()
        time.sleep(sleeptime)
        lock.release()
        time.sleep(sleeptime)
if __name__ == "__main__":
    lock = thread.allocate_lock()
    thread.start_new_thread(myfunction, ("Thread #: 1", 2, lock))
    thread.start_new_thread(myfunction, ("Thread #: 2", 2, lock))
```

还有`*args`在这里是什么意思?

***

当Python解析器读取一个源文件时,它会执行所有的代码.在执行代码前,会定义一些特殊的变量.例如,如果解析器运行的模块(源文件)作为主程序,它将会把`__name__`变量设置成`"__main__"`.如果只是引入其他的模块,`__name__`变量将会设置成模块的名字.

假设下面是你的脚本,让我们作为主程序来执行:

```
python threading_example.py
```

当设置完特殊变量,它就会执行`import`语句并且加载这些模块.当遇到`def`代码段的时候,它就会创建一个函数对象并创建一个名叫`myfunction`变量指向函数对象.接下来会读取`if`语句并检查`__name__`是不是等于`"__main__"`,如果是的话他就会执行这个代码段.

这么做的原因是有时你需要你写的模块既可以直接的执行,还可以被当做模块导入到其他模块中去.通过检查是不是主函数,可以让你的代码只在它作为主程序运行时执行,而当其他人调用你的模块中的函数的时候不必执行.

如果想了解更多,请查看[这个](http://ibiblio.org/g2swap/byteofpython/read/module-name.html)
