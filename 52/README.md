| rank | ▲ | ✰ | vote | url |
|:-:|:-:|:-:|:-:|:-:|
|  52 | 403 | 113 | 370 | [url](http://stackoverflow.com/questions/1231688/how-do-i-remove-packages-installed-with-pythons-easy-install) |

***

## 如何移除用easy_install下载的包?

用`easy_install`下载包非常方便.但是我至今没发现怎么移除下载的包.

有什么更好的方法来移除包?如果我手动移除的话需要修改什么文件?(比如`rm /usr/local/lib/python2.6/dist-packages/my_installed_pkg.egg`)

***

[pip](http://pypi.python.org/pypi/pip/),另一个选择,提供了"uninstall"命令.

按着[说明](http://pip.readthedocs.org/en/latest/installing.html)安装pip:

```
$ wget https://bootstrap.pypa.io/get-pip.py
$ python get-pip.py
```

然后就可以用`pip uninstall`去移除用`easy_install`安装的包.
