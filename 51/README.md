| rank | ▲ | ✰ | vote | url |
|:-:|:-:|:-:|:-:|:-:|
|  51 | 403 | 213 | 451 | [url](http://stackoverflow.com/questions/2817869/error-unable-to-find-vcvarsall-bat) |

***

## error: Unable to find vcvarsall.bat

我试着安装Python的`dulwich`包:

```python
pip install dulwich
```

但是得到了个错误:

```python
error: Unable to find vcvarsall.bat
```

如果手动安装也会出现相同的错误:

```python
> python setup.py install
running build_ext
building 'dulwich._objects' extension
error: Unable to find vcvarsall.bat
```

***

对于Windows安装:

当安装包运行`setup.py`时,Python2.7会先寻找已经安装的Visual Studio 2008.你可以在运行`setup.py`直线设置正确的`VS90COMNTOOLS`变量.

根据Visual Studio的不同执行不同的命令:

* Visual Studio 2010 (VS10): SET `VS90COMNTOOLS=%VS100COMNTOOLS%`
* Visual Studio 2012 (VS11): SET `VS90COMNTOOLS=%VS110COMNTOOLS%`
* Visual Studio 2013 (VS12): SET `VS90COMNTOOLS=%VS120COMNTOOLS%`
