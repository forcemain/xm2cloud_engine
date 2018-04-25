### For Arch:
#### xm2cloud_engine is a powerful and graceful engine component for xm2cloud devops framework.

### For Task:

```
```

### For Debug:


```
:0: UserWarning: You do not have a working installation of the service_identity module: 'cannot import name opentype'.  Please install it from <https://pypi.python.org/pypi/service_identity> and make sure all of its dependencies are satisfied.  Without the service_identity module, Twisted can perform only rudimentary TLS client hostname verification.  Many valid certificate/hostname mappings may be rejected.
2018-04-25 11:01:01,441 - server.core.engine - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/engine.py - 126 - INFO - No events ready, next scheduled at 2018-04-25 11:01:02
2018-04-25 11:01:01,442 - server.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/channel/rabbitmq.py - 63 - INFO - Connecting to ops.xxoo.com:5672
2018-04-25 11:01:01,443 - server.core.heatbeat - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/heatbeat.py - 76 - INFO - Events ready, next scheduled at 2018-04-25 11:01:04
2018-04-25 11:01:01,443 - server.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/channel/rabbitmq.py - 122 - INFO - Connecting to ops.xxoo.com:5672
2018-04-25 11:01:01,444 - server.core.channel - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/channel.py - 73 - WARNING - Channel sender status, disconnected
2018-04-25 11:01:01,445 - server.core.channel - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/channel.py - 75 - WARNING - Channel receiver status, disconnected
2018-04-25 11:01:01,446 - server.core.channel - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/channel.py - 107 - INFO - Events ready, next scheduled at 2018-04-25 11:01:02
2018-04-25 11:01:01,490 - pika.adapters.base_connection - /Library/Python/2.7/site-packages/pika/adapters/base_connection.py - 217 - INFO - Connecting to 120.131.14.225:5672
2018-04-25 11:01:01,491 - pika.adapters.base_connection - /Library/Python/2.7/site-packages/pika/adapters/base_connection.py - 217 - INFO - Connecting to 120.131.14.225:5672
2018-04-25 11:01:01,714 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 42 - INFO - Connection opened
2018-04-25 11:01:01,714 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 52 - INFO - Adding connection close callback
2018-04-25 11:01:01,715 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 76 - INFO - Creating a new channel
2018-04-25 11:01:01,715 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 47 - INFO - Connection opened
2018-04-25 11:01:01,716 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 57 - INFO - Adding connection close callback
2018-04-25 11:01:01,716 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 86 - INFO - Creating a new channel
2018-04-25 11:01:01,766 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 80 - INFO - Channel opened
2018-04-25 11:01:01,766 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 89 - INFO - Adding channel close callback
2018-04-25 11:01:01,766 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 98 - INFO - Declaring exchange event_up_exchange
2018-04-25 11:01:01,767 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 122 - INFO - Issuing consumer related RPC commands
2018-04-25 11:01:01,767 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 128 - INFO - Adding consumer cancellation callback
2018-04-25 11:01:01,770 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 90 - INFO - Channel opened
2018-04-25 11:01:01,770 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 99 - INFO - Adding channel close callback
2018-04-25 11:01:01,770 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 108 - INFO - Declaring exchange event_down_exchange
2018-04-25 11:01:01,771 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 132 - INFO - Issuing consumer related RPC commands
2018-04-25 11:01:01,771 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 137 - INFO - Issuing Confirm.Select RPC command
2018-04-25 11:01:01,771 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:01,820 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 104 - INFO - Exchange declared
2018-04-25 11:01:01,821 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 108 - INFO - Declaring queue event_up_queue
2018-04-25 11:01:01,837 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 114 - INFO - Exchange declared
2018-04-25 11:01:01,838 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 118 - INFO - Declaring queue event_down_queue
2018-04-25 11:01:01,881 - server.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/channel/rabbitmq.py - 129 - INFO - Received message # 1 from None: {
    "target_host_id": null, 
    "handled_event_host_id": null, 
    "event_source": "xm2cloud_agent", 
    "target_hostgroup_id": null, 
    "source_cluster_id": [
        1
    ], 
    "event_id": null, 
    "encryption": null, 
    "response_code": null, 
    "agent_uuid": "f352c284-19f3-44ef-927e-8ad2eabdae94", 
    "source_host_id": 1, 
    "target_cluster_id": null, 
    "event_name": "heartbeat", 
    "source_hostgroup_id": [
        14
    ], 
    "handled_event_cluster_id": null, 
    "event_timestamp": 1524624355, 
    "source_version": "0.0.1", 
    "handled_event_hostgroup_id": null, 
    "event_uuid": "d7c962dc-3047-49f3-b8da-debb29de0b3b", 
    "event_data": "{\n    \"version\": \"0.0.1\", \n    \"name\": \"xm2cloud_agent\"\n}", 
    "handled_event_id": null
}
2018-04-25 11:01:01,882 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 141 - INFO - Acknowledging message 1
2018-04-25 11:01:01,882 - server.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/channel/rabbitmq.py - 129 - INFO - Received message # 2 from None: {
    "target_host_id": null, 
    "handled_event_host_id": null, 
    "event_source": "xm2cloud_agent", 
    "target_hostgroup_id": null, 
    "source_cluster_id": [
        1
    ], 
    "event_id": null, 
    "encryption": null, 
    "response_code": null, 
    "agent_uuid": "f352c284-19f3-44ef-927e-8ad2eabdae94", 
    "source_host_id": 1, 
    "target_cluster_id": null, 
    "event_name": "heartbeat", 
    "source_hostgroup_id": [
        14
    ], 
    "handled_event_cluster_id": null, 
    "event_timestamp": 1524624355, 
    "source_version": "0.0.1", 
    "handled_event_hostgroup_id": null, 
    "event_uuid": "d7c962dc-3047-49f3-b8da-debb29de0b3b", 
    "event_data": "{\n    \"version\": \"0.0.1\", \n    \"name\": \"xm2cloud_agent\"\n}", 
    "handled_event_id": null
}
2018-04-25 11:01:01,883 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 141 - INFO - Acknowledging message 2
2018-04-25 11:01:01,883 - server.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/channel/rabbitmq.py - 129 - INFO - Received message # 3 from None: {
    "target_host_id": null, 
    "handled_event_host_id": null, 
    "event_source": "xm2cloud_agent", 
    "target_hostgroup_id": null, 
    "source_cluster_id": [
        1
    ], 
    "event_id": null, 
    "encryption": null, 
    "response_code": null, 
    "agent_uuid": "f352c284-19f3-44ef-927e-8ad2eabdae94", 
    "source_host_id": 1, 
    "target_cluster_id": null, 
    "event_name": "heartbeat", 
    "source_hostgroup_id": [
        14
    ], 
    "handled_event_cluster_id": null, 
    "event_timestamp": 1524624358, 
    "source_version": "0.0.1", 
    "handled_event_hostgroup_id": null, 
    "event_uuid": "da02b84b-7e52-4a69-950c-40b3cc4a8f58", 
    "event_data": "{\n    \"version\": \"0.0.1\", \n    \"name\": \"xm2cloud_agent\"\n}", 
    "handled_event_id": null
}
2018-04-25 11:01:01,884 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 141 - INFO - Acknowledging message 3
2018-04-25 11:01:01,884 - server.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/channel/rabbitmq.py - 129 - INFO - Received message # 4 from None: {
    "target_host_id": null, 
    "handled_event_host_id": null, 
    "event_source": "xm2cloud_agent", 
    "target_hostgroup_id": null, 
    "source_cluster_id": [
        1
    ], 
    "event_id": null, 
    "encryption": null, 
    "response_code": null, 
    "agent_uuid": "f352c284-19f3-44ef-927e-8ad2eabdae94", 
    "source_host_id": 1, 
    "target_cluster_id": null, 
    "event_name": "heartbeat", 
    "source_hostgroup_id": [
        14
    ], 
    "handled_event_cluster_id": null, 
    "event_timestamp": 1524624358, 
    "source_version": "0.0.1", 
    "handled_event_hostgroup_id": null, 
    "event_uuid": "da02b84b-7e52-4a69-950c-40b3cc4a8f58", 
    "event_data": "{\n    \"version\": \"0.0.1\", \n    \"name\": \"xm2cloud_agent\"\n}", 
    "handled_event_id": null
}
2018-04-25 11:01:01,885 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 141 - INFO - Acknowledging message 4
2018-04-25 11:01:01,885 - server.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/channel/rabbitmq.py - 129 - INFO - Received message # 5 from None: {
    "target_host_id": null, 
    "handled_event_host_id": null, 
    "event_source": "xm2cloud_agent", 
    "target_hostgroup_id": null, 
    "source_cluster_id": [
        1
    ], 
    "event_id": null, 
    "encryption": null, 
    "response_code": null, 
    "agent_uuid": "f352c284-19f3-44ef-927e-8ad2eabdae94", 
    "source_host_id": 1, 
    "target_cluster_id": null, 
    "event_name": "heartbeat", 
    "source_hostgroup_id": [
        14
    ], 
    "handled_event_cluster_id": null, 
    "event_timestamp": 1524624361, 
    "source_version": "0.0.1", 
    "handled_event_hostgroup_id": null, 
    "event_uuid": "a622ac5b-1cf7-4b29-9011-38f6c95dbade", 
    "event_data": "{\n    \"version\": \"0.0.1\", \n    \"name\": \"xm2cloud_agent\"\n}", 
    "handled_event_id": null
}
2018-04-25 11:01:01,885 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 141 - INFO - Acknowledging message 5
2018-04-25 11:01:01,886 - server.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/channel/rabbitmq.py - 129 - INFO - Received message # 6 from None: {
    "target_host_id": null, 
    "handled_event_host_id": null, 
    "event_source": "xm2cloud_agent", 
    "target_hostgroup_id": null, 
    "source_cluster_id": [
        1
    ], 
    "event_id": null, 
    "encryption": null, 
    "response_code": null, 
    "agent_uuid": "f352c284-19f3-44ef-927e-8ad2eabdae94", 
    "source_host_id": 1, 
    "target_cluster_id": null, 
    "event_name": "heartbeat", 
    "source_hostgroup_id": [
        14
    ], 
    "handled_event_cluster_id": null, 
    "event_timestamp": 1524624361, 
    "source_version": "0.0.1", 
    "handled_event_hostgroup_id": null, 
    "event_uuid": "a622ac5b-1cf7-4b29-9011-38f6c95dbade", 
    "event_data": "{\n    \"version\": \"0.0.1\", \n    \"name\": \"xm2cloud_agent\"\n}", 
    "handled_event_id": null
}
2018-04-25 11:01:01,886 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 141 - INFO - Acknowledging message 6
2018-04-25 11:01:01,886 - server.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/channel/rabbitmq.py - 129 - INFO - Received message # 7 from None: {
    "target_host_id": null, 
    "handled_event_host_id": null, 
    "event_source": "xm2cloud_agent", 
    "target_hostgroup_id": null, 
    "source_cluster_id": [
        1
    ], 
    "event_id": null, 
    "encryption": null, 
    "response_code": null, 
    "agent_uuid": "f352c284-19f3-44ef-927e-8ad2eabdae94", 
    "source_host_id": 1, 
    "target_cluster_id": null, 
    "event_name": "monitoring", 
    "source_hostgroup_id": [
        14
    ], 
    "handled_event_cluster_id": null, 
    "event_timestamp": 1524624362, 
    "source_version": "0.0.1", 
    "handled_event_hostgroup_id": null, 
    "event_uuid": "f4cca64e-04d8-403f-bbf1-83524b87c58e", 
    "event_data": "{\n    \"name\": \"df.bytes.used\", \n    \"value\": 56744947712, \n    \"tags\": {\n        \"device\": \"disk1s1\", \n        \"mount\": \"/\"\n    }\n}", 
    "handled_event_id": null
}
2018-04-25 11:01:01,889 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 141 - INFO - Acknowledging message 7
2018-04-25 11:01:01,889 - server.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/channel/rabbitmq.py - 129 - INFO - Received message # 8 from None: {
    "target_host_id": null, 
    "handled_event_host_id": null, 
    "event_source": "xm2cloud_agent", 
    "target_hostgroup_id": null, 
    "source_cluster_id": [
        1
    ], 
    "event_id": null, 
    "encryption": null, 
    "response_code": null, 
    "agent_uuid": "f352c284-19f3-44ef-927e-8ad2eabdae94", 
    "source_host_id": 1, 
    "target_cluster_id": null, 
    "event_name": "monitoring", 
    "source_hostgroup_id": [
        14
    ], 
    "handled_event_cluster_id": null, 
    "event_timestamp": 1524624362, 
    "source_version": "0.0.1", 
    "handled_event_hostgroup_id": null, 
    "event_uuid": "26649461-bf8b-4ce3-b130-d2cce79a503d", 
    "event_data": "{\n    \"name\": \"mem.memfree\", \n    \"value\": 121733120, \n    \"tags\": {}\n}", 
    "handled_event_id": null
}
2018-04-25 11:01:01,890 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 141 - INFO - Acknowledging message 8
2018-04-25 11:01:01,890 - server.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/channel/rabbitmq.py - 129 - INFO - Received message # 9 from None: {
    "target_host_id": null, 
    "handled_event_host_id": null, 
    "event_source": "xm2cloud_agent", 
    "target_hostgroup_id": null, 
    "source_cluster_id": [
        1
    ], 
    "event_id": null, 
    "encryption": null, 
    "response_code": null, 
    "agent_uuid": "f352c284-19f3-44ef-927e-8ad2eabdae94", 
    "source_host_id": 1, 
    "target_cluster_id": null, 
    "event_name": "monitoring", 
    "source_hostgroup_id": [
        14
    ], 
    "handled_event_cluster_id": null, 
    "event_timestamp": 1524624362, 
    "source_version": "0.0.1", 
    "handled_event_hostgroup_id": null, 
    "event_uuid": "9b530116-b903-4cc3-b2df-02852175e7b4", 
    "event_data": "{\n    \"name\": \"df.bytes.used.percentage\", \n    \"value\": 23.1, \n    \"tags\": {\n        \"device\": \"disk1s1\", \n        \"mount\": \"/\"\n    }\n}", 
    "handled_event_id": null
}
2018-04-25 11:01:01,891 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 141 - INFO - Acknowledging message 9
2018-04-25 11:01:01,891 - server.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/channel/rabbitmq.py - 129 - INFO - Received message # 10 from None: {
    "target_host_id": null, 
    "handled_event_host_id": null, 
    "event_source": "xm2cloud_agent", 
    "target_hostgroup_id": null, 
    "source_cluster_id": [
        1
    ], 
    "event_id": null, 
    "encryption": null, 
    "response_code": null, 
    "agent_uuid": "f352c284-19f3-44ef-927e-8ad2eabdae94", 
    "source_host_id": 1, 
    "target_cluster_id": null, 
    "event_name": "monitoring", 
    "source_hostgroup_id": [
        14
    ], 
    "handled_event_cluster_id": null, 
    "event_timestamp": 1524624362, 
    "source_version": "0.0.1", 
    "handled_event_hostgroup_id": null, 
    "event_uuid": "7ffcdfa6-53c1-4d77-a98c-b076ca785483", 
    "event_data": "{\n    \"name\": \"df.bytes.used\", \n    \"value\": 4294987776, \n    \"tags\": {\n        \"device\": \"disk1s4\", \n        \"mount\": \"/private/var/vm\"\n    }\n}", 
    "handled_event_id": null
}
2018-04-25 11:01:01,892 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 141 - INFO - Acknowledging message 10
2018-04-25 11:01:01,942 - server.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/channel/rabbitmq.py - 129 - INFO - Received message # 11 from None: {
    "target_host_id": null, 
    "handled_event_host_id": null, 
    "event_source": "xm2cloud_agent", 
    "target_hostgroup_id": null, 
    "source_cluster_id": [
        1
    ], 
    "event_id": null, 
    "encryption": null, 
    "response_code": null, 
    "agent_uuid": "f352c284-19f3-44ef-927e-8ad2eabdae94", 
    "source_host_id": 1, 
    "target_cluster_id": null, 
    "event_name": "monitoring", 
    "source_hostgroup_id": [
        14
    ], 
    "handled_event_cluster_id": null, 
    "event_timestamp": 1524624362, 
    "source_version": "0.0.1", 
    "handled_event_hostgroup_id": null, 
    "event_uuid": "e6ebf976-32ea-4e59-8078-8fcad6e6bb77", 
    "event_data": "{\n    \"name\": \"df.bytes.free\", \n    \"value\": 188967055360, \n    \"tags\": {\n        \"device\": \"disk1s4\", \n        \"mount\": \"/private/var/vm\"\n    }\n}", 
    "handled_event_id": null
}
2018-04-25 11:01:01,943 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 141 - INFO - Acknowledging message 11
2018-04-25 11:01:01,944 - server.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/channel/rabbitmq.py - 129 - INFO - Received message # 12 from None: {
    "target_host_id": null, 
    "handled_event_host_id": null, 
    "event_source": "xm2cloud_agent", 
    "target_hostgroup_id": null, 
    "source_cluster_id": [
        1
    ], 
    "event_id": null, 
    "encryption": null, 
    "response_code": null, 
    "agent_uuid": "f352c284-19f3-44ef-927e-8ad2eabdae94", 
    "source_host_id": 1, 
    "target_cluster_id": null, 
    "event_name": "monitoring", 
    "source_hostgroup_id": [
        14
    ], 
    "handled_event_cluster_id": null, 
    "event_timestamp": 1524624362, 
    "source_version": "0.0.1", 
    "handled_event_hostgroup_id": null, 
    "event_uuid": "48dd0c16-2ef6-4ce5-935d-207101da6cd6", 
    "event_data": "{\n    \"name\": \"mem.swaptotal\", \n    \"value\": 3221225472, \n    \"tags\": {}\n}", 
    "handled_event_id": null
}
2018-04-25 11:01:01,944 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 141 - INFO - Acknowledging message 12
2018-04-25 11:01:01,945 - server.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/channel/rabbitmq.py - 129 - INFO - Received message # 13 from None: {
    "target_host_id": null, 
    "handled_event_host_id": null, 
    "event_source": "xm2cloud_agent", 
    "target_hostgroup_id": null, 
    "source_cluster_id": [
        1
    ], 
    "event_id": null, 
    "encryption": null, 
    "response_code": null, 
    "agent_uuid": "f352c284-19f3-44ef-927e-8ad2eabdae94", 
    "source_host_id": 1, 
    "target_cluster_id": null, 
    "event_name": "monitoring", 
    "source_hostgroup_id": [
        14
    ], 
    "handled_event_cluster_id": null, 
    "event_timestamp": 1524624362, 
    "source_version": "0.0.1", 
    "handled_event_hostgroup_id": null, 
    "event_uuid": "4cae8acc-9f56-4b93-849e-69f822bfe2a6", 
    "event_data": "{\n    \"name\": \"mem.swapused\", \n    \"value\": 1823735808, \n    \"tags\": {}\n}", 
    "handled_event_id": null
}
2018-04-25 11:01:01,946 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 141 - INFO - Acknowledging message 13
2018-04-25 11:01:01,947 - server.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/channel/rabbitmq.py - 129 - INFO - Received message # 14 from None: {
    "target_host_id": null, 
    "handled_event_host_id": null, 
    "event_source": "xm2cloud_agent", 
    "target_hostgroup_id": null, 
    "source_cluster_id": [
        1
    ], 
    "event_id": null, 
    "encryption": null, 
    "response_code": null, 
    "agent_uuid": "f352c284-19f3-44ef-927e-8ad2eabdae94", 
    "source_host_id": 1, 
    "target_cluster_id": null, 
    "event_name": "monitoring", 
    "source_hostgroup_id": [
        14
    ], 
    "handled_event_cluster_id": null, 
    "event_timestamp": 1524624362, 
    "source_version": "0.0.1", 
    "handled_event_hostgroup_id": null, 
    "event_uuid": "9dbffd5b-c7ca-49ba-b0fd-829737cd6da2", 
    "event_data": "{\n    \"name\": \"mem.memtotal\", \n    \"value\": 8589934592, \n    \"tags\": {}\n}", 
    "handled_event_id": null
}
2018-04-25 11:01:01,947 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 141 - INFO - Acknowledging message 14
2018-04-25 11:01:01,948 - server.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/channel/rabbitmq.py - 129 - INFO - Received message # 15 from None: {
    "target_host_id": null, 
    "handled_event_host_id": null, 
    "event_source": "xm2cloud_agent", 
    "target_hostgroup_id": null, 
    "source_cluster_id": [
        1
    ], 
    "event_id": null, 
    "encryption": null, 
    "response_code": null, 
    "agent_uuid": "f352c284-19f3-44ef-927e-8ad2eabdae94", 
    "source_host_id": 1, 
    "target_cluster_id": null, 
    "event_name": "monitoring", 
    "source_hostgroup_id": [
        14
    ], 
    "handled_event_cluster_id": null, 
    "event_timestamp": 1524624362, 
    "source_version": "0.0.1", 
    "handled_event_hostgroup_id": null, 
    "event_uuid": "22d3a4d8-4d98-4553-9d98-5b0c37136dae", 
    "event_data": "{\n    \"name\": \"df.bytes.free\", \n    \"value\": 188967055360, \n    \"tags\": {\n        \"device\": \"disk1s1\", \n        \"mount\": \"/\"\n    }\n}", 
    "handled_event_id": null
}
2018-04-25 11:01:01,948 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 141 - INFO - Acknowledging message 15
2018-04-25 11:01:01,948 - server.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/channel/rabbitmq.py - 129 - INFO - Received message # 16 from None: {
    "target_host_id": null, 
    "handled_event_host_id": null, 
    "event_source": "xm2cloud_agent", 
    "target_hostgroup_id": null, 
    "source_cluster_id": [
        1
    ], 
    "event_id": null, 
    "encryption": null, 
    "response_code": null, 
    "agent_uuid": "f352c284-19f3-44ef-927e-8ad2eabdae94", 
    "source_host_id": 1, 
    "target_cluster_id": null, 
    "event_name": "monitoring", 
    "source_hostgroup_id": [
        14
    ], 
    "handled_event_cluster_id": null, 
    "event_timestamp": 1524624362, 
    "source_version": "0.0.1", 
    "handled_event_hostgroup_id": null, 
    "event_uuid": "740ec86c-e19e-49ef-b8d8-8c879cff2262", 
    "event_data": "{\n    \"name\": \"mem.memused.percentage\", \n    \"value\": 73.6, \n    \"tags\": {}\n}", 
    "handled_event_id": null
}
2018-04-25 11:01:01,949 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 141 - INFO - Acknowledging message 16
2018-04-25 11:01:01,949 - server.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/channel/rabbitmq.py - 129 - INFO - Received message # 17 from None: {
    "target_host_id": null, 
    "handled_event_host_id": null, 
    "event_source": "xm2cloud_agent", 
    "target_hostgroup_id": null, 
    "source_cluster_id": [
        1
    ], 
    "event_id": null, 
    "encryption": null, 
    "response_code": null, 
    "agent_uuid": "f352c284-19f3-44ef-927e-8ad2eabdae94", 
    "source_host_id": 1, 
    "target_cluster_id": null, 
    "event_name": "monitoring", 
    "source_hostgroup_id": [
        14
    ], 
    "handled_event_cluster_id": null, 
    "event_timestamp": 1524624362, 
    "source_version": "0.0.1", 
    "handled_event_hostgroup_id": null, 
    "event_uuid": "7280bf24-4d2f-4941-99d3-38d886b3af2f", 
    "event_data": "{\n    \"name\": \"mem.memused\", \n    \"value\": 7271620608, \n    \"tags\": {}\n}", 
    "handled_event_id": null
}
2018-04-25 11:01:01,950 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 141 - INFO - Acknowledging message 17
2018-04-25 11:01:01,950 - server.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/channel/rabbitmq.py - 129 - INFO - Received message # 18 from None: {
    "target_host_id": null, 
    "handled_event_host_id": null, 
    "event_source": "xm2cloud_agent", 
    "target_hostgroup_id": null, 
    "source_cluster_id": [
        1
    ], 
    "event_id": null, 
    "encryption": null, 
    "response_code": null, 
    "agent_uuid": "f352c284-19f3-44ef-927e-8ad2eabdae94", 
    "source_host_id": 1, 
    "target_cluster_id": null, 
    "event_name": "monitoring", 
    "source_hostgroup_id": [
        14
    ], 
    "handled_event_cluster_id": null, 
    "event_timestamp": 1524624362, 
    "source_version": "0.0.1", 
    "handled_event_hostgroup_id": null, 
    "event_uuid": "a81903b3-4a84-4a86-98d3-5585bef47236", 
    "event_data": "{\n    \"name\": \"df.bytes.used.percentage\", \n    \"value\": 2.2, \n    \"tags\": {\n        \"device\": \"disk1s4\", \n        \"mount\": \"/private/var/vm\"\n    }\n}", 
    "handled_event_id": null
}
2018-04-25 11:01:01,950 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 141 - INFO - Acknowledging message 18
2018-04-25 11:01:01,951 - server.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/channel/rabbitmq.py - 129 - INFO - Received message # 19 from None: {
    "target_host_id": null, 
    "handled_event_host_id": null, 
    "event_source": "xm2cloud_agent", 
    "target_hostgroup_id": null, 
    "source_cluster_id": [
        1
    ], 
    "event_id": null, 
    "encryption": null, 
    "response_code": null, 
    "agent_uuid": "f352c284-19f3-44ef-927e-8ad2eabdae94", 
    "source_host_id": 1, 
    "target_cluster_id": null, 
    "event_name": "monitoring", 
    "source_hostgroup_id": [
        14
    ], 
    "handled_event_cluster_id": null, 
    "event_timestamp": 1524624362, 
    "source_version": "0.0.1", 
    "handled_event_hostgroup_id": null, 
    "event_uuid": "42a704d0-e8c1-40c6-96af-825116b67efb", 
    "event_data": "{\n    \"name\": \"mem.swapused.percentage\", \n    \"value\": 56.6, \n    \"tags\": {}\n}", 
    "handled_event_id": null
}
2018-04-25 11:01:01,951 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 141 - INFO - Acknowledging message 19
2018-04-25 11:01:01,952 - server.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/channel/rabbitmq.py - 129 - INFO - Received message # 20 from None: {
    "target_host_id": null, 
    "handled_event_host_id": null, 
    "event_source": "xm2cloud_agent", 
    "target_hostgroup_id": null, 
    "source_cluster_id": [
        1
    ], 
    "event_id": null, 
    "encryption": null, 
    "response_code": null, 
    "agent_uuid": "f352c284-19f3-44ef-927e-8ad2eabdae94", 
    "source_host_id": 1, 
    "target_cluster_id": null, 
    "event_name": "monitoring", 
    "source_hostgroup_id": [
        14
    ], 
    "handled_event_cluster_id": null, 
    "event_timestamp": 1524624362, 
    "source_version": "0.0.1", 
    "handled_event_hostgroup_id": null, 
    "event_uuid": "d60b541a-e09f-445b-878c-a68fb2f96416", 
    "event_data": "{\n    \"name\": \"mem.swapfree\", \n    \"value\": 1397489664, \n    \"tags\": {}\n}", 
    "handled_event_id": null
}
2018-04-25 11:01:01,952 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 141 - INFO - Acknowledging message 20
2018-04-25 11:01:01,953 - server.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/channel/rabbitmq.py - 129 - INFO - Received message # 21 from None: {
    "target_host_id": null, 
    "handled_event_host_id": null, 
    "event_source": "xm2cloud_agent", 
    "target_hostgroup_id": null, 
    "source_cluster_id": [
        1
    ], 
    "event_id": null, 
    "encryption": null, 
    "response_code": null, 
    "agent_uuid": "f352c284-19f3-44ef-927e-8ad2eabdae94", 
    "source_host_id": 1, 
    "target_cluster_id": null, 
    "event_name": "monitoring", 
    "source_hostgroup_id": [
        14
    ], 
    "handled_event_cluster_id": null, 
    "event_timestamp": 1524624362, 
    "source_version": "0.0.1", 
    "handled_event_hostgroup_id": null, 
    "event_uuid": "f4cca64e-04d8-403f-bbf1-83524b87c58e", 
    "event_data": "{\n    \"name\": \"df.bytes.used\", \n    \"value\": 56744947712, \n    \"tags\": {\n        \"device\": \"disk1s1\", \n        \"mount\": \"/\"\n    }\n}", 
    "handled_event_id": null
}
2018-04-25 11:01:01,953 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 141 - INFO - Acknowledging message 21
2018-04-25 11:01:01,953 - server.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/channel/rabbitmq.py - 129 - INFO - Received message # 22 from None: {
    "target_host_id": null, 
    "handled_event_host_id": null, 
    "event_source": "xm2cloud_agent", 
    "target_hostgroup_id": null, 
    "source_cluster_id": [
        1
    ], 
    "event_id": null, 
    "encryption": null, 
    "response_code": null, 
    "agent_uuid": "f352c284-19f3-44ef-927e-8ad2eabdae94", 
    "source_host_id": 1, 
    "target_cluster_id": null, 
    "event_name": "monitoring", 
    "source_hostgroup_id": [
        14
    ], 
    "handled_event_cluster_id": null, 
    "event_timestamp": 1524624362, 
    "source_version": "0.0.1", 
    "handled_event_hostgroup_id": null, 
    "event_uuid": "26649461-bf8b-4ce3-b130-d2cce79a503d", 
    "event_data": "{\n    \"name\": \"mem.memfree\", \n    \"value\": 121733120, \n    \"tags\": {}\n}", 
    "handled_event_id": null
}
2018-04-25 11:01:01,954 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 141 - INFO - Acknowledging message 22
2018-04-25 11:01:01,954 - server.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/channel/rabbitmq.py - 129 - INFO - Received message # 23 from None: {
    "target_host_id": null, 
    "handled_event_host_id": null, 
    "event_source": "xm2cloud_agent", 
    "target_hostgroup_id": null, 
    "source_cluster_id": [
        1
    ], 
    "event_id": null, 
    "encryption": null, 
    "response_code": null, 
    "agent_uuid": "f352c284-19f3-44ef-927e-8ad2eabdae94", 
    "source_host_id": 1, 
    "target_cluster_id": null, 
    "event_name": "monitoring", 
    "source_hostgroup_id": [
        14
    ], 
    "handled_event_cluster_id": null, 
    "event_timestamp": 1524624362, 
    "source_version": "0.0.1", 
    "handled_event_hostgroup_id": null, 
    "event_uuid": "9b530116-b903-4cc3-b2df-02852175e7b4", 
    "event_data": "{\n    \"name\": \"df.bytes.used.percentage\", \n    \"value\": 23.1, \n    \"tags\": {\n        \"device\": \"disk1s1\", \n        \"mount\": \"/\"\n    }\n}", 
    "handled_event_id": null
}
2018-04-25 11:01:01,955 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 141 - INFO - Acknowledging message 23
2018-04-25 11:01:01,955 - server.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/channel/rabbitmq.py - 129 - INFO - Received message # 24 from None: {
    "target_host_id": null, 
    "handled_event_host_id": null, 
    "event_source": "xm2cloud_agent", 
    "target_hostgroup_id": null, 
    "source_cluster_id": [
        1
    ], 
    "event_id": null, 
    "encryption": null, 
    "response_code": null, 
    "agent_uuid": "f352c284-19f3-44ef-927e-8ad2eabdae94", 
    "source_host_id": 1, 
    "target_cluster_id": null, 
    "event_name": "monitoring", 
    "source_hostgroup_id": [
        14
    ], 
    "handled_event_cluster_id": null, 
    "event_timestamp": 1524624362, 
    "source_version": "0.0.1", 
    "handled_event_hostgroup_id": null, 
    "event_uuid": "7ffcdfa6-53c1-4d77-a98c-b076ca785483", 
    "event_data": "{\n    \"name\": \"df.bytes.used\", \n    \"value\": 4294987776, \n    \"tags\": {\n        \"device\": \"disk1s4\", \n        \"mount\": \"/private/var/vm\"\n    }\n}", 
    "handled_event_id": null
}
2018-04-25 11:01:01,956 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 141 - INFO - Acknowledging message 24
2018-04-25 11:01:01,956 - server.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/channel/rabbitmq.py - 129 - INFO - Received message # 25 from None: {
    "target_host_id": null, 
    "handled_event_host_id": null, 
    "event_source": "xm2cloud_agent", 
    "target_hostgroup_id": null, 
    "source_cluster_id": [
        1
    ], 
    "event_id": null, 
    "encryption": null, 
    "response_code": null, 
    "agent_uuid": "f352c284-19f3-44ef-927e-8ad2eabdae94", 
    "source_host_id": 1, 
    "target_cluster_id": null, 
    "event_name": "monitoring", 
    "source_hostgroup_id": [
        14
    ], 
    "handled_event_cluster_id": null, 
    "event_timestamp": 1524624362, 
    "source_version": "0.0.1", 
    "handled_event_hostgroup_id": null, 
    "event_uuid": "e6ebf976-32ea-4e59-8078-8fcad6e6bb77", 
    "event_data": "{\n    \"name\": \"df.bytes.free\", \n    \"value\": 188967055360, \n    \"tags\": {\n        \"device\": \"disk1s4\", \n        \"mount\": \"/private/var/vm\"\n    }\n}", 
    "handled_event_id": null
}
2018-04-25 11:01:01,957 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 141 - INFO - Acknowledging message 25
2018-04-25 11:01:01,957 - server.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/channel/rabbitmq.py - 129 - INFO - Received message # 26 from None: {
    "target_host_id": null, 
    "handled_event_host_id": null, 
    "event_source": "xm2cloud_agent", 
    "target_hostgroup_id": null, 
    "source_cluster_id": [
        1
    ], 
    "event_id": null, 
    "encryption": null, 
    "response_code": null, 
    "agent_uuid": "f352c284-19f3-44ef-927e-8ad2eabdae94", 
    "source_host_id": 1, 
    "target_cluster_id": null, 
    "event_name": "monitoring", 
    "source_hostgroup_id": [
        14
    ], 
    "handled_event_cluster_id": null, 
    "event_timestamp": 1524624362, 
    "source_version": "0.0.1", 
    "handled_event_hostgroup_id": null, 
    "event_uuid": "48dd0c16-2ef6-4ce5-935d-207101da6cd6", 
    "event_data": "{\n    \"name\": \"mem.swaptotal\", \n    \"value\": 3221225472, \n    \"tags\": {}\n}", 
    "handled_event_id": null
}
2018-04-25 11:01:01,958 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 141 - INFO - Acknowledging message 26
2018-04-25 11:01:01,958 - server.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/channel/rabbitmq.py - 129 - INFO - Received message # 27 from None: {
    "target_host_id": null, 
    "handled_event_host_id": null, 
    "event_source": "xm2cloud_agent", 
    "target_hostgroup_id": null, 
    "source_cluster_id": [
        1
    ], 
    "event_id": null, 
    "encryption": null, 
    "response_code": null, 
    "agent_uuid": "f352c284-19f3-44ef-927e-8ad2eabdae94", 
    "source_host_id": 1, 
    "target_cluster_id": null, 
    "event_name": "monitoring", 
    "source_hostgroup_id": [
        14
    ], 
    "handled_event_cluster_id": null, 
    "event_timestamp": 1524624362, 
    "source_version": "0.0.1", 
    "handled_event_hostgroup_id": null, 
    "event_uuid": "4cae8acc-9f56-4b93-849e-69f822bfe2a6", 
    "event_data": "{\n    \"name\": \"mem.swapused\", \n    \"value\": 1823735808, \n    \"tags\": {}\n}", 
    "handled_event_id": null
}
2018-04-25 11:01:01,958 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 141 - INFO - Acknowledging message 27
2018-04-25 11:01:01,959 - server.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/channel/rabbitmq.py - 129 - INFO - Received message # 28 from None: {
    "target_host_id": null, 
    "handled_event_host_id": null, 
    "event_source": "xm2cloud_agent", 
    "target_hostgroup_id": null, 
    "source_cluster_id": [
        1
    ], 
    "event_id": null, 
    "encryption": null, 
    "response_code": null, 
    "agent_uuid": "f352c284-19f3-44ef-927e-8ad2eabdae94", 
    "source_host_id": 1, 
    "target_cluster_id": null, 
    "event_name": "monitoring", 
    "source_hostgroup_id": [
        14
    ], 
    "handled_event_cluster_id": null, 
    "event_timestamp": 1524624362, 
    "source_version": "0.0.1", 
    "handled_event_hostgroup_id": null, 
    "event_uuid": "9dbffd5b-c7ca-49ba-b0fd-829737cd6da2", 
    "event_data": "{\n    \"name\": \"mem.memtotal\", \n    \"value\": 8589934592, \n    \"tags\": {}\n}", 
    "handled_event_id": null
}
2018-04-25 11:01:01,959 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 141 - INFO - Acknowledging message 28
2018-04-25 11:01:01,959 - server.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/channel/rabbitmq.py - 129 - INFO - Received message # 29 from None: {
    "target_host_id": null, 
    "handled_event_host_id": null, 
    "event_source": "xm2cloud_agent", 
    "target_hostgroup_id": null, 
    "source_cluster_id": [
        1
    ], 
    "event_id": null, 
    "encryption": null, 
    "response_code": null, 
    "agent_uuid": "f352c284-19f3-44ef-927e-8ad2eabdae94", 
    "source_host_id": 1, 
    "target_cluster_id": null, 
    "event_name": "monitoring", 
    "source_hostgroup_id": [
        14
    ], 
    "handled_event_cluster_id": null, 
    "event_timestamp": 1524624362, 
    "source_version": "0.0.1", 
    "handled_event_hostgroup_id": null, 
    "event_uuid": "22d3a4d8-4d98-4553-9d98-5b0c37136dae", 
    "event_data": "{\n    \"name\": \"df.bytes.free\", \n    \"value\": 188967055360, \n    \"tags\": {\n        \"device\": \"disk1s1\", \n        \"mount\": \"/\"\n    }\n}", 
    "handled_event_id": null
}
2018-04-25 11:01:01,960 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 141 - INFO - Acknowledging message 29
2018-04-25 11:01:01,960 - server.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/channel/rabbitmq.py - 129 - INFO - Received message # 30 from None: {
    "target_host_id": null, 
    "handled_event_host_id": null, 
    "event_source": "xm2cloud_agent", 
    "target_hostgroup_id": null, 
    "source_cluster_id": [
        1
    ], 
    "event_id": null, 
    "encryption": null, 
    "response_code": null, 
    "agent_uuid": "f352c284-19f3-44ef-927e-8ad2eabdae94", 
    "source_host_id": 1, 
    "target_cluster_id": null, 
    "event_name": "monitoring", 
    "source_hostgroup_id": [
        14
    ], 
    "handled_event_cluster_id": null, 
    "event_timestamp": 1524624362, 
    "source_version": "0.0.1", 
    "handled_event_hostgroup_id": null, 
    "event_uuid": "740ec86c-e19e-49ef-b8d8-8c879cff2262", 
    "event_data": "{\n    \"name\": \"mem.memused.percentage\", \n    \"value\": 73.6, \n    \"tags\": {}\n}", 
    "handled_event_id": null
}
2018-04-25 11:01:01,961 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 141 - INFO - Acknowledging message 30
2018-04-25 11:01:01,961 - server.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/channel/rabbitmq.py - 129 - INFO - Received message # 31 from None: {
    "target_host_id": null, 
    "handled_event_host_id": null, 
    "event_source": "xm2cloud_agent", 
    "target_hostgroup_id": null, 
    "source_cluster_id": [
        1
    ], 
    "event_id": null, 
    "encryption": null, 
    "response_code": null, 
    "agent_uuid": "f352c284-19f3-44ef-927e-8ad2eabdae94", 
    "source_host_id": 1, 
    "target_cluster_id": null, 
    "event_name": "monitoring", 
    "source_hostgroup_id": [
        14
    ], 
    "handled_event_cluster_id": null, 
    "event_timestamp": 1524624362, 
    "source_version": "0.0.1", 
    "handled_event_hostgroup_id": null, 
    "event_uuid": "7280bf24-4d2f-4941-99d3-38d886b3af2f", 
    "event_data": "{\n    \"name\": \"mem.memused\", \n    \"value\": 7271620608, \n    \"tags\": {}\n}", 
    "handled_event_id": null
}
2018-04-25 11:01:01,961 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 141 - INFO - Acknowledging message 31
2018-04-25 11:01:01,962 - server.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/channel/rabbitmq.py - 129 - INFO - Received message # 32 from None: {
    "target_host_id": null, 
    "handled_event_host_id": null, 
    "event_source": "xm2cloud_agent", 
    "target_hostgroup_id": null, 
    "source_cluster_id": [
        1
    ], 
    "event_id": null, 
    "encryption": null, 
    "response_code": null, 
    "agent_uuid": "f352c284-19f3-44ef-927e-8ad2eabdae94", 
    "source_host_id": 1, 
    "target_cluster_id": null, 
    "event_name": "monitoring", 
    "source_hostgroup_id": [
        14
    ], 
    "handled_event_cluster_id": null, 
    "event_timestamp": 1524624362, 
    "source_version": "0.0.1", 
    "handled_event_hostgroup_id": null, 
    "event_uuid": "a81903b3-4a84-4a86-98d3-5585bef47236", 
    "event_data": "{\n    \"name\": \"df.bytes.used.percentage\", \n    \"value\": 2.2, \n    \"tags\": {\n        \"device\": \"disk1s4\", \n        \"mount\": \"/private/var/vm\"\n    }\n}", 
    "handled_event_id": null
}
2018-04-25 11:01:01,962 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 141 - INFO - Acknowledging message 32
2018-04-25 11:01:01,962 - server.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/channel/rabbitmq.py - 129 - INFO - Received message # 33 from None: {
    "target_host_id": null, 
    "handled_event_host_id": null, 
    "event_source": "xm2cloud_agent", 
    "target_hostgroup_id": null, 
    "source_cluster_id": [
        1
    ], 
    "event_id": null, 
    "encryption": null, 
    "response_code": null, 
    "agent_uuid": "f352c284-19f3-44ef-927e-8ad2eabdae94", 
    "source_host_id": 1, 
    "target_cluster_id": null, 
    "event_name": "monitoring", 
    "source_hostgroup_id": [
        14
    ], 
    "handled_event_cluster_id": null, 
    "event_timestamp": 1524624362, 
    "source_version": "0.0.1", 
    "handled_event_hostgroup_id": null, 
    "event_uuid": "42a704d0-e8c1-40c6-96af-825116b67efb", 
    "event_data": "{\n    \"name\": \"mem.swapused.percentage\", \n    \"value\": 56.6, \n    \"tags\": {}\n}", 
    "handled_event_id": null
}
2018-04-25 11:01:01,963 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 141 - INFO - Acknowledging message 33
2018-04-25 11:01:01,964 - server.handler.channel.rabbitmq - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/channel/rabbitmq.py - 129 - INFO - Received message # 34 from None: {
    "target_host_id": null, 
    "handled_event_host_id": null, 
    "event_source": "xm2cloud_agent", 
    "target_hostgroup_id": null, 
    "source_cluster_id": [
        1
    ], 
    "event_id": null, 
    "encryption": null, 
    "response_code": null, 
    "agent_uuid": "f352c284-19f3-44ef-927e-8ad2eabdae94", 
    "source_host_id": 1, 
    "target_cluster_id": null, 
    "event_name": "monitoring", 
    "source_hostgroup_id": [
        14
    ], 
    "handled_event_cluster_id": null, 
    "event_timestamp": 1524624362, 
    "source_version": "0.0.1", 
    "handled_event_hostgroup_id": null, 
    "event_uuid": "d60b541a-e09f-445b-878c-a68fb2f96416", 
    "event_data": "{\n    \"name\": \"mem.swapfree\", \n    \"value\": 1397489664, \n    \"tags\": {}\n}", 
    "handled_event_id": null
}
2018-04-25 11:01:01,964 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 141 - INFO - Acknowledging message 34
2018-04-25 11:01:01,965 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 113 - INFO - Binding event_up_exchange to event_up_queue with event_engine.rpc
2018-04-25 11:01:01,979 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 123 - INFO - Binding event_down_exchange to event_down_queue with event_engine.rpc
2018-04-25 11:01:02,050 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 128 - INFO - Queue bound
2018-04-25 11:01:02,050 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 132 - INFO - Issuing consumer related RPC commands
2018-04-25 11:01:02,050 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 137 - INFO - Issuing Confirm.Select RPC command
2018-04-25 11:01:02,051 - pika.callback - /Library/Python/2.7/site-packages/pika/callback.py - 157 - WARNING - Duplicate callback found for "1:Basic.Ack"
2018-04-25 11:01:02,051 - pika.callback - /Library/Python/2.7/site-packages/pika/callback.py - 157 - WARNING - Duplicate callback found for "1:Basic.Nack"
2018-04-25 11:01:02,051 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:02,059 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 118 - INFO - Queue bound
2018-04-25 11:01:02,060 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 122 - INFO - Issuing consumer related RPC commands
2018-04-25 11:01:02,060 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 128 - INFO - Adding consumer cancellation callback
2018-04-25 11:01:02,060 - pika.callback - /Library/Python/2.7/site-packages/pika/callback.py - 157 - WARNING - Duplicate callback found for "1:Basic.Cancel"
2018-04-25 11:01:02,447 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 92 - INFO - Start handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,447 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 92 - INFO - Start handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,449 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 92 - INFO - Start handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,450 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 92 - INFO - Start handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,451 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 92 - INFO - Start handle outer event: heartbeat (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,453 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 92 - INFO - Start handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,455 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 92 - INFO - Start handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,456 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 92 - INFO - Start handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,457 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 92 - INFO - Start handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,458 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 92 - INFO - Start handle outer event: heartbeat (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,460 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 92 - INFO - Start handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,461 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 92 - INFO - Start handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,463 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 92 - INFO - Start handle outer event: heartbeat (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,463 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 92 - INFO - Start handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,465 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 92 - INFO - Start handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,465 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 92 - INFO - Start handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,466 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 92 - INFO - Start handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,468 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 92 - INFO - Start handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,468 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 92 - INFO - Start handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,470 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 92 - INFO - Start handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,471 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 92 - INFO - Start handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,472 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 92 - INFO - Start handle outer event: heartbeat (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,473 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 92 - INFO - Start handle outer event: heartbeat (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,475 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 92 - INFO - Start handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,476 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 92 - INFO - Start handle outer event: heartbeat (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,477 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 92 - INFO - Start handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,478 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 92 - INFO - Start handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,479 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 92 - INFO - Start handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,479 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 92 - INFO - Start handle outer event: heartbeat (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,479 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 92 - INFO - Start handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,481 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 92 - INFO - Start handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,483 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 92 - INFO - Start handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,484 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 92 - INFO - Start handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,485 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 92 - INFO - Start handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,487 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 92 - INFO - Start handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,488 - server.core.engine - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/engine.py - 139 - INFO - Events ready, next scheduled at 2018-04-25 11:01:03
2018-04-25 11:01:02,640 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 103 - INFO - Finish handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,642 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 103 - INFO - Finish handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,647 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 103 - INFO - Finish handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,650 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 103 - INFO - Finish handle outer event: heartbeat (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,657 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 103 - INFO - Finish handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,657 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 103 - INFO - Finish handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,658 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 103 - INFO - Finish handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,658 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 103 - INFO - Finish handle outer event: heartbeat (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,660 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 103 - INFO - Finish handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,662 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 103 - INFO - Finish handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,662 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 103 - INFO - Finish handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,662 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 103 - INFO - Finish handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,662 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 103 - INFO - Finish handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,662 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 103 - INFO - Finish handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,663 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 103 - INFO - Finish handle outer event: heartbeat (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,663 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 103 - INFO - Finish handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,663 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 103 - INFO - Finish handle outer event: heartbeat (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,664 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 103 - INFO - Finish handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,664 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 103 - INFO - Finish handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,666 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 103 - INFO - Finish handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,666 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 103 - INFO - Finish handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,666 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 103 - INFO - Finish handle outer event: heartbeat (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,668 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 103 - INFO - Finish handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,672 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 103 - INFO - Finish handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,673 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 103 - INFO - Finish handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,673 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 103 - INFO - Finish handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,683 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 103 - INFO - Finish handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,683 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 103 - INFO - Finish handle outer event: heartbeat (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,684 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 103 - INFO - Finish handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,684 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 103 - INFO - Finish handle outer event: heartbeat (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,700 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 103 - INFO - Finish handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,719 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 103 - INFO - Finish handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,719 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 103 - INFO - Finish handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,723 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 103 - INFO - Finish handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,724 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 103 - INFO - Finish handle outer event: monitoring (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:02,776 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:03,053 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:03,490 - server.core.engine - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/engine.py - 126 - INFO - No events ready, next scheduled at 2018-04-25 11:01:04
2018-04-25 11:01:03,778 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:04,056 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:04,446 - server.core.heatbeat - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/heatbeat.py - 76 - INFO - Events ready, next scheduled at 2018-04-25 11:01:07
2018-04-25 11:01:04,447 - server.core.channel - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/channel.py - 107 - INFO - Events ready, next scheduled at 2018-04-25 11:01:05
2018-04-25 11:01:04,492 - server.core.engine - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/engine.py - 139 - INFO - Events ready, next scheduled at 2018-04-25 11:01:05
2018-04-25 11:01:04,493 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 92 - INFO - Start handle outer event: heartbeat (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:04,736 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 103 - INFO - Finish handle outer event: heartbeat (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:04,781 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:05,057 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:05,495 - server.core.engine - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/engine.py - 126 - INFO - No events ready, next scheduled at 2018-04-25 11:01:06
2018-04-25 11:01:05,784 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:06,060 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:06,497 - server.core.engine - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/engine.py - 126 - INFO - No events ready, next scheduled at 2018-04-25 11:01:07
2018-04-25 11:01:06,785 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:07,064 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:07,449 - server.core.channel - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/channel.py - 107 - INFO - Events ready, next scheduled at 2018-04-25 11:01:08
2018-04-25 11:01:07,452 - server.core.heatbeat - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/heatbeat.py - 76 - INFO - Events ready, next scheduled at 2018-04-25 11:01:10
2018-04-25 11:01:07,499 - server.core.engine - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/engine.py - 139 - INFO - Events ready, next scheduled at 2018-04-25 11:01:08
2018-04-25 11:01:07,499 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 92 - INFO - Start handle outer event: heartbeat (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:07,695 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 103 - INFO - Finish handle outer event: heartbeat (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:07,786 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:08,066 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:08,501 - server.core.engine - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/engine.py - 126 - INFO - No events ready, next scheduled at 2018-04-25 11:01:09
2018-04-25 11:01:08,790 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:09,067 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:09,504 - server.core.engine - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/engine.py - 126 - INFO - No events ready, next scheduled at 2018-04-25 11:01:10
2018-04-25 11:01:09,792 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:10,071 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:10,452 - server.core.channel - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/channel.py - 107 - INFO - Events ready, next scheduled at 2018-04-25 11:01:11
2018-04-25 11:01:10,454 - server.core.heatbeat - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/heatbeat.py - 76 - INFO - Events ready, next scheduled at 2018-04-25 11:01:13
2018-04-25 11:01:10,508 - server.core.engine - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/engine.py - 139 - INFO - Events ready, next scheduled at 2018-04-25 11:01:11
2018-04-25 11:01:10,508 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 92 - INFO - Start handle outer event: heartbeat (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:10,693 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 103 - INFO - Finish handle outer event: heartbeat (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:10,795 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:11,072 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:11,510 - server.core.engine - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/engine.py - 126 - INFO - No events ready, next scheduled at 2018-04-25 11:01:12
2018-04-25 11:01:11,797 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:12,077 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:12,512 - server.core.engine - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/engine.py - 126 - INFO - No events ready, next scheduled at 2018-04-25 11:01:13
2018-04-25 11:01:12,799 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:13,082 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:13,453 - server.core.channel - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/channel.py - 107 - INFO - Events ready, next scheduled at 2018-04-25 11:01:14
2018-04-25 11:01:13,457 - server.core.heatbeat - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/heatbeat.py - 76 - INFO - Events ready, next scheduled at 2018-04-25 11:01:16
2018-04-25 11:01:13,515 - server.core.engine - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/engine.py - 139 - INFO - Events ready, next scheduled at 2018-04-25 11:01:14
2018-04-25 11:01:13,516 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 92 - INFO - Start handle outer event: heartbeat (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:13,684 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 103 - INFO - Finish handle outer event: heartbeat (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:13,804 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:14,083 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:14,517 - server.core.engine - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/engine.py - 126 - INFO - No events ready, next scheduled at 2018-04-25 11:01:15
2018-04-25 11:01:14,805 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:15,086 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:15,518 - server.core.engine - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/engine.py - 126 - INFO - No events ready, next scheduled at 2018-04-25 11:01:16
2018-04-25 11:01:15,810 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:16,093 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:16,455 - server.core.channel - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/channel.py - 107 - INFO - Events ready, next scheduled at 2018-04-25 11:01:17
2018-04-25 11:01:16,462 - server.core.heatbeat - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/heatbeat.py - 76 - INFO - Events ready, next scheduled at 2018-04-25 11:01:19
2018-04-25 11:01:16,521 - server.core.engine - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/engine.py - 139 - INFO - Events ready, next scheduled at 2018-04-25 11:01:17
2018-04-25 11:01:16,521 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 92 - INFO - Start handle outer event: heartbeat (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:16,717 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 103 - INFO - Finish handle outer event: heartbeat (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:16,814 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:17,095 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:17,523 - server.core.engine - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/engine.py - 126 - INFO - No events ready, next scheduled at 2018-04-25 11:01:18
2018-04-25 11:01:17,817 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:18,096 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:18,526 - server.core.engine - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/engine.py - 126 - INFO - No events ready, next scheduled at 2018-04-25 11:01:19
2018-04-25 11:01:18,823 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:19,099 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:19,457 - server.core.channel - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/channel.py - 107 - INFO - Events ready, next scheduled at 2018-04-25 11:01:20
2018-04-25 11:01:19,465 - server.core.heatbeat - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/heatbeat.py - 76 - INFO - Events ready, next scheduled at 2018-04-25 11:01:22
2018-04-25 11:01:19,527 - server.core.engine - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/engine.py - 139 - INFO - Events ready, next scheduled at 2018-04-25 11:01:20
2018-04-25 11:01:19,528 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 92 - INFO - Start handle outer event: heartbeat (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:19,686 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 103 - INFO - Finish handle outer event: heartbeat (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:19,828 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:20,101 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:20,529 - server.core.engine - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/engine.py - 126 - INFO - No events ready, next scheduled at 2018-04-25 11:01:21
2018-04-25 11:01:20,834 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:21,103 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:21,531 - server.core.engine - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/engine.py - 126 - INFO - No events ready, next scheduled at 2018-04-25 11:01:22
2018-04-25 11:01:21,835 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:22,106 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:22,458 - server.core.channel - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/channel.py - 107 - INFO - Events ready, next scheduled at 2018-04-25 11:01:23
2018-04-25 11:01:22,468 - server.core.heatbeat - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/heatbeat.py - 76 - INFO - Events ready, next scheduled at 2018-04-25 11:01:25
2018-04-25 11:01:22,533 - server.core.engine - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/engine.py - 139 - INFO - Events ready, next scheduled at 2018-04-25 11:01:23
2018-04-25 11:01:22,534 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 92 - INFO - Start handle outer event: heartbeat (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:22,757 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 103 - INFO - Finish handle outer event: heartbeat (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:22,836 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:23,111 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:23,535 - server.core.engine - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/engine.py - 126 - INFO - No events ready, next scheduled at 2018-04-25 11:01:24
2018-04-25 11:01:23,840 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:24,117 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:24,538 - server.core.engine - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/engine.py - 126 - INFO - No events ready, next scheduled at 2018-04-25 11:01:25
2018-04-25 11:01:24,841 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:25,121 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:01:25,460 - server.core.channel - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/channel.py - 107 - INFO - Events ready, next scheduled at 2018-04-25 11:01:26
2018-04-25 11:01:25,470 - server.core.heatbeat - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/heatbeat.py - 76 - INFO - Events ready, next scheduled at 2018-04-25 11:01:28
2018-04-25 11:01:25,540 - server.core.engine - /Users/manmanli/xm-gits/xm2cloud_engine/server/core/engine.py - 139 - INFO - Events ready, next scheduled at 2018-04-25 11:01:26
2018-04-25 11:01:25,541 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 92 - INFO - Start handle outer event: heartbeat (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:25,695 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 103 - INFO - Finish handle outer event: heartbeat (host: None, hostgroup: None, cluster: None)
2018-04-25 11:01:25,843 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 164 - INFO - Scheduling next message for 1.0 seconds
2018-04-25 11:03:01,742 - server.handler.engine.baseengine - /Users/manmanli/xm-gits/xm2cloud_engine/server/handler/engine/baseengine.py - 92 - INFO - Start handle outer event: heartbeat (host: None, hostgroup: None, cluster: None)
^CChannel process(93387) got GracefulExitException.
Heartbeat process(93388) got GracefulExitException.
Engine process(93386) got GracefulExitException.
Main process(93384) got GracefulExitException.
2018-04-25 11:03:01,745 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 181 - INFO - Stopping
2018-04-25 11:03:01,745 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 172 - INFO - Closing the channel
2018-04-25 11:03:01,746 - pika.channel - /Library/Python/2.7/site-packages/pika/channel.py - 529 - INFO - Closing channel (0): 'Normal shutdown' on <Channel number=1 OPEN conn=<SelectConnection OPEN socket=('192.168.3.239', 50879)->('120.131.14.225', 5672) params=<ConnectionParameters host=ops.xxoo.com port=5672 virtual_host=/event_engine ssl=False>>>
2018-04-25 11:03:01,747 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 189 - INFO - Closing connection
2018-04-25 11:03:01,747 - pika.connection - /Library/Python/2.7/site-packages/pika/connection.py - 1147 - INFO - Closing connection (200): Normal shutdown
2018-04-25 11:03:01,747 - pika.connection - /Library/Python/2.7/site-packages/pika/connection.py - 1159 - INFO - Connection.close is waiting for 1 channels to close: <SelectConnection CLOSING socket=('192.168.3.239', 50879)->('120.131.14.225', 5672) params=<ConnectionParameters host=ops.xxoo.com port=5672 virtual_host=/event_engine ssl=False>>
2018-04-25 11:03:01,748 - server.util.amqp.sender - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/sender.py - 186 - INFO - Stopped
2018-04-25 11:03:01,748 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 162 - INFO - Stopping
2018-04-25 11:03:01,748 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 146 - INFO - Sending a Basic.Cancel RPC command to RabbitMQ
2018-04-25 11:03:01,749 - server.util.amqp.receiver - /Users/manmanli/xm-gits/xm2cloud_engine/server/util/amqp/receiver.py - 166 - INFO - Stopped
```
