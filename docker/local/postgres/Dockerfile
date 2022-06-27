FROM postgres:14.1

COPY ./docker/local/postgres/maitenance /usr/local/bin/maitenance

RUN chmod +x /usr/local/bin/maitenance/*
RUN mv /usr/local/bin/maitenance/* /usr/local/bin \
    && rmdir /usr/local/bin/maitenance
