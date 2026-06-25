#!/usr/bin/env bash
#DEBUG_OPTS="-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=8001"
PWD=$(cd "`dirname "$0"`" && pwd)
chmod -R 777 "$PWD"/jre
# sudo "$PWD"/jre/bin/java --add-opens=javafx.web/com.sun.webkit.network=ALL-UNNAMED -Ddevplay.home="$PWD" $DEBUG_OPTS -jar "$PWD"/dev-access.jar $1
sudo "$PWD"/jre/bin/java --add-opens java.desktop/sun.awt=ALL-UNNAMED --add-opens java.desktop/sun.lwawt=ALL-UNNAMED --add-opens java.desktop/sun.lwawt.macosx=ALL-UNNAMED -Ddevplay.home="$PWD" $DEBUG_OPTS -jar "$PWD"/dev-access.jar $1
