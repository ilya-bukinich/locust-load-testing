## Build & run
```
docker build --tag locust:latest .  
docker run -d \
-p 8089:8089 \
--restart unless-stopped \
locust:latest
```
## Docs
https://docs.locust.io/en/stable/what-is-locust.html
## Test
Go to http://localhost:8089, setup `host`, `number of users`, `spawn rate`