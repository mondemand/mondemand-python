import mondemand

# create the client
client = mondemand.client_create("python_client")

# create a transport to send data
transport = mondemand.transport_lwes_create("127.0.0.1", 25552, None, 0, 60)

# attach the transport to the client
mondemand.add_transport(client, transport)

# add some contextual information to the client
mondemand.set_context(client, "cluster_id", "12345")

# set some stats
mondemand.stats_set(client, "demo.py", 1, "stat_1", 1234)
mondemand.stats_inc(client, "demo.py", 1, "stat_2", 1)

# send it to the network
mondemand.flush(client)

# send some annotations
mondemand.flush_annotation('', 1234567890, 'test', 'test desc', [], 0, client)
