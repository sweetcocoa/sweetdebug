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