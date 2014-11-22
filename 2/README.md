| rank | ▲ | ✰ | vote | url |
|:-:|:-:|:-:|:-:|:-:|
| 2 | 1919 | 1842 | 3137 | [url](http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python) |

***

## Python中的元类(metaclass)是什么?

元类是什么?如何使用元类?



***

#### 类对象

在理解元类之前,你需要掌握Python里的类.Python中类的概念借鉴于Smalltalk，这显得有些奇特.

在大多数语言中,类就是一组用来描述如何生成一个对象的代码段。在Python中这一点仍然成立：

```python
>>> class ObjectCreator(object):
...       pass
...

>>> my_object = ObjectCreator()
>>> print(my_object)
<__main__.ObjectCreator object at 0x8974f2c>
```

但是在Python中类也是对象.

是的,对象.

每当你用到关键字```class```,Python就会执行它并且建立一个对象.例如:

```python
>>> class ObjectCreator(object):
...       pass
...
```

上面代码在内存里创建了名叫"ObjectCreator"的对象.

这个对象(类)有生成对象(实例)的能力,这就是为什么叫做类.

它是个对象,所以:

* 你可以把它赋值给一个变量
* 你可以赋值它
* 你可以给它添加属性
* 你个以作为函数参数来传递它

e.g.:

```python
>>> print(ObjectCreator) # 你可以打印一个类,因为它是一个对象
<class '__main__.ObjectCreator'>
>>> def echo(o):
...       print(o)
...
>>> echo(ObjectCreator) # 你可以把类作为参数传递
<class '__main__.ObjectCreator'>
>>> print(hasattr(ObjectCreator, 'new_attribute'))
False
>>> ObjectCreator.new_attribute = 'foo' # 可以给一个类添加属性
>>> print(hasattr(ObjectCreator, 'new_attribute'))
True
>>> print(ObjectCreator.new_attribute)
foo
>>> ObjectCreatorMirror = ObjectCreator # 可以把类赋值给一个变量
>>> print(ObjectCreatorMirror.new_attribute)
foo
>>> print(ObjectCreatorMirror())
<__main__.ObjectCreator object at 0x8997b4c>
```

#### 动态创建类

因为类也是对象，你可以在运行时动态的创建它们，就像其他任何对象一样。

首先，你可以在函数中创建类，使用class关键字即可:

```python
>>> def choose_class(name):
...     if name == 'foo':
...         class Foo(object):
...             pass
...         return Foo # 返回一个类不是一个实例
...     else:
...         class Bar(object):
...             pass
...         return Bar
...
>>> MyClass = choose_class('foo')
>>> print(MyClass) # 返回一个类不是一个实例
<class '__main__.Foo'>
>>> print(MyClass()) # 你可以在类里创建一个对象
<__main__.Foo object at 0x89c6d4c>
```

但这还不够动态,因为你仍然需要自己编写整个类的代码.

既然类是对象,那么肯定有什么东西来生成它.

当你使用关键字```objects```,Python自动的创建对象.像Python中大多数的东西一样,他也给你自己动手的机会.

记得函数```type```吗?这个古老好用的函数能让你知道对象的类型是什么:

```python
>>> print(type(1))
<type 'int'>
>>> print(type("1"))
<type 'str'>
>>> print(type(ObjectCreator))
<type 'type'>
>>> print(type(ObjectCreator()))
<class '__main__.ObjectCreator'>
```

这里,```type```有一种完全不同的能力,它也能动态的创建类.```type```可以接受一个类的描述作为参数,然后返回一个类.

(我知道，根据传入参数的不同，同一个函数拥有两种完全不同的用法是一件很傻的事情，但这在Python中是为了保持向后兼容性)

```type```这样工作:

```python
type(类名,
     父类名的元组 (针对继承情况,可以为空),
     包含属性的字典(名称和值))
```

e.g.:

```python
>>> class MyShinyClass(object):
...       pass
```

可以手动创建:

```python
>>> MyShinyClass = type('MyShinyClass', (), {}) # 返回类对象
>>> print(MyShinyClass)
<class '__main__.MyShinyClass'>
>>> print(MyShinyClass()) # 创建一个类的实例
<__main__.MyShinyClass object at 0x8997cec>
```

