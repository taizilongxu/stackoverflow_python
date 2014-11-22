| rank | ▲ | ✰ | vote | url |
|:-:|:-:|:-:|:-:|:-:|
|  53 | 400 | 168 | 184 | [url](http://stackoverflow.com/questions/279237/import-a-module-from-a-relative-path) |

***

## 从相对路径引入一个模块

怎么用相对路径引入一个模块?

例如,如果`dirFoo`包含`Foo.py`和`dirBar`,而`dirBar`包含`Bar.py`,怎么样才能在`Foo.py`里引入`Bar.py`?

结构:

```
dirFoo\
    Foo.py
    dirBar\
        Bar.py
```

`Foo`希望包含`Bar`,但是重新组织文件结构好像不太好.

***

确定`djirBar`有一个`__init__.py`文件--使你的目录包含一个Python包.


