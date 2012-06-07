import mondemand

# create the client
client = mondemand.client_create("my_application")
  
# create a transport to send data
transport = mondemand.transport_lwes_create("10.1.37.27", 9191, None, 0, 60)

# attach the transport to the client
mondemand.add_transport(client, transport)

# add some contextual information to the client
mondemand.set_context(client, "cluster_id", "12345")

# log some stats
mondemand.stats_set(client, "filename.py", 1, "stat_1", 1234)
mondemand.stats_inc(client, "filename.py", 1, "stat_2", 1)

# send it to the network
mondemand.flush(client)
