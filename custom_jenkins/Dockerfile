# Use the Jenkins LTS image
FROM jenkins/jenkins:lts-jdk17

# Switch to root
USER root

# Install required dependencies
RUN apt-get update -y && \
    apt-get install -y apt-transport-https ca-certificates curl gnupg2 && \
    curl -fsSL https://download.docker.com/linux/debian/gpg \
        | gpg --dearmor -o /usr/share/keyrings/docker.gpg && \
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker.gpg] \
        https://download.docker.com/linux/debian trixie stable" \
        > /etc/apt/sources.list.d/docker.list && \
    apt-get update -y && \
    apt-get install -y docker-ce docker-ce-cli containerd.io && \
    apt-get clean

# Add Jenkins user to Docker group
RUN groupadd -f docker && usermod -aG docker jenkins

# Docker directory for DinD
RUN mkdir -p /var/lib/docker
VOLUME /var/lib/docker

# Back to Jenkins user
USER jenkins
