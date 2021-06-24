[![Build Status](https://travis-ci.com/TeamPagnus/minecraft-server-manager.png?branch=master)](https://travis-ci.com/TeamPagnus/minecraft-server-manager)
# Running the container
```sh
docker run --name minecraft-server \
  --publish 8000:8000 \
  --publish 25565:25565 \
  -d teampagnus/minecraft-server-manager
```
