
# Propósito
------------------------
Este proyecto ha sido creado con el fin de educar a todas las personas que quieran saber y experimentar como manegar contenedores desde la web. He creado un codigo en python y HTML que me permite iniciar, parar, reinicier y eliminar un contenedor en específico. 

# Requisitos
--------------------------

## Python3, pip, flask
1. Instalaremos python3 y pip con el siguiente comando:
```bash
apt-get install python3 python3-pip
```
2. Instalamos flask:
```bash
pip install flask
```

## Docker y docker compose 
### Docker
1. Update the apt package index and install packages to allow apt to use a repository over HTTPS:
```bash
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
```

2. Add Docker's official GPG key:
```bash
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
```

3. Use the following command to set up the repository:
```bash
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

4. Update the apt package index:
```bash
sudo apt-get update
```

5. Install Docker Engine, containerd, and Docker Compose.
```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
### Docker compose
1. Update the package index, and install the latest version of Docker Compose:
 - For Ubuntu and Debian, run:
```bash
sudo apt-get update
sudo apt-get install docker-compose-plugin
```
- For RPM-based distros, run:
```bash
sudo yum update
sudo yum install docker-compose-plugin
```

2. Verify that Docker Compose is installed correctly by checking the version.
```bash
docker compose version
Docker Compose version vN.N.N
```



