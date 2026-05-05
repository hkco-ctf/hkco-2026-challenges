FROM ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y gcc make socat libssl-dev && \
    rm -rf /var/lib/apt/lists/*

RUN useradd -M hkco2026

WORKDIR /app
COPY src/chall.c .
RUN gcc -O2 chall.c -o chall -lcrypto && \
    chmod 755 chall

ENV FLAG=hkco2026{**REDACTED**}

USER hkco2026
CMD ["socat", "TCP-LISTEN:1337,fork,reuseaddr", "EXEC:./chall,stderr"]
EXPOSE 1337
