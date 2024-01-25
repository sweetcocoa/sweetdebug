# sweetdebug - Feel easy to debug
---
Automatic pdb invoker, Telegram support

## Install
```bash
pip install sweetdebug
```
or (To use Telegram notification)
```bash
pip install sweetdebug[telegram]
```


## Main Feature
- Just add one(or two) line.
```python
from sweetdebug import sweetdebug
sweetdebug()
1/0 # Error !!
```

- This will invoke pdb automatically.

```bash
Traceback (Most recent call last):
3 /main.py <module> --> 1/0
ZeroDivisionError: division by zero
> /main.py(3)<module>()
-> 1/0
(Pdb) 
```


## Other feature(s)
- You can receive error message with Telegram, too.
- To get Telegram authentication token, See [Telegram Botfather](https://core.telegram.org/bots/features#botfather) for details.
```python
# Assume you have Telegram tokens and corresponding chat ids.

token = "123456789:ABCDEF_VGRXDZKwvHS8@Xca5e2EnZdfsgTw"
chat_ids = ["13852425", '29384594']
sweetdebug(telegram=True, telegram_api_token=token, chat_ids=chat_ids)


1/0 # Error !!
```

- Also, If you have used your tokens and chat ids, then you can use cached token and chat ids.
```python
sweetdebug(telegram=True)
```

![img](./resource/telegram_sample.png)


## Other feature(s) - 2 (Added from 1.0.8)
- sweettimer : simple timer for a code snippets

```python
from sweetdebug import sweettimer

# simple timer for a function
@sweettimer()
def xxx1():
    return sum([i for i in range(1000)])


# replace function name or time units
@sweettimer(name="my_xxx", unit="ms")
def xxx2():
    return sum([i for i in range(1000)])

# also supports context-level
with sweettimer():
    sum([i for i in range(1000)])

xxx1()
xxx2()

# you can also check elapsed times through this class attribute
print(sweettimer.times)
```

```bash
(/home/jongho/workspace/testbed/timer.py, line 15) :: elapsed 0.01293182373046875 s
(/home/jongho/workspace/testbed/timer.py)[xxx1] :: elapsed 2.288818359375e-05 s
(/home/jongho/workspace/testbed/timer.py)[my_xxx] :: elapsed 0.019788742065429688 ms
[(None, 0.011715888977050781, 's'), ('xxx1', 2.09808349609375e-05, 's'), ('my_xxx', 1.6927719116210938e-05, 'ms')]
```