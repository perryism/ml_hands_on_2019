FROM ubuntu:18.04
MAINTAINER Perry

RUN apt-get -qq update && apt-get -qq -y install curl bzip2 git \
    && curl -sSL https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -o /tmp/miniconda.sh \
    && bash /tmp/miniconda.sh -bfp /usr/local \
    && rm -rf /tmp/miniconda.sh \
    && conda install -y python=3 \
    && conda update conda \
    && apt-get -qq -y remove curl bzip2 \
    && apt-get -qq -y autoremove \
    && apt-get autoclean \
    && rm -rf /var/lib/apt/lists/* /var/log/dpkg.log \
    && conda clean --all --yes 

COPY requirements.txt .  
RUN pip install -r requirements.txt

EXPOSE 8888

WORKDIR /workspace

COPY entrypoint.sh /workspace

VOLUME ["/workspace/notebooks"]

CMD ["/workspace/entrypoint.sh"]
