# Official Docker Documentation official website

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
# Build Container Image with image tag and detach mode
docker build -t -d <IMAGE_TAG> .

# Running container
docker ps

# Exec
docker exec -it <CONTAINER_ID> <bash|sh|...>

# Stop and Pause
docker pause <CONTAINER_ID>
docker stop <CONTAINER_ID>

# Remove docker with force tag
docker rm -f <CONTAINER_ID>
# Remove all running containers
docker rm -f $(docker ps -a -q)
# Remove all images
docker rmi -f $(docker images -a -q)

# Prune 
docker prune <...>

# Docker Repository
docker login
# First, Create Repository in Container Registry, then
docker push <...>