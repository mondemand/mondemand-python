%module mondemand
%feature("autodoc", "1");
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

// This tells SWIG to treat char ** as a special case, needed for the
// char ** in flush_annotations. See goo.gl/EfhRZr
%typemap(in) char ** {
  /* Check if is a list */
  if (PyList_Check($input)) {
    int size = PyList_Size($input);
    int i = 0;
    $1 = (char **) malloc((size+1)*sizeof(char *));
    for (i = 0; i < size; i++) {
      PyObject *o = PyList_GetItem($input,i);
      if (PyString_Check(o))
        $1[i] = PyString_AsString(PyList_GetItem($input,i));
      else {
        PyErr_SetString(PyExc_TypeError,"list must contain strings");
        free($1);
        return NULL;
      }
    }
    $1[i] = 0;
  } else {
    PyErr_SetString(PyExc_TypeError,"not a list");
    return NULL;
  }
}

// This cleans up the char ** array we malloc'd before the function call
%typemap(freearg) char ** {
  free((char *) $1);
}

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

int
initialize_performance_trace (struct mondemand_client *client,
                              const char *id,
                              const char *caller_label)
{
  return mondemand_initialize_performance_trace(client, id, caller_label);
}

int
add_performance_trace_timing (struct mondemand_client *client,
                              const char *label,
                              const long long int start,
                              const long long int end)
{
  return mondemand_add_performance_trace_timing(client, label, start, end);
}

void
clear_performance_trace (struct mondemand_client *client)
{
  return mondemand_clear_performance_trace(client);
}

int
flush_performance_trace(struct mondemand_client *client)
{
  return mondemand_flush_performance_trace(client);
}

int
flush_annotation (const char* id,
                  const long long int timestamp,
                  const char* description,
                  const char* text,
                  const char** tags,
                  const int num_tags,
                  struct mondemand_client *client)
{
  return mondemand_flush_annotation(id, timestamp, description, text, tags, num_tags, client);
}

%}
