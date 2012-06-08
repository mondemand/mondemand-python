#!/usr/bin/env python

"""
setup.py file for Mondemand binding
"""

from distutils.core import setup, Extension
import commands, syslog

def pkgconfig(*packages, **kw):
    flag_map = {'-I': 'include_dirs', '-L': 'library_dirs', '-l': 'libraries'}
    for token in commands.getoutput("PKG_CONFIG_PATH=/usr/lib/pkgconfig pkg-config --libs --cflags %s" % ' '.join(packages)).split():
        if flag_map.has_key(token[:2]):
	    kw.setdefault(flag_map.get(token[:2]), []).append(token[2:])
        else:
            kw.setdefault('extra_link_args', []).append(token)
    for k, v in kw.iteritems():
        kw[k] = list(set(v))
    kw['library_dirs'].append('/opt/lib64')
    return kw

mondemand_module = Extension('_mondemand',
                             sources=['mondemand_wrap.c'],
                             **pkgconfig('mondemand-4.0')
                             )

setup(name='mondemand',
      version = '0.0.1',
      author = "Keith Miller",
      author_email = "keith.miller@openx.com", 
      description = """Python bindings for Mondemand""",
      url='http://www.mondemand.org',
      ext_modules = [mondemand_module],
      py_modules = ["mondemand"]
      )
