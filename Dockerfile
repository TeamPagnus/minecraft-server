FROM python:3.9.5-alpine

RUN apk --update upgrade && apk add --no-cache \
    openjdk11-jre-headless \
    screen

RUN addgroup -S minecraft-server && adduser -S minecraft-server -G minecraft-server
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
