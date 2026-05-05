FROM ubuntu:24.04

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y install \
        tini xinetd \
        python3.12 \
    && rm -rf /var/lib/apt/lists/*

RUN useradd --no-create-home hkco2026 && mkdir -p /home/hkco2026

COPY ./src /home/hkco2026/
COPY ./app.xinetd /etc/xinetd.d/app
COPY ./src/flag.txt /

RUN chown -R root:root /home && \
    find /home -type d -exec chmod 555 {} \; && \
    find /home -type f -exec chmod 444 {} \;

WORKDIR /home/hkco2026
EXPOSE 1337

ENTRYPOINT ["/usr/bin/tini", "--"]
CMD ["/usr/sbin/xinetd", "-dontfork"]