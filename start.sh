#!/bin/bash
echo Starting Good Mood server...
cd /var/www/good-mood/server/
gunicorn -w 6 -b 127.0.0.1:5003 server:app
