## Client
~/.ssh/config or /etc/ssh/ssh_config
``` 
Host *
  ServerAliveInterval 60
```

## Server
~/etc/ssh/sshd_config
```
  # make connection alive
  ClientAliveInterval 60
```
