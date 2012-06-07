# This file was created automatically by SWIG 1.3.29.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _mondemand
import new
new_instancemethod = new.instancemethod
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


mondemand_client_create = _mondemand.mondemand_client_create
mondemand_client_destroy = _mondemand.mondemand_client_destroy
mondemand_set_immediate_send_level = _mondemand.mondemand_set_immediate_send_level
mondemand_set_no_send_level = _mondemand.mondemand_set_no_send_level
mondemand_get_context = _mondemand.mondemand_get_context
mondemand_get_context_keys = _mondemand.mondemand_get_context_keys
mondemand_set_context = _mondemand.mondemand_set_context
mondemand_remove_context = _mondemand.mondemand_remove_context
mondemand_remove_all_contexts = _mondemand.mondemand_remove_all_contexts
mondemand_add_transport = _mondemand.mondemand_add_transport
mondemand_level_is_enabled = _mondemand.mondemand_level_is_enabled
mondemand_flush_logs = _mondemand.mondemand_flush_logs
mondemand_flush_stats = _mondemand.mondemand_flush_stats
mondemand_reset_stats = _mondemand.mondemand_reset_stats
mondemand_flush = _mondemand.mondemand_flush
mondemand_log_level_from_string = _mondemand.mondemand_log_level_from_string
mondemand_stat_type_from_string = _mondemand.mondemand_stat_type_from_string
mondemand_initialize_trace = _mondemand.mondemand_initialize_trace
mondemand_clear_trace = _mondemand.mondemand_clear_trace
mondemand_get_trace = _mondemand.mondemand_get_trace
mondemand_get_trace_keys = _mondemand.mondemand_get_trace_keys
mondemand_set_trace = _mondemand.mondemand_set_trace
mondemand_remove_trace = _mondemand.mondemand_remove_trace
mondemand_remove_all_traces = _mondemand.mondemand_remove_all_traces
mondemand_flush_trace = _mondemand.mondemand_flush_trace


