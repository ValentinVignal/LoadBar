# LoadBar

**LoadBar** is a very simple library to create a loading bar in the terminal

## Install it

```
pip install load-bar
```

## Use it

Here is a simple script to show the loading bar

```python
import loadbar
import time

bar = loadbar.LoadBar()
bar.start()
for i in range(100):
    time.sleep(0.1)
    bar.update()
bar.end()
```

Here is what produces: 
![image](../images/loadbar.gif)

## Options

## ColorBar

## RainbowBar