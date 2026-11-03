## dhammapada-bot.py

### dependencies

* python 3

### how to use

0. clone the repository
4. run via crontab the script `dhammapada-bot.py`; you can follow the example below.

### `crontab -e` example

`0 */6 * * * /home/USERNAME/.venv/bin/python /home/USERNAME/cronjobs/dhammapada-bot/dhammapada-bot.py`

First is the path to the python executable, then the script.

This would run it at 0h, 6h, 12h and 18h.

### running

```
python ./dhammapada-bot.py
```
