#!/bin/sh

#osascript -e "tell application \"Finder\"
#	set currentDir to target of Finder window 1 as alias
#end tell
#set jrePath to \"jre/bin/java \"
#set options to \"-Djava.awt.headless=false \"
#set jarCommand to \"-jar \"
#set options to \"-Djava.awt.headless=false \"
#set jarName to \"dev-access-ios-standalone.jar\"
#set shellScript to POSIX path of currentDir & jrePath & options & jarCommand & POSIX path of currentDir & jarName
#log \"launch app by command -> \" & shellScript
#do shell script shellScript with administrator privileges"

#DEBUG_OPTS="-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=8001"
PWD=$(cd "`dirname "$0"`" && pwd)
chmod -R 777 "$PWD"/jre
# sudo "$PWD"/jre/bin/java --add-opens=javafx.web/com.sun.javafx.webkit=ALL-UNNAMED -Ddevplay.home="$PWD" $DEBUG_OPTS -jar "$PWD"/dev-access-ios-standalone.jar $1
sudo "$PWD"/jre/bin/java -Duser.dir="$PWD" -Drun.env="mac" --add-opens java.desktop/sun.awt=ALL-UNNAMED --add-opens java.desktop/sun.lwawt=ALL-UNNAMED --add-opens java.desktop/sun.lwawt.macosx=ALL-UNNAMED -Ddevplay.home="$PWD" $DEBUG_OPTS -jar "$PWD"/dev-access-ios-standalone.jar $1
