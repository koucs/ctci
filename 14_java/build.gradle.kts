plugins {
    groovy
    java
}

group = "com.koucs"
version = "1.0-SNAPSHOT"

repositories {
    mavenCentral()
}

dependencies {
    implementation("org.codehaus.groovy:groovy-all:2.3.11")
    testImplementation("junit", "junit", "4.12")
}
