#!/bin/bash

NAME="epreuve_api"                                  # Name of the application
DJANGODIR=/Users/tharcisse/Desktop/Files/Darcy-Tharcisse/epreuve-archive/epreuve_api  # Django project directory
SOCKFILE=/Users/tharcisse/Desktop/Files/Darcy-Tharcisse/epreuve-archive/epreuve_api/run/gunicorn.sock  # we will communicate using this unix socket
USER=$(whoami)                                    # the user to run as
GROUP="staff"                                   # the group to run as
NUM_WORKERS=3                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=epreuve_api.settings       # which settings file should Django use
DJANGO_WSGI_MODULE=epreuve_api.wsgi               # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source /Users/tharcisse/Desktop/Files/Darcy-Tharcisse/epreuve-archive/epreuve_api/env/bin/activate

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
exec /Users/tharcisse/Desktop/Files/Darcy-Tharcisse/epreuve-archive/epreuve_api/env/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-