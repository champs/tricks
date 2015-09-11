## Client
~/.ssh/config or /etc/ssh/ssh_config
``` 
Host *
  ServerAliveInterval 60
  ExitOnForwardFailure yes  # disconnect from remote server if connection failed
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


### create reverse tunnel
ssh -o ExitOnForwardFailure=yes\
    -o UserKnownHostsFile=/dev/null\
    -o StrictHostKeyChecking=no\
    -o ServerAliveInterval=5\
    -o ServerAliveCountMax=1\
    -i <private key>\
    -p <port number>\
    -N -T -R <reverse port>:localhost:22\
    <user>@<hostname>
