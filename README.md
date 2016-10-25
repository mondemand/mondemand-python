
REQUIREMENTS
============
* [mondemand library](https://github.com/mondemand/mondemand)
* [lwes library](https://github.com/lwes)
* [swig](https://github.com/swig/swig)

INSTALL
=======

Run `make` and `make install`.

Example Run
===========

Start lwes-event-printing-listener to echo out all data that the lwes
receives from the mondemand client.

```shell
lwes-event-printing-listener -m 0.0.0.0 -p 42042
python demo.py
```

Investigate demo.py for more examples.
