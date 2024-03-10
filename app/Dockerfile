FROM python:3

ENV HOST 0.0.0.0
ENV PORT 8080
ENV WEBSITES_PORT 8080

EXPOSE 8080
EXPOSE 2222

COPY . /app
COPY ["startup.sh", "/app/startup.sh"]

#SSH
RUN apt-get update
RUN apt-get install -y openssh-server 
RUN echo "root:Docker!" | chpasswd 
RUN mkdir -p /run/sshd 
COPY ["sshd_config", "/etc/ssh/"]
RUN mkdir -p /tmp
RUN ssh-keygen -A 
#SSH End

#install additional packages
RUN apt-get install -y iproute2
RUN apt-get install -y curl
#installs END

#start
CMD ["bash","/app/startup.sh"]