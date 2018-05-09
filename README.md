# dominos
why did we make this

## the rundown:
this here's a [flask](http://flask.pocoo.org/)-based web app mated to a simple GPIO polling routine that waits for you to press a connected button. once pressed, it will invoke a user-defined python script. originally this started out as something to order pizza with, (hence the name), but it seems only right to make it more general purpose. 

[>inb4 hawaii jokes...](https://i.kinja-img.com/gawker-media/image/upload/s--1_Rqgpab--/c_scale,f_auto,fl_progressive,q_80,w_800/ahlbmm7nifilnj41ta2t.jpg)


## quickstart:
install the requirements:

```
pip install -r requirements.txt
```

run the server:

```
FLASK_APP=server.py flask run --host=0.0.0.0
```

## todo:
finish the quickstart

