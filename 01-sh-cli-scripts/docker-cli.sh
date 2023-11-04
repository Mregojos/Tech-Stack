# Official Docker Documentation official website: https://docs.docker.com

# Install docker

# Dockerfile
touch Dockerfile

# Docker Help
docker help

# Pull Container Image
docker pull <CONTAINER_IMAGE>

# Images
docker images

# Build Container Image with image tag
docker build -t <IMAGE_TAG> .

# Run an image
docker run <...>
# Run an image with detached mode and port mapping
docker run -d -p <PORT>:<CONTANER_PORT> <IMAGE_ID/IMAGE_NAME>
# Run an image with detached mode, port mapping, and volume
docker run -d -p <PORT>:<CONTANER_PORT> -v <LOCATION>:<CONTAINER_LOCATION> <IMAGE_ID/IMAGE_NAME>

# Running container
docker ps
# Show all
docker ps -a 

# Exec
docker exec -it <CONTAINER_ID> <bash|sh|...>

# Stop and Pause
docker pause <CONTAINER_ID>
docker stop <CONTAINER_ID>

# Remove docker with force tag
docker rm -f <CONTAINER_ID>
# Remove all running containers
docker rm -f $(docker ps -a -q)
# Remove docker image with force tag
docker rmi -f <IMAGE_ID>
# Remove all images
docker rmi -f $(docker images -a -q)

# Volume
docker volume <...>

# Prune network
docker network prune <...>

# Docker Repository
docker login
# First, Create Repository in Container Registry, then
# Build Docker image with a tag
docker build -t <USERNAME>/<IMAGE_NAME>:<IMAGE_TAG> .
# Push the image
docker push <USERNAME>/<IMAGE_NAME>:<IMAGE_TAG> 
# Pull the image
docker pull <USERNAME>/<IMAGE_NAME>:<IMAGE_TAG> 