你会发现我们使用“MyShinyClass”作为类名，并且也可以把它当做一个变量来作为类的引用。类和变量是不同的，这里没有任何理由把事情弄的复杂。

```type```可以接受一个字典来定义类的属性:

```python
>>> class Foo(object):
...       bar = True
```

可以写成:

```python
>>> Foo = type('Foo', (), {'bar':True})
```

然后我们可以像用正常类来用它:

```python
>>> print(Foo)
<class '__main__.Foo'>
>>> print(Foo.bar)
True
>>> f = Foo()
>>> print(f)
<__main__.Foo object at 0x8a9b84c>
>>> print(f.bar)
True
```

当然,你也可以继承它:

```python
>>>   class FooChild(Foo):
...         pass
```

这样:

```python
>>> FooChild = type('FooChild', (Foo,), {})
>>> print(FooChild)
<class '__main__.FooChild'>
>>> print(FooChild.bar) # bar从Foo继承
True
```

要是在类中添加方法,你要做的就是把函数名写入字典就可以了,不懂可以看下面:

```python
>>> def echo_bar(self):
...       print(self.bar)
...
>>> FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar})
>>> hasattr(Foo, 'echo_bar')
False
>>> hasattr(FooChild, 'echo_bar')
True
>>> my_foo = FooChild()
>>> my_foo.echo_bar()
True
```

你可以看到，在Python中，类也是对象，你可以动态的创建类。这就是当你使用关键字class时Python在幕后做的事情，而这就是通过元类来实现的。

#### 什么是元类(终于到正题了)

元类就是创建类的东西.

你是为了创建对象才定义类的,对吧?

但是我们已经知道了Python的类是对象.

这里,元类创建类.它们是类的类,你可以把它们想象成这样:

```python
MyClass = MetaClass()
MyObject = MyClass()
```

你已经看到了```type```可以让你像这样做：

```python
MyClass = type('MyClass', (), {})
```

这是因为```type```就是一个元类.```type```是Python中创建所有类的元类.

现在你可能纳闷为啥子```type```用小写而不写成```Type```?

我想是因为要跟```str```保持一致,```str```创建字符串对象,```int```创建整数对象.```type```正好创建类对象.

你可以通过检查```__class__```属性来看到这一点.

Python中**所有的东西**都是对象.包括整数,字符串,函数还有类.所有这些都是对象.所有这些也都是从类中创建的:

```python
>>> age = 35
>>> age.__class__
<type 'int'>
>>> name = 'bob'
>>> name.__class__
<type 'str'>
>>> def foo(): pass
>>> foo.__class__
<type 'function'>
>>> class Bar(object): pass
>>> b = Bar()
>>> b.__class__
<class '__main__.Bar'>
```

那么,```__class__```的```__class__```属性是什么?

```python
>>> age.__class__.__class__
<type 'type'>
>>> name.__class__.__class__
<type 'type'>
>>> foo.__class__.__class__
<type 'type'>
>>> b.__class__.__class__
<type 'type'>
```

所以,元类就是创建类对象的东西.

如果你愿意你也可以把它叫做'类工厂'.```type```是Python的内建元类,当然,你也可以创建你自己的元类.

#### ```__metaclass__```属性

当你创建一个函数的时候,你可以添加```__metaclass__```属性:

```python
class Foo(object):
  __metaclass__ = something...
  [...]
```

如果你这么做了，Python就会用元类来创建类Foo.

小心点，这里面有些技巧.

你首先写下```class Foo(object```，但是类对象```Foo```还没有在内存中创建.

Python将会在类定义中寻找```__metaclass__```.如果找打了就用它来创建类对象```Foo```.如果没找到,就会默认用```type```创建类.

把下面这段话反复读几次。

当你写如下代码时 :

```python
class Foo(Bar):
  pass
```

Python将会这样运行:

在```Foo```中有没有```___metaclass__```属性?

如果有,Python会在内存中通过```__metaclass__```创建一个名字为```Foo```的类对象(我说的是类对象,跟紧我的思路).

如果Python没有找到```__metaclass__```，它会继续在Bar（父类）中寻找```__metaclass__属性```，并尝试做和前面同样的操作.

