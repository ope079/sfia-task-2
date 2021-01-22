#!/bin/bash

# Build and push images
docker-compose build --build-arg APP_VERSION=${version}
docker-compose push
docker system prune -af