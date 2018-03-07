# LXC


## lxc-ls  -f

```
NAME     STATE    IPV4                      IPV6  GROUPS  AUTOSTART  
-------------------------------------------------------------------
box1003  STOPPED  -                         -     -       NO         
box1004  STOPPED  -                         -     -       NO         
box1007  STOPPED  -                         -     -       NO         
box714   RUNNING  10.0.4.1, 172.17.202.169  -     -       NO         
box715   RUNNING  10.0.4.1, 172.17.199.217  -     -       NO         
box717   RUNNING  10.0.4.1, 172.17.206.27   -     -       NO         
```

## lxc-info -n box717
```
Name:           box717
State:          RUNNING
PID:            16702
IP:             10.0.4.1
IP:             172.17.206.27
CPU use:        155.61 seconds
BlkIO use:      326.77 MiB
Memory use:     1.85 GiB
KMem use:       0 bytes
Link:           veth28I78N
 TX bytes:      1.27 MiB
 RX bytes:      76.27 MiB
 Total bytes:   77.55 MiB
```
