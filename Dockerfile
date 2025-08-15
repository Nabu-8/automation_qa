FROM jenkins/jenkins:lts

USER root

# Установка Google Chrome и зависимостей
RUN apt-get update && apt-get install -y \
    wget unzip curl gnupg2 libglib2.0-0 libnss3 libgconf-2-4 libxss1 libappindicator1 libindicator7 xvfb

# Установка Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb

# Установка ChromeDriver
RUN CHROME_VERSION=$(google-chrome --version | grep -oP '\d+\.\d+\.\d+') && \
    CHROMEDRIVER_VERSION=$(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION") && \
    wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/${CHROMEDRIVER_VERSION}/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin && \
    chmod +x /usr/local/bin/chromedriver && \
    rm /tmp/chromedriver.zip

ENV PATH="/usr/local/bin:$PATH"

USER jenkins