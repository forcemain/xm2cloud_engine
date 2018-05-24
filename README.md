### For Arch:
#### xm2cloud_engine is a powerful and graceful engine component for xm2cloud devops framework.

### For Metric (LifeCycle: 1h):

```
# Heartbeat(hmset):
xm2cloud_agent::f352c284-19f3-44ef-927e-8ad2eabdae94::heartbeat
{
    name: ...,
    version: ...,
    timestamp: ...
}
xm2cloud_engine::0599f2ea-d113-4970-873d-f9ad154ae22c::heartbeat
{
    name: ...,
    version: ...,
    timestamp: ...,
}

# Timeseries(zadd):
f352c284-19f3-44ef-927e-8ad2eabdae94.net.if.out.bytes.persec/iface=en2 
[
    1524625902.152811 55b71404-d994-401a-b4cc-857ce9b0e43b
]

# Eventdata(hmset):
55b71404-d994-401a-b4cc-857ce9b0e43b
{
    value: ...
}

```

### For Debug:

```
```
