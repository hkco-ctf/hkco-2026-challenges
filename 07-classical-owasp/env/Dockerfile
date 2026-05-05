FROM python:3.11-slim

RUN pip install --no-cache-dir flask

RUN useradd -M hkco2026

WORKDIR /app
COPY src/ .
RUN chmod -R a+rX /app

ENV FLAG=hkco2026{cl4ss1c_sqli_a774ck_v3ry_eff3c71ve}

USER hkco2026
CMD ["python3", "-u", "app.py"]
EXPOSE 1337
