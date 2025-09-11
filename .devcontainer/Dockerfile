FROM ros:humble

LABEL "name"="rqt_dotgraph DevContainer"
LABEL "version"="0.0.1"
LABEL "maintainer"="Alexander Xydes <alexander.l.xydes.civ@us.navy.mil>"

USER root

ENV DEBIAN_FRONTEND=noninteractive

ARG GROUP_ID=1000
ARG GROUP_NAME=dev
ARG USER_ID=1000
ARG USER_NAME=tester

# Packages needed for various utility steps.
RUN apt-get update && apt-get install --no-install-recommends -y \
    acl \
    bash-completion \
    ca-certificates \
    git \
    git-core \
    gitk \
    gnupg \
    iputils-ping \
    less \
    net-tools \
    netcat \
    openssl \
    python3-dbus \
    python3-pip \
    python3-secretstorage \
    python3-setuptools \
    python3-wheel \
    python3-opencv \
    sudo \
    unzip \
    vim \
    wget && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean

# User setup.
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN groupadd -g ${GROUP_ID} ${GROUP_NAME} && \
    useradd -l -m ${USER_NAME} -s /bin/bash -u ${USER_ID} -g ${GROUP_NAME} -d /home/${USER_NAME} && \
    echo ${USER_NAME}:${GROUP_NAME} | chpasswd && \
    echo "${USER_NAME} ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/${USER_NAME} && \
    chmod 0440 /etc/sudoers.d/${USER_NAME}

ENV HOME=/home/${USER_NAME}
WORKDIR ${HOME}

# Fancy prompt.
COPY --chown=${USER_ID}:${GROUP_ID} .devcontainer/config/.git-prompt.sh ${HOME}/.git-prompt.sh
COPY --chown=${USER_ID}:${GROUP_ID} .devcontainer/config/.bash_prompt ${HOME}/.bash_prompt
RUN echo ". ~/.git-prompt.sh" >> ${HOME}/.bashrc && \
    echo ". /opt/ros/humble/setup.bash" >> ${HOME}/.bashrc && \
    echo ". ~/.bash_prompt" >> ${HOME}/.bashrc

RUN mkdir -p ${HOME}/.local/bin && \
    ls -lh ${HOME} && \
    ls -lh ${HOME}/.local && \
    ls -lh ${HOME}/.local/bin && \
    chown -R ${USER_ID}:${GROUP_ID} ${HOME}/.local

USER ${USER_NAME}
RUN mkdir -p ${HOME}/ws/src && \
    chown -R ${USER_ID}:${GROUP_ID} ${HOME}/ws/
RUN export PATH="$HOME/.local/bin:$PATH"
WORKDIR ${HOME}/ws

ENTRYPOINT ["/ros_entrypoint.sh"]
