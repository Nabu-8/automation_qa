FROM jenkins/jenkins:lts

USER root

RUN apt-get update && apt-get install -y \
    wget unzip curl gnupg2 libglib2.0-0 libnss3 libgconf-2-4 libxss1 libayatana-appindicator1 xvfb

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb

RUN wget -O /tmp/chromedriver-linux64.zip \
     https://storage.googleapis.com/chrome-for-testing-public/139.0.7258.68/linux64/chromedriver-linux64.zip && \
    unzip /tmp/chromedriver-linux64.zip -d /tmp/ && \
    mv /tmp/chromedriver-linux64/chromedriver /usr/local/bin/chromedriver && \
    chmod +x /usr/local/bin/chromedriver && \
    rm -rf /tmp/chromedriver-linux64*

ENV PATH="/usr/local/bin:$PATH"

USER jenkins