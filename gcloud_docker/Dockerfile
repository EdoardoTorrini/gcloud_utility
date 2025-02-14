FROM ubuntu:jammy-20240911.1

ARG USER

RUN useradd -ms /bin/bash "$USER" -G sudo

RUN apt update && \
    apt install -y openssh-server \
    tmux \
    neovim \
    curl \
    sudo \
    net-tools \
    iputils-ping

RUN mkdir /var/run/sshd
RUN echo "$USER:pwd" | chpasswd
COPY ./sshd_config /etc/ssh/sshd_config

RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
EXPOSE 22

RUN apt install -y python3-pip python3-venv && python3 -m pip install ipython requests
RUN echo "pwd" > /home/"$USER"/.password && chown "$USER":"$USER" /home/"$USER"/.password

USER "$USER"

RUN sudo -S curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-linux-x86_64.tar.gz < /home/"$USER"/.password && \
    tar -xf google-cloud-cli-linux-x86_64.tar.gz --directory /home/"$USER"/

RUN echo 'alias gcloud="/home/"$USER"/google-cloud-sdk/bin/gcloud"' >> /home/"$USER"/.bashrc

USER root

CMD ["/usr/sbin/sshd", "-D"]