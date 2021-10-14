# sweetdebug - Feel easy to debug
---
- Install
```bash
pip install sweetdebug
```


- Just add one(or two) line
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
