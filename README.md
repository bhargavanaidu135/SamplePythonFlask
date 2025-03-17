# A Simple Time Service application is built in python-3.12 (flask app)

Flask App Deployment Using Docker on VM

This guide will walk you through setting up a VM, building a Docker image for your Flask application, scanning the image for vulnerabilities, pushing it to a Docker registry, and running the containerized application.

## Table of Contents:

1. [Setup a Virtual Machine (VM) and Install Git & Docker](#setup-a-VM-and-install-git--docker)
2. [Clone the Repository](#clone-the-repository)
3. [Build the Docker Image](#build-the-docker-image)
4. [Scan the Docker Image for Vulnerabilities (VA Assessment)](#scan-the-docker-image-for-vulnerabilities-va-assessment)
5. [Push the Docker Image to Docker Registry](#push-the-docker-image-to-docker-registry)
6. [Run the Docker Container Application](#run-the-docker-container-application)

Pre-Requisites:

- A Virtual Machine (Eg: AWS EC2, Azure VM, Google Compute Engine, or local VM)
- Access to a Docker Hub or any private Docker registry
- GitHub account for code management
- Basic knowledge of Docker and Python Flask

STEP1:
## Setup a VM and Install Git & Docker

Install Git-
```
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install -y git
git --version
```

Install Docker-

```
# Update and upgrade system packages
sudo apt-get update -y
sudo apt-get upgrade -y

# Install required dependencies
sudo apt-get install -y ca-certificates curl gnupg lsb-release

# Add Docker GPG key
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Add Docker repository
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Update package index for Docker repo
sudo apt-get update -y

# Install Docker packages such as buildx and docker compose plugins
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Enabling, starting docker and adding user to Docker group
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -aG docker $USER

##check the docker version
docker --version
```

STEP2: 
## Clone the Repository

Clone this GitHub repository to your VM-
```
git clone -b master https://github.com/bhargavanaidu135/SamplePythonFlask.git
cd app
```
STEP3: 
## Build the Docker Image

Ensure your Dockerfile is present in the root directory of the project. When you build a docker image tag the image with version number (v1.0) and Latest tag which is used by container currently.  
Maintain the docker image tags as latest and v1.0 for an image each time it is built with new code.  
Format of image tag during image build- `docker build -t <DockerHubUserName>/<ImageName>:v1.0`

```
docker build -t bhargav135/flask-app:latest
docker build -t bhargav135/flask-app:v1.0
```

STEP4: 
## Scan the Docker Image for Vulnerabilities (VA Assessment)

use TRIVY tool to scan the image

Install Trivy-
```
sudo apt install wget -y  
wget https://github.com/aquasecurity/trivy/releases/latest/download/trivy_0.50.1_Linux-64bit.deb  
sudo dpkg -i trivy_0.50.1_Linux-64bit.deb  
```
Scan the image-
Important: Fix high and critical vulnerabilities as much as possible before pushing to registry.
```
trivy image bhargav135/flask-app:v1.0
```
STEP5: 
## Push the Docker Image to Docker Registry

Login to Docker Hub-
create PAT --> go to https://hub.docker.com --> login to your account --> go to account settings --> Generate a Personal Access Token with READONLY access --> copy and save it in a secure place for feature use.  
Instead of directly exposing docker hub credentials on the CLI, it's a best practice to use them as environment variables.

```
export DOCKERHUB_PAT="<your-personal-access-token>"
echo $DOCKERHUB_PAT | docker login -u bhargav135 --password-stdin
unset DOCKERHUB_PAT
```
Push the image-

```
docker push bhargav135/flask-app:v1.0
docker push bhargav135/flask-app:latest
```

STEP6: 
## Run the Docker Container Application

Run the container-

```
docker run -dt --name <containerName_FlaskApp> -p 8443:80 bhargav135/flask-app:latest
# check the status of container whether it is in running state or not
docker ps
```

After successful executing of these steps and running of containerized application, will be able to see that the app is giving exact response by browsing the "<PublicIP>:8443" or using `curl localhost:80` as shown below
flask-app response


![image](https://github.com/user-attachments/assets/e40c47f2-7086-463b-8ab3-23932884e78a)







