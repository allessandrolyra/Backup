#!/usr/bin/env bash
#DEBUG_OPTS="-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=8001"
PWD=$(cd "`dirname "$0"`" && pwd)
chmod -R 777 "$PWD"/jre
"$PWD"/jre/bin/java -Ddevplay.home="$PWD" $DEBUG_OPTS -jar "$PWD"/dev-access.jar $1
