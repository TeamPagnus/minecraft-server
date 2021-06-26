FROM python:3.9.5

RUN apt-get update && apt-get install -y \
    default-jre-headless \
    screen \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -r minecraft-server
USER minecraft-server
WORKDIR /home/minecraft-server

RUN pip install --no-cache-dir \
    bs4 \
    ipaddress \
    requests \
    html5lib

COPY --chown=minecraft-server:minecraft-server favicon.ico index.html startcgi.sh ./
COPY --chown=minecraft-server:minecraft-server cgi-bin cgi-bin/
COPY --chown=minecraft-server:minecraft-server js js/
RUN mkdir minecraft

COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
