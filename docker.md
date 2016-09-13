docker build cmds:
```
docker build -t .
Step 1: <cmd>
 ---> Running in 27b060a3f926
     ... <output>  <---
 ---> 233ddda75c1a
Removing intermediate container 27b060a3f926

If there is any error on output we can debug img <27b060a3f926>
>>> docker run --rm -it <img_id> /bin/bash


```

docker images
```
docker rmi <img_id>
```
docker containers
```
docker rm <cntr_id>
```


docker compose
```
docker-compose -f docker-compose.yml -f production.yml up -d
```

stop & remove all docker ps
```
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
```
