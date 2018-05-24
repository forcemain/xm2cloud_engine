### For Arch:
#### xm2cloud_engine is a powerful and graceful engine component for xm2cloud devops framework.

### For Metric (LifeCycle: 1h):

```
# Heartbeat(hmset):
xm2cloud_agent::heartbeat::f352c284-19f3-44ef-927e-8ad2eabdae94
{
    name: ...,
    version: ...,
    timestamp: ...
}
xm2cloud_engine::heartbeat::0599f2ea-d113-4970-873d-f9ad154ae22c
{
    name: ...,
    version: ...,
    timestamp: ...,
}

# Timeseries(zadd):
xm2cloud_engine::monitor::key::f352c284-19f3-44ef-927e-8ad2eabdae94.net.if.out.bytes.persec/iface=en2 
[
    1524625902.152811 xm2cloud_engine::monitor::val::55b71404-d994-401a-b4cc-857ce9b0e43b
]

# Eventdata(hmset):
xm2cloud_engine::monitor::val::55b71404-d994-401a-b4cc-857ce9b0e43b
{
    value: ...
}

```

### For Debug:

```
```
