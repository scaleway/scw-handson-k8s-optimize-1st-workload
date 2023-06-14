FROM python:alpine

LABEL org.opencontainers.image.source=https://github.com/scaleway/scw-handson-k8s-optimize-1st-workload

RUN pip install bottle paste requests

COPY run.py /run.py

ENV K8S_NS="docker"
ENV K8S_NODE="local"

EXPOSE 80 9001

ENTRYPOINT ["/run.py"]
