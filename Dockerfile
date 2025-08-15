FROM jenkins/jenkins:lts

USER root

RUN apt-get update && apt-get install -y \
    wget unzip curl gnupg2 libglib2.0-0 libnss3 libgconf-2-4 libxss1 libayatana-appindicator1 xvfb

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb

RUN CHROMEDRIVER_VERSION=124.0.6367.91 && \
    wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/${CHROMEDRIVER_VERSION}/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin && \
    chmod +x /usr/local/bin/chromedriver && \
    rm /tmp/chromedriver.zip

ENV PATH="/usr/local/bin:$PATH"

USER jenkins