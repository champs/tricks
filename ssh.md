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


## autossh
```
flags 
  -f deamon
  -M monitor port, (0 turns off)
```

## mosh (mobile shell)
```
install
sudo apt-get install mosh
```
### server
mosh-server

### client
mosh --ssh="-o <blah> -p <port>" server.com
