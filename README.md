# LoadBar

This is a very simple python library to create a loading bar on the shell

## Install it

```
pip install load-bar
```

## Use it

``` python
import time
from loadbar import LoadBar
bar = LoadBar(max=100)
bar.start()
for i in range(100):
    time.sleep(0.05)
    bar.update(step=i)
bar.end()
```

![image](images/loadbar.gif)

[See the documentation](https://github.com/ValentinVignal/LoadBar/blob/master/doc/Loadbar.md)
