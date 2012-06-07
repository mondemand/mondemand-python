%module mondemand
%{
    #include "mondemand.h"
    #define MONDEMAND_UNKNOWN 0
    #define MONDEMAND_GAUGE   1
    #define MONDEMAND_COUNTER 2
    #define MONDEMAND_INC     0
    #define MONDEMAND_DEC     1
    #define MONDEMAND_SET     2
    typedef long long MStatCounter;
%}

%inline %{

struct mondemand_client *
client_create(const char *program_identifier) 
{
  return mondemand_client_create(program_identifier);
}

void 
client_destroy(struct mondemand_client *client)
{
  return mondemand_client_destroy(client);
}

void
set_immediate_send_level(struct mondemand_client *client,
                                   const int level)
{
  return mondemand_set_immediate_send_level(client, level);
}

void
set_no_send_level(struct mondemand_client *client, const int level)
{
  return mondemand_set_no_send_level(client, level);
}

const char *
get_context(struct mondemand_client *client, const char *key)
{
  return mondemand_get_context(client, key);
}

const char **
get_context_keys(struct mondemand_client *client)
{
  return mondemand_get_context_keys(client);
}

int
set_context(struct mondemand_client *client, const char *key, 
                      const char *value)
{
  return mondemand_set_context(client, key, value);
}
                      
void
remove_context(struct mondemand_client *client, const char *key)
{
  return mondemand_remove_context(client, key);
}

void
remove_all_contexts(struct mondemand_client *client)
{
  return mondemand_remove_all_contexts(client);
}

int
add_transport(struct mondemand_client *client,
                        struct mondemand_transport *transport)
{
  return mondemand_add_transport(client, transport);
}

int
level_is_enabled(struct mondemand_client *client,
                           const int log_level)
{
  return mondemand_level_is_enabled(client, log_level);
}

int 
flush_logs(struct mondemand_client *client)
{
  return mondemand_flush_logs(client);
}

int 
flush_stats(struct mondemand_client *client)
{
  return mondemand_flush_stats(client);
}

int 
reset_stats(struct mondemand_client *client)
{
  return mondemand_reset_stats(client);
}

int 
flush(struct mondemand_client *client)
{
  return mondemand_flush(client);
}

int 
log_level_from_string(const char *level)
{
  return mondemand_log_level_from_string(level);
}

MondemandStatType 
stat_type_from_string(const char *type)
{
  return mondemand_stat_type_from_string(type);
}

int
initialize_trace(struct mondemand_client *client,
                            const char *owner,
                            const char *trace_id,
                            const char *message)
{
  return mondemand_initialize_trace(client, owner,
    trace_id, message);
}                           

void
clear_trace(struct mondemand_client *client)
{
  return mondemand_clear_trace(client);
}

const char *
get_trace(struct mondemand_client *client, const char *key)
{
  return mondemand_get_trace(client, key);
}

const char **
get_trace_keys(struct mondemand_client *client)
{
  return mondemand_get_trace_keys(client);
}

int
set_trace(struct mondemand_client *client,
                     const char *key, const char *value)
{
  return mondemand_set_trace(client, key, value);
}

void
remove_trace(struct mondemand_client *client, const char *key)
{
  return mondemand_remove_trace(client, key);
}

void
remove_all_traces(struct mondemand_client *client)
{
  return mondemand_remove_all_traces(client);
}

int
flush_trace(struct mondemand_client *client)
{
  return mondemand_flush_trace(client);
}

struct mondemand_transport *
transport_lwes_create(const char *address, const int port,
                    const char *interface, int emit_heartbeat,
                    int heartbeat_frequency)
{
  return mondemand_transport_lwes_create(address, port,
    interface, emit_heartbeat, heartbeat_frequency);
}

int
stats_inc(struct mondemand_client *client, 
                    const char *filename, const int line, 
                    const char *key, const long value)
{
  return mondemand_stats_perform_op (client, filename, line,
    MONDEMAND_INC, MONDEMAND_COUNTER, key, value);
}

int
stats_dec(struct mondemand_client *client, const char *filename,
                    const int line, const char *key, 
                    const long value)
{
  return mondemand_stats_perform_op (client, filename, line,
    MONDEMAND_DEC, MONDEMAND_COUNTER, key, value * (-1));
}

int
stats_set(struct mondemand_client *client, const char *filename,
                    const int line, const char *key, 
                    const long value)
{
  return mondemand_stats_perform_op(client, filename, line, 
    MONDEMAND_SET, MONDEMAND_GAUGE, key, value);
}

%}
