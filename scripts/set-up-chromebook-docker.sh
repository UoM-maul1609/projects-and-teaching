sudo apt-get install -y lsb-release software-properties-common
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian \
   $(lsb_release -cs) \
   stable"
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io 
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
docker run hello-world