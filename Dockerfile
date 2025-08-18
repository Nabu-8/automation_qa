FROM jenkins/jenkins:lts

USER root

RUN apt-get update && apt-get install -y \
    wget unzip curl gnupg2 \
    libglib2.0-0 libnss3 libgconf-2-4 libxss1 \
    libayatana-appindicator1 xvfb libxrandr2 libasound2 \
    libatk-bridge2.0-0 libatk1.0-0 libatspi2.0-0 libcups2 \
    libxcomposite1 libxcursor1 libxi6 libxtst6 libappindicator3-1 \
    fonts-liberation libgbm1 --no-install-recommends

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb

RUN CHROME_VERSION=$(google-chrome --version | grep -oP '\d+\.\d+\.\d+') && \
    CHROMEDRIVER_VERSION=$(curl -s "https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_$CHROME_VERSION") && \
    wget -O /tmp/chromedriver.zip "https://storage.googleapis.com/chrome-for-testing-public/${CHROMEDRIVER_VERSION}/linux64/chromedriver-linux64.zip" && \
    unzip /tmp/chromedriver.zip -d /tmp/ && \
    mv /tmp/chromedriver-linux64/chromedriver /usr/local/bin/chromedriver && \
    chmod +x /usr/local/bin/chromedriver && \
    rm -rf /tmp/chromedriver*

ENV PATH="/usr/local/bin:$PATH"

USER jenkins