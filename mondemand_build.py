import shlex
import subprocess
import sys

from cffi import FFI


def pkgconfig(flags, *pkgs):
	"""Obtain informations through pkg-config"""
	cmd = ['pkg-config', flags]
	cmd.extend(pkgs)
	try:
		out = subprocess.check_output(cmd)
	except subprocess.CalledProcessError as e:
		sys.exit(e.returncode)
	else:
		if isinstance(out, bytes):
			out = out.decode(sys.getfilesystemencoding())

		return shlex.split(out)


ffibuilder = FFI()

ffibuilder.cdef("""
/* Types */
typedef long long MondemandStatValue;

typedef enum {
	MONDEMAND_UNKNOWN = ...,
	MONDEMAND_GAUGE = ...,
	MONDEMAND_COUNTER = ...
} MondemandStatType;

typedef enum {
	MONDEMAND_INC = ...,
	MONDEMAND_DEC = ...,
	MONDEMAND_SET = ...
} MondemandOp;

/* LWES */
struct mondemand_transport *
mondemand_transport_lwes_create(
	const char *address, const int port, const char *interface, int emit_heartbeat,
	int heartbeat_frequency);

struct mondemand_transport *
mondemand_transport_lwes_create_with_ttl(
	const char *address, const int port, const char *interface, int emit_heartbeat,
	int heartbeat_frequency, int ttl);

void
mondemand_transport_lwes_destroy(struct mondemand_transport *transport);                               

/* Mondemand */
struct mondemand_client *
mondemand_client_create(const char *program_identifier);

void mondemand_client_destroy(struct mondemand_client *client);

void
mondemand_set_immediate_send_level(struct mondemand_client *client,
	const int level);

void
mondemand_set_no_send_level(struct mondemand_client *client, const int level);

int
mondemand_level_is_enabled(struct mondemand_client *client, const int log_level);

int
mondemand_initialize_trace(struct mondemand_client *client, const char *owner,
	const char *trace_id, const char *message);

void
mondemand_clear_trace(struct mondemand_client *client);

const char *
mondemand_get_trace(struct mondemand_client *client, const char *key);

const char **
mondemand_get_trace_keys(struct mondemand_client *client);

int
mondemand_set_trace(struct mondemand_client *client, const char *key,
	const char *value);

void
mondemand_remove_trace(struct mondemand_client *client, const char *key);

void
mondemand_remove_all_traces(struct mondemand_client *client);

const char *
mondemand_get_context(struct mondemand_client *client, const char *key);

const char **
mondemand_get_context_keys(struct mondemand_client *client);

int
mondemand_set_context(struct mondemand_client *client, const char *key,
	const char *value);

void
mondemand_remove_context(struct mondemand_client *client, const char *key);

void
mondemand_remove_all_contexts(struct mondemand_client *client);

int
mondemand_reset_stats(struct mondemand_client *client);

int
mondemand_stats_perform_op(struct mondemand_client *client,
	const char *filename, const int line, const MondemandOp op,
	const MondemandStatType type, const char *key,
	const MondemandStatValue value);

int
mondemand_flush(struct mondemand_client *client);

int
mondemand_flush_logs(struct mondemand_client *client);

int
mondemand_flush_stats(struct mondemand_client *client);

int
mondemand_flush_trace(struct mondemand_client *client);

int
mondemand_add_transport(struct mondemand_client *client,
	struct mondemand_transport *transport);

void
free(void *ptr);
""")

ffibuilder.set_source('mondemand._mondemand', """
	#include "mondemand.h"
""",
	extra_compile_args=pkgconfig('--cflags', 'mondemand-4'),
	extra_link_args=pkgconfig('--libs', 'mondemand-4')
)

if __name__ == '__main__':
	ffibuilder.compile(verbose=True, debug=True)
