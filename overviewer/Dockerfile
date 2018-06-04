FROM ubuntu:latest
MAINTAINER chrismarksus@gmail.com

# Add crontab file in the cron directory
ADD ./overviewer_cron.sh /etc/cron.d/overviewer_cron.sh
ADD ./overviewer_config.py /etc/cron.d/overviewer_config.py

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/overviewer_cron.sh

# Create the log file to be able to run tail
RUN touch /var/log/overviewer_cron.log

RUN apt-get update && \
    apt-get install -y wget gnupg cron && \
    echo "deb http://overviewer.org/debian ./" >> /etc/apt/sources.list && \
    wget -O - https://overviewer.org/debian/overviewer.gpg.asc | apt-key add - && \
    apt-get update && \
    apt-get install -y minecraft-overviewer && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    wget https://s3.amazonaws.com/Minecraft.Download/versions/1.12/1.12.jar -P ~/.minecraft/versions/1.12/

# Run the command on container startup
CMD cron && tail -f /var/log/overviewer_cron.log
