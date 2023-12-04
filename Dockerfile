# FROM bitnami/spark:3.5.0
# # FROM continuumio/anaconda3

# USER root

# # Install OpenJDK-11
# RUN apt update && \
#     apt-get install -y openjdk-11-jdk && \
#     apt-get install -y ant && \
#     apt-get install -y curl && \
#     apt-get install -y wget && \
#     apt-get clean;

FROM bitnami/spark:3.5.0

USER root

# Install OpenJDK-11
RUN apt update && \
    apt-get install -y openjdk-11-jdk && \
    apt-get install -y ant && \
    apt-get install -y curl && \
    apt-get install -y wget && \
    apt-get clean;

# Install Python packages
RUN pip install seaborn

# Download IMDb dataset
RUN mkdir -p /usr/local/spark/tmp && \
    wget -P /usr/local/spark/tmp https://datasets.imdbws.com/title.basics.tsv.gz && \
    gzip -d /usr/local/spark/tmp/title.basics.tsv.gz