如果Python在任何父类中都找不到```__metaclass__```，它就会在模块层次中去寻找```__metaclass__```，并尝试做同样的操作。

如果还是找不到```__metaclass__```,Python就会用内置的```type```来创建这个类对象。

现在的问题就是，你可以在```__metaclass__```中放置些什么代码呢？

答案就是：可以创建一个类的东西。

那么什么可以用来创建一个类呢？```type```，或者任何使用到```type```或者子类化```type```的东东都可以。

#### 自定义元类

元类的主要目的就是为了当创建类时能够自动地改变类.

通常，你会为API做这样的事情，你希望可以创建符合当前上下文的类.

假想一个很傻的例子，你决定在你的模块里所有的类的属性都应该是大写形式。有好几种方法可以办到，但其中一种就是通过在模块级别设定```__metaclass__```.

采用这种方法，这个模块中的所有类都会通过这个元类来创建，我们只需要告诉元类把所有的属性都改成大写形式就万事大吉了。

幸运的是，```__metaclass__```实际上可以被任意调用，它并不需要是一个正式的类（我知道，某些名字里带有'class'的东西并不需要是一个class，画画图理解下，这很有帮助）。

所以，我们这里就先以一个简单的函数作为例子开始。

```python
# 元类会自动将你通常传给'type'的参数作为自己的参数传入
def upper_attr(future_class_name, future_class_parents, future_class_attr):
  """
    返回一个将属性列表变为大写字母的类对象
  """

  # 选取所有不以'__'开头的属性,并把它们编程大写
  uppercase_attr = {}
  for name, val in future_class_attr.items():
      if not name.startswith('__'):
          uppercase_attr[name.upper()] = val
      else:
          uppercase_attr[name] = val

  # 用'type'创建类
  return type(future_class_name, future_class_parents, uppercase_attr)

__metaclass__ = upper_attr # 将会影响整个模块

class Foo(): # global __metaclass__ won't work with "object" though
  # 我们也可以只在这里定义__metaclass__，这样就只会作用于这个类中
  bar = 'bip'

print(hasattr(Foo, 'bar'))
# 输出: False
print(hasattr(Foo, 'BAR'))
# 输出: True

f = Foo()
print(f.BAR)
# 输出: 'bip'
```

现在让我们再做一次，这一次用一个真正的class来当做元类。

```python
# 请记住，'type'实际上是一个类，就像'str'和'int'一样
# 所以，你可以从type继承
class UpperAttrMetaclass(type):
    # __new__ 是在__init__之前被调用的特殊方法
    # __new__是用来创建对象并返回它的方法
    # 而__init__只是用来将传入的参数初始化给对象
    # 你很少用到__new__，除非你希望能够控制对象的创建
    # 这里，创建的对象是类，我们希望能够自定义它，所以我们这里改写__new__
    # 如果你希望的话，你也可以在__init__中做些事情
    # 还有一些高级的用法会涉及到改写__call__特殊方法，但是我们这里不用
    def __new__(upperattr_metaclass, future_class_name,
                future_class_parents, future_class_attr):

        uppercase_attr = {}
        for name, val in future_class_attr.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        return type(future_class_name, future_class_parents, uppercase_attr)
```

但是这不是真正的面向对象(OOP).我们直接调用了type，而且我们没有改写父类的__new__方法。现在让我们这样去处理:

```python
class UpperAttrMetaclass(type):

    def __new__(upperattr_metaclass, future_class_name,
                future_class_parents, future_class_attr):

        uppercase_attr = {}
        for name, val in future_class_attr.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        # 重用 type.__new__ 方法
        # 这就是基本的OOP编程，没什么魔法
        return type.__new__(upperattr_metaclass, future_class_name,
                            future_class_parents, uppercase_attr)
```

你可能已经注意到了有个额外的参数```upperattr_metaclass```，这并没有什么特别的。类方法的第一个参数总是表示当前的实例，就像在普通的类方法中的```self```参数一样。

当然了，为了清晰起见，这里的名字我起的比较长。但是就像```self```一样，所有的参数都有它们的传统名称。因此，在真实的产品代码中一个元类应该是像这样的：

