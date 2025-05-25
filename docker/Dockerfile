FROM continuumio/miniconda3:latest

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

USER root

RUN apt-get update --yes && apt-get install --yes \
    python3 \
    python3-dev \
    python3-pip \
    build-essential \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /usr/src/miniconda3
WORKDIR /usr/src/miniconda3

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./docker/environment.yml .
RUN conda update -n base conda -y && conda env update -n base -f environment.yml

EXPOSE 8889

CMD ["jupyter", "lab", "--no-browser", "--ip=0.0.0.0", "--port=8889", "--allow-root"]
