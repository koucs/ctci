plugins {
    java
}

group = "com.koucs"
version = "1.0-SNAPSHOT"

repositories {
    mavenCentral()
}

dependencies {
    testImplementation("junit", "junit", "4.12")
    implementation("com.google.guava", "guava", "30.1.1-jre" )
}
