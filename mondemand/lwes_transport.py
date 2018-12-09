from __future__ import absolute_import

from ._mondemand import ffi, lib
from .utils import text_to_cstring


class LwesTransport(object):
	def __init__(self, address, port, interface=None, heartbeat_flag=0,
			heartbeat_frequency=0, ttl=30):

		transport = lib.mondemand_transport_lwes_create_with_ttl(
			text_to_cstring(address), port, text_to_cstring(interface) if interface else ffi.NULL,
			heartbeat_flag, heartbeat_frequency, ttl
		)

		if transport == ffi.NULL:
			raise MemoryError('Unable to create LWES transport')

		# self.transport = ffi.gc(transport, lib.mondemand_transport_lwes_destroy)
		# TODO: mondemand frees all added transports; make sure to free transports that are not added
		self.transport = transport
