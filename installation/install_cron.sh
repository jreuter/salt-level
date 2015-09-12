#!/bin/bash
source './require_root.sh'
source './log_errors.sh'

# Temporary cron file.
USER=$('logname')
FILE="/tmp/"$USER"_saltcheck_cron"
CMD="sudo python /home/pi/code/salt-level/reading.py"

#sudo crontab -l > $FILE

# Add command script to cron.
echo "00 02 * * * $USER $CMD" > $FILE

# Install new cron file.
mv $FILE "/etc/cron.d/"

