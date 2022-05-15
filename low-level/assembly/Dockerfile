FROM ubuntu@sha256:aba80b77e27148d99c034a987e7da3a287ed455390352663418c0f2ed40417fe

RUN export TZ='Europe/Amsterdam'

RUN yes | unminimize && apt update -y && apt upgrade -y && \
    apt install -y nasm gdb gcc

COPY post_bashrc.sh /tmp/
RUN cat /tmp/post_bashrc.sh >> /root/.bashrc

STOPSIGNAL SIGKILL

CMD sleep infinity
