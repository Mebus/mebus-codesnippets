# Maven

## Build a jar package

```
mvn package
```

## Execute

```
mvn exec:java
```

## Get sources and Javadocs

When you're using Maven in an IDE you often find the need for your IDE to resolve source code and Javadocs for your library dependencies. There's an easy way to accomplish that goal.

```
mvn dependency:sources
mvn dependency:resolve -Dclassifier=javadoc
```

The first command will attempt to download source code for each of the dependencies in your pom file.

The second command will attempt to download the Javadocs.

Maven is at the mercy of the library packagers here. So some of them won't have source code packaged and many of them won't have Javadocs.

In case you have a lot of dependencies it might also be a good idea to use inclusions/exclusions to get specific artifacts, the following command will for example only download the sources for the dependency with a specific artifactId:

```
mvn dependency:sources -DincludeArtifactIds=guava
```

(source: https://stackoverflow.com/a/2430107)
