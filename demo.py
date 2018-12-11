from mondemand.client import MondemandClient
from mondemand.lwes_transport import LwesTransport

# create the client
client = MondemandClient("python_client")

# create a transport to send data
transport = LwesTransport('127.0.0.1', 10201, heartbeat_flag=0, heartbeat_frequency=60)

# attach the transport to the client
client.add_transport(transport)

# add some contextual information to the client
client.set_context("cluster_id", "12345")

# log some stats
client.stats_set("stat_1", 1234)
client.stats_inc("stat_2", 1)

# send it to the network
client.flush_stats()
