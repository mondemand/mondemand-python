from __future__ import absolute_import

from functools import partial
from inspect import getframeinfo, stack
from typing import AnyStr, List

from ._mondemand import ffi, lib
from .lwes_transport import LwesTransport
from .utils import text_to_cstring
from . import utils

_cstring_to_text = partial(utils.cstring_to_text, ffi)
_string_array_to_text_list = partial(utils.string_array_to_text_list, ffi)


class MondemandClient(object):
	def __init__(self, program_id):
		# type: (AnyStr) -> None
		"""
		Create a client with the given program_id
		"""
		client = lib.mondemand_client_create(text_to_cstring(program_id))
		if client == ffi.NULL:
			raise MemoryError('Unable to create mondemand client')

		self.client = ffi.gc(client, lib.mondemand_client_destroy)
		self.transport = None

	def set_immediate_send_level(self, level):
		# type: (int) -> None
		"""Set the immediate send level, which defines the minimum level where
		events are sent as soon as they are received (as opposed to being bundled).
		Out of range values are ignored."""
		lib.mondemand_set_immediate_send_level(self.client, level)

	def set_no_send_level(self, level):
		# type: (int) -> None
		"""Set the no send level, which defines the minimum log level where events
		are sent at all.  Anything lower than this defined level will be suppressed.
		Out of range values are ignored."""
		lib.mondemand_set_no_send_level(self.client, level)

	def level_is_enabled(self, level):
		# type: (int) -> bool
		"""Checks if a log level is enabled, which is useful to callers in case they want
		to check whether or not to bother to log."""
		return bool(lib.mondemand_level_is_enabled(self.client, level))

	def initialize_trace(self, trace_owner, trace_id, trace_message):
		# type: (AnyStr, AnyStr, AnyStr) -> int
		"""
		Initialize a trace with the given owner, id, and message
		"""
		return lib.mondemand_initialize_trace(self.client, text_to_cstring(trace_owner),
			text_to_cstring(trace_id), text_to_cstring(trace_message))

	def clear_trace(self):
		# type: () -> None
		"""
		Remove all trace keys/values and remove the trace owner/id information
		"""
		lib.mondemand_clear_trace(self.client)

	def get_trace(self, key):
		# type: (AnyStr) -> str
		"""
		Return the value for the given trace key
		"""
		return _cstring_to_text(lib.mondemand_get_trace(self.client, text_to_cstring(key)))

	def get_trace_keys(self):
		# type: () -> List[str]
		"""
		Return all the trace keys for the client
		"""
		response = ffi.gc(lib.mondemand_get_trace_keys(self.client), lib.free)
		return _string_array_to_text_list(response)

	def set_trace(self, key, value):
		# type: (AnyStr, AnyStr) -> int
		"""
		Set the trace with the given key to the given value
		"""
		return lib.mondemand_set_trace(self.client, text_to_cstring(key), text_to_cstring(value))

	def remove_trace(self, key):
		# type: (AnyStr) -> None
		"""
		Remove the trace under the given key
		"""
		lib.mondemand_remove_trace(self.client, text_to_cstring(key))

	def remove_all_traces(self):
		# type: () -> None
		"""
		Remove all traces from the client
		"""
		lib.mondemand_remove_all_traces(self.client)

	def get_context(self, key):
		# type: (AnyStr) -> str
		"""
		Get the value for the context with the given key
		"""
		return _cstring_to_text(lib.mondemand_get_context(self.client, text_to_cstring(key)))

	def get_context_keys(self):
		# type: () -> List[str]
		"""
		Return all the context keys for the client
		"""
		response = ffi.gc(lib.mondemand_get_context_keys(self.client), lib.free)
		return _string_array_to_text_list(response)

	def set_context(self, key, value):
		# type: (AnyStr, AnyStr) -> int
		"""
		Set the context with the given key to the given value
		"""
		return lib.mondemand_set_context(self.client, text_to_cstring(key),
			text_to_cstring(value))

	def remove_context(self, key):
		# type: (AnyStr) -> None
		"""
		Remove the context stored under the given key
		"""
		lib.mondemand_remove_context(self.client, text_to_cstring(key))

	def remove_all_contexts(self):
		# type: () -> None
		"""
		Remove all context information from the client
		"""
		lib.mondemand_remove_all_contexts(self.client)

	def reset_stats(self):
		# type: () -> int
		"""
		Reset all stat counters and gauges to 0
		"""
		return lib.mondemand_reset_stats(self.client)

	def stats_inc(self, key, value=1):
		# type: (AnyStr, int) -> int
		"""
		Increment the given COUNTER stat by the given value.  If no value
		is passed in, increment by 1.
		"""
		caller = getframeinfo(stack()[1][0])
		filename = text_to_cstring('%s:%s' % (caller.filename, caller.function))
		return lib.mondemand_stats_perform_op(self.client, filename, caller.lineno,
			lib.MONDEMAND_INC, lib.MONDEMAND_COUNTER, text_to_cstring(key),
			value)

	def stats_dec(self, key, value=1):
		# type: (AnyStr, int) -> int
		"""
		Decrement the given COUNTER stat by the given value.  If no value
		is passed in, decrement by 1.
		"""
		caller = getframeinfo(stack()[1][0])
		filename = text_to_cstring('%s:%s' % (caller.filename, caller.function))
		return lib.mondemand_stats_perform_op(self.client, filename, caller.lineno,
			lib.MONDEMAND_DEC, lib.MONDEMAND_COUNTER, text_to_cstring(key),
			value)

	def stats_set(self, key, value):
		# type: (AnyStr, int) -> int
		"""
		Set the given GAUGE stat to the given value.
		"""
		caller = getframeinfo(stack()[1][0])
		filename = text_to_cstring('%s:%s' % (caller.filename, caller.function))
		return lib.mondemand_stats_perform_op(self.client, filename, caller.lineno,
			lib.MONDEMAND_SET, lib.MONDEMAND_COUNTER, text_to_cstring(key),
			value)

	def flush(self):
		# type: () -> int
		"""
		Send all current trace, stats, and log data using the mondemand client
		"""
		return lib.mondemand_flush(self.client)

	def flush_logs(self):
		# type: () -> int
		"""
		Send all current log data using the mondemand client
		"""
		return lib.mondemand_flush_logs(self.client)

	def flush_stats(self):
		# type: () -> int
		"""
		Send all current stats data using the mondemand client
		"""
		return lib.mondemand_flush_stats(self.client)

	def flush_trace(self):
		# type: () -> int
		"""
		Send all current trace data using the mondemand client
		"""
		return lib.mondemand_flush_trace(self.client)

	def add_transport(self, transport):
		# type: (LwesTransport) -> int
		"""
		Add a transport to the mondemand client
		"""
		self.transport = transport.transport
		return lib.mondemand_add_transport(self.client, self.transport)
