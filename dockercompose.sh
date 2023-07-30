#!/bin/bash
# Validate number of args
if [ $# -lt 2 ]; then
  echo "Usage: $(basename $0) branch command"
  exit 1
fi

BRANCH=$1

# Shift args and take the rest
shift 1
COMMAND="$@"

echo "Branch: $BRANCH"
echo "Command: $COMMAND"

# Project name
if [ $BRANCH == prod ]; then
  PROJECT="production"
elif [ $BRANCH == dev ]; then
  PROJECT="development"
elif [ $BRANCH == local ]; then
  PROJECT="local"
else
  echo "Possible branches: [prod, dev, local]"
  exit 1
fi

DOCKER_CMD="docker compose -f ./docker/docker-compose.yml \
  -f ./docker/docker-compose.$BRANCH.yml \
  -p project-agent-$PROJECT $COMMAND"

${DOCKER_CMD}