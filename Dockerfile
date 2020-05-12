FROM ubuntu

WORKDIR /root/.kube

COPY src/config ./

# Create app directory
WORKDIR /app

RUN apt-get update && apt-get install -y \
    software-properties-common
RUN add-apt-repository universe
RUN apt-get update && apt-get install -y \
  apt-utils \
  python3 \
  python3-pip

# Install app dependencies
COPY src/requirements.txt ./

RUN pip3 install -r requirements.txt

# Bundle app source
COPY src /app
EXPOSE 8050
CMD ["/bin/bash"]
