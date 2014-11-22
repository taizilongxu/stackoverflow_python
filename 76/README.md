| rank | ▲ | ✰ | vote | url |
|:-:|:-:|:-:|:-:|:-:|
|  76 | 340 | 217 | 397 | [url](http://stackoverflow.com/questions/2720014/upgrading-all-packages-with-pip) |

***

## 用pip升级所有包

可不可以用pip一次性升级所有的Python包?

注:在官方的issue里也有这个[需求](http://stackoverflow.com/questions/2720014/upgrading-all-packages-with-pip).

***

内部还不支持这个命令,但是可以这样:

```
pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs pip install -U
```
