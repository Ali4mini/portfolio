
#TODO: use the slim version for 
FROM docker.arvancloud.ir/python:3.13


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /code

# setting runflare debian mirros
RUN DEBIAN_CODENAME=trixie && tee /etc/apt/sources.list > /dev/null <<EOF
deb http://mirror-linux.runflare.com/debian $DEBIAN_CODENAME main
deb http://mirror-linux.runflare.com/debian-security $DEBIAN_CODENAME-security main
EOF

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    gettext \
    netcat-traditional \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies with runflare mirrors 
COPY requirements.txt /code/
RUN pip install -i https://mirror-pypi.runflare.com/simple --upgrade pip && pip install -i https://mirror-pypi.runflare.com/simple -r requirements.txt

# Copy project
COPY . /code/


ENTRYPOINT ["python3", "/code/portfolio/manage.py", "runserver", "0.0.0.0:8080"]
