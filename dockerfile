# ベースイメージとしてUbuntu 22.04を使用
FROM ubuntu:22.04

# 非対話型モードを設定
ENV DEBIAN_FRONTEND=noninteractive

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y --no-install-recommends \
      python3.11 python3.11-venv python3.11-distutils python3.11-dev \
      curl \
      vim \
      git \
      sudo\
      tzdata \
 && ln -s /usr/bin/python3.11 /usr/local/bin/python3 \
 && ln -s /usr/bin/pip3.11 /usr/local/bin/pip3 || true \
 && curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11 \
 && rm -rf /var/lib/apt/lists/*

# 非rootユーザー (ホストとの権限トラブル回避用)
ARG UID=1001
ARG GID=1001
RUN groupadd -g ${GID} dev && useradd -m -u ${UID} -g ${GID} -s /bin/bash dev \
  && usermod -aG sudo dev
USER dev

# 作業ディレクトリの設定
WORKDIR /usr/src/app

# コンテナ起動時にbashシェルを起動
CMD ["/bin/bash"]