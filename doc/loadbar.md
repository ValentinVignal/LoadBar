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

### Constructor

```python
bar = loadbar.LoadBar()
```

- `max=100` the number of steps of your loading
- `size=20` the size of the loading bar in number of characters
- `head='.'` the character of the first element of the loading bar
- `body='.'` the characters used to fill the loading bar
- `border_left='['` the character at the left of the loading bar
- `border_right=']'` the character at the right of the loading bar
- `show_step=True` boolean indicating whether to show the current step number (`100/100`)
- `show_percentage=True` boolean indicating whether to show the current percentage (`100%`)
- `show_eta=True` boolean indicating whether to show the eta (`0:00:10`)

Here is a example of a custome loading bar:

```python
import loadbar
import time

bar = loadbar.LoadBar(
    head='>',
    body='-',
    border_left='(',
    border_right=')'
)
bar.start()
for i in range(100):
    time.sleep(0.1)
    bar.update()
bar.end()
```

It creates the output

![image](../images/loadbar_custom.gif)

### Update method

```python
bar.update()
```

By default the call of the method will add `1` to the progress.
However, you can custom it with the following parameters:
- `to_add` to specify how many to add to the progress.
For example, `to_add=2` will add `2` to the progress
- `step` to specify when to set the progress.
For example, `step=10` will set the progress to `10`


## ColorBar

## RainbowBar