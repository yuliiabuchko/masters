## Bugs.jar configuration

1. **Log4j repo**    
   - Download `jconslole.jar` and put to the right `lib` folder
   - Czasami kloci sie o jakies dziwne rzeczy o `-source 1.6` w performance test
     - Pomaga `mvn clean install`





### Python
1. `sudo pip install joblib` - fails without sudo
2. Easier without venv (don't blame me)


### Bash
1. `curl`
2. w skrypcie download spotbugs http -> https (`SB_URL`)
3. `sudo apt-get install libdbi-perl`




java -Xbootclasspath/p:/home/yuliia/PycharmProjects/StaticBugCheckers/python/../static-checkers/error_prone_ant-2.1.1.jar com.google.errorprone.ErrorProneCompiler -implicit:none -cp /home/yuliia/.local/share/JetBrains/Toolbox/apps/IDEA-U/ch-0/213.7172.25/plugins/maven/lib/maven3/boot/plexus-classworlds.license:/home/yuliia/.local/share/JetBrains/Toolbox/apps/IDEA-U/ch-0/213.7172.25/plugins/maven/lib/maven3/boot/plexus-classworlds-2.6.0.jar log4j-core/src/main/java/org/apache/logging/log4j/core/async/AsyncLoggerConfig.java




javac   -J--add-exports=jdk.compiler/com.sun.tools.javac.api=ALL-UNNAMED   -J--add-exports=jdk.compiler/com.sun.tools.javac.file=ALL-UNNAMED   -J--add-exports=jdk.compiler/com.sun.tools.javac.main=ALL-UNNAMED   -J--add-exports=jdk.compiler/com.sun.tools.javac.model=ALL-UNNAMED   -J--add-exports=jdk.compiler/com.sun.tools.javac.parser=ALL-UNNAMED   -J--add-exports=jdk.compiler/com.sun.tools.javac.processing=ALL-UNNAMED   -J--add-exports=jdk.compiler/com.sun.tools.javac.tree=ALL-UNNAMED   -J--add-exports=jdk.compiler/com.sun.tools.javac.util=ALL-UNNAMED   -J--add-opens=jdk.compiler/com.sun.tools.javac.code=ALL-UNNAMED   -J--add-opens=jdk.compiler/com.sun.tools.javac.comp=ALL-UNNAMED   -XDcompilePolicy=simple -processorpath /home/yuliia/PycharmProjects/StaticBugCheckers/static-checkers/error_prone_core-2.12.1-with-dependencies.jar:/home/yuliia/PycharmProjects/StaticBugCheckers/static-checkers/dataflow-errorprone-3.15.0.jar   '-Xplugin:ErrorProne -XepDisableAllChecks -Xep:CollectionIncompatibleType:ERROR' -cp /home/yuliia/PycharmProjects/bugs-dot-jar/logging-log4j2/log4j-api/target/log4j-api-2.3-SNAPSHOT.jar:/home/yuliia/PycharmProjects/bugs-dot-jar/logging-log4j2/log4j-api/target/log4j-api-2.3-SNAPSHOT-tests.jar:/home/yuliia/PycharmProjects/bugs-dot-jar/logging-log4j2/log4j-core/target/log4j-core-2.3-SNAPSHOT.jar:/home/yuliia/PycharmProjects/bugs-dot-jar/logging-log4j2/log4j-core/target/log4j-core-2.3-SNAPSHOT-tests.jar:/home/yuliia/PycharmProjects/bugs-dot-jar/logging-log4j2/log4j-slf4j-impl/target/log4j-slf4j-impl-2.3-SNAPSHOT.jar:/home/yuliia/PycharmProjects/bugs-dot-jar/logging-log4j2/log4j-to-slf4j/target/log4j-to-slf4j-2.3-SNAPSHOT.jar:/home/yuliia/PycharmProjects/bugs-dot-jar/logging-log4j2/log4j-jcl/target/log4j-jcl-2.3-SNAPSHOT.jar:/home/yuliia/PycharmProjects/bugs-dot-jar/logging-log4j2/log4j-flume-ng/target/log4j-flume-ng-2.3-SNAPSHOT.jar:/home/yuliia/PycharmProjects/bugs-dot-jar/logging-log4j2/log4j-flume-ng/target/log4j-flume-ng-2.3-SNAPSHOT-tests.jar:/home/yuliia/PycharmProjects/bugs-dot-jar/logging-log4j2/log4j-web/target/log4j-web-2.3-SNAPSHOT.jar:/home/yuliia/PycharmProjects/bugs-dot-jar/logging-log4j2/log4j-taglib/target/log4j-taglib-2.3-SNAPSHOT.jar:/home/yuliia/PycharmProjects/bugs-dot-jar/logging-log4j2/log4j-jmx-gui/target/log4j-jmx-gui-2.3-SNAPSHOT.jar:/home/yuliia/PycharmProjects/bugs-dot-jar/logging-log4j2/log4j-samples/flume-common/target/log4j-samples-flume-common-2.3-SNAPSHOT.jar:/home/yuliia/PycharmProjects/bugs-dot-jar/logging-log4j2/log4j-nosql/target/log4j-nosql-2.3-SNAPSHOT.jar:/home/yuliia/PycharmProjects/bugs-dot-jar/logging-log4j2/log4j-perf/target/log4j-perf-2.3-SNAPSHOT.jar:/home/yuliia/PycharmProjects/bugs-dot-jar/logging-log4j2/log4j-iostreams/target/log4j-iostreams-2.3-SNAPSHOT.jar:/home/yuliia/PycharmProjects/bugs-dot-jar/logging-log4j2/log4j-jul/target/log4j-jul-2.3-SNAPSHOT.jar log4j-core/src/main/java/org/apache/logging/log4j/core/async/AsyncLoggerConfig.java



