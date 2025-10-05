FROM debian:bookworm-slim

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt-get install git -y
RUN pip3 install pip-tools --break-system-packages

CMD while : ; do sleep 1000; done
