%module mondemand
%{
    #include "mondemand.h"
%}

struct mondemand_client *
mondemand_client_create(const char *program_identifier);

void mondemand_client_destroy(struct mondemand_client *client);

void
mondemand_set_immediate_send_level(struct mondemand_client *client,
                                   const int level);

void
mondemand_set_no_send_level(struct mondemand_client *client, const int level);

const char *
mondemand_get_context(struct mondemand_client *client, const char *key);

const char **
mondemand_get_context_keys(struct mondemand_client *client);

int
mondemand_set_context(struct mondemand_client *client,
                      const char *key, const char *value);

void
mondemand_remove_context(struct mondemand_client *client, const char *key);

void
mondemand_remove_all_contexts(struct mondemand_client *client);

int
mondemand_add_transport(struct mondemand_client *client,
                        struct mondemand_transport *transport);

int
mondemand_level_is_enabled(struct mondemand_client *client,
                           const int log_level);

int mondemand_flush_logs(struct mondemand_client *client);

int mondemand_flush_stats(struct mondemand_client *client);

int mondemand_reset_stats (struct mondemand_client *client);

int mondemand_flush(struct mondemand_client *client);

int mondemand_log_level_from_string (const char *level);

MondemandStatType mondemand_stat_type_from_string (const char *type);

int
mondemand_initialize_trace (struct mondemand_client *client,
                            const char *owner,
                            const char *trace_id,
                            const char *message);

void
mondemand_clear_trace (struct mondemand_client *client);

const char *
mondemand_get_trace (struct mondemand_client *client, const char *key);

const char **
mondemand_get_trace_keys (struct mondemand_client *client);

int
mondemand_set_trace (struct mondemand_client *client,
                     const char *key, const char *value);

void
mondemand_remove_trace (struct mondemand_client *client, const char *key);

void
mondemand_remove_all_traces (struct mondemand_client *client);

int
mondemand_flush_trace(struct mondemand_client *client);

