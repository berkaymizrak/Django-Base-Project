#!/bin/sh

echo "Waiting for postgres..."

while [ "$(pg_isready -h $POSTGRES_HOST -p $POSTGRES_PORT)" != "$POSTGRES_HOST:$POSTGRES_PORT - accepting connections" ]; do
  sleep 1
done

echo "PostgreSQL started"

if [ "$SERVICE_NAME" = "app_agent" ]; then

  echo " --- --- --- --- --- --- --- --- --- "
  echo "Applying database migrations"
  python manage.py migrate --noinput

fi

echo " --- --- --- --- --- --- --- --- --- "
echo "Starting server"
exec "$@"
