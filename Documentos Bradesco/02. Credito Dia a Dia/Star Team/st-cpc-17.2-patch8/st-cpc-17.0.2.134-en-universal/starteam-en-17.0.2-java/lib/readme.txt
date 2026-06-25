only the libs needed to get CPC to compile are checked in to starteam, mainly 
for the convinience of devs who aren't interested in the reporting features.

The ant build kicks off the build.gradle build which will fetch the remainder
of the depedencies from starteam and put them here.

To do this manually, run gradlew reportLibs
from the project root