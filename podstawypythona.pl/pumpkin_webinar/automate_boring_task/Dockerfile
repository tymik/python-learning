FROM python:3.12

WORKDIR /app

RUN apt update -y \
    && apt install -y \
        python3-pip \
        python3-cffi \
        python3-brotli \
        libpango-1.0-0 \
        libpangoft2-1.0-0

COPY requirements.txt .

RUN pip install -r requirements.txt 

CMD [ "/bin/bash" ]