```python
class UpperAttrMetaclass(type):

    def __new__(cls, clsname, bases, dct):

        uppercase_attr = {}
        for name, val in dct.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        return type.__new__(cls, clsname, bases, uppercase_attr)
```

如果使用super方法的话，我们还可以使它变得更清晰一些，这会缓解继承（是的，你可以拥有元类，从元类继承，从type继承）

```python
class UpperAttrMetaclass(type):

    def __new__(cls, clsname, bases, dct):

        uppercase_attr = {}
        for name, val in dct.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        return super(UpperAttrMetaclass, cls).__new__(cls, clsname, bases, uppercase_attr)
```

就是这样，除此之外，关于元类真的没有别的可说的了。

使用到元类的代码比较复杂，这背后的原因倒并不是因为元类本身，而是因为你通常会使用元类去做一些晦涩的事情，依赖于自省，控制继承等等。

确实，用元类来搞些“黑暗魔法”是特别有用的，因而会搞出些复杂的东西来。但就元类本身而言，它们其实是很简单的：

* 拦截类的创建
* 修改一个类
* 返回修改之后的类

#### 为什么要用metaclass类而不是函数?

由于```__metaclass__```可以接受任何可调用的对象，那为何还要使用类呢，因为很显然使用类会更加复杂啊？

这里有好几个原因：

* 意图会更加清晰。当你读到```UpperAttrMetaclass(type)```时，你知道接下来要发生什么。
* 你可以使用OOP编程。元类可以从元类中继承而来，改写父类的方法。元类甚至还可以使用元类。
* 你可以把代码组织的更好。当你使用元类的时候肯定不会是像我上面举的这种简单场景，通常都是针对比较复杂的问题。将多个方法归总到一个类中会很有帮助，也会使得代码更容易阅读。
* 你可以使用```__new__```,``` __init__```以及```__call__```这样的特殊方法。它们能帮你处理不同的任务。就算通常你可以把所有的东西都在```__new__```里处理掉，有些人还是觉得用```__init__```更舒服些。
* 哇哦，这东西的名字是metaclass，肯定非善类，我要小心！

#### 说了这么多TMD究竟为什么要使用元类？

现在回到我们的大主题上来，究竟是为什么你会去使用这样一种容易出错且晦涩的特性？

好吧，一般来说，你根本就用不上它：

>“元类就是深度的魔法，99%的用户应该根本不必为此操心。如果你想搞清楚究竟是否需要用到元类，那么你就不需要它。那些实际用到元类的人都非常清楚地知道他们需要做什么，而且根本不需要解释为什么要用元类。”  —— Python界的领袖 Tim Peters

元类的主要用途是创建API。一个典型的例子是Django ORM。

它允许你像这样定义：

```python
class Person(models.Model):
  name = models.CharField(max_length=30)
  age = models.IntegerField()
```

但是如果你像这样做的话：

```python
guy = Person(name='bob', age='35')
print(guy.age)
```

这并不会返回一个```IntegerField```对象，而是会返回一个int，甚至可以直接从数据库中取出数据。

这是有可能的，因为```models.Model```定义了```__metaclass__```， 并且使用了一些魔法能够将你刚刚定义的简单的Person类转变成对数据库的一个复杂hook。

Django框架将这些看起来很复杂的东西通过暴露出一个简单的使用元类的API将其化简，通过这个API重新创建代码，在背后完成真正的工作。

#### 结语

首先，你知道了类其实是能够创建出类实例的对象。

好吧，事实上，类本身也是实例，当然，它们是元类的实例。

```python
>>> class Foo(object): pass
>>> id(Foo)
142630324
```

Python中的一切都是对象，它们要么是类的实例，要么是元类的实例.

除了```type```.```type```实际上是它自己的元类，在纯Python环境中这可不是你能够做到的，这是通过在实现层面耍一些小手段做到的。

其次，元类是很复杂的。对于非常简单的类，你可能不希望通过使用元类来对类做修改。你可以通过其他两种技术来修改类：

* [monkey patching](http://en.wikipedia.org/wiki/Monkey_patch)
* 装饰器

当你需要动态修改类时，99%的时间里你最好使用上面这两种技术。当然了，其实在99%的时间里你根本就不需要动态修改类 :D
