FROM ubuntu:jammy-20260410@sha256:962f6cadeae0ea6284001009daa4cc9a8c37e75d1f5191cf0eb83fe565b63dd7

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \ 
    apt-get install -y socat && \
    rm -rf /var/lib/apt/lists/*
RUN useradd -M hkco2026

WORKDIR /app
COPY --chown=root src/chal .
COPY --chown=root src/flag.txt .
RUN chmod 755 /app && chmod 755 chal && chmod 644 flag.txt

USER hkco2026
CMD ["socat", "TCP-LISTEN:1337,fork,reuseaddr", "EXEC:./chal,stderr"]
EXPOSE 1337