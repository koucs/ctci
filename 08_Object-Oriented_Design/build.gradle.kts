/*
 * This file was generated by the Gradle 'init' task.
 *
 * This is a general purpose Gradle build.
 * Learn how to create Gradle builds at https://guides.gradle.org/creating-new-gradle-builds
 */
plugins {
//    val springBootVersion = "2.2.0.RELEASE"
//    id("org.springframework.boot") version springBootVersion
//    id("io.spring.dependency-management") version "1.0.8.RELEASE"
    id("java")
    application
}

version = "1.0.0-SNAPSHOT"

application {
    mainClassName = "q8_1.Application"
}

dependencies {
//    implementation("com.graphql-java:graphql-java:14.0") // NEW
//    implementation("com.graphql-java:graphql-java-spring-boot-starter-webmvc:1.0") // NEW
//    implementation("com.google.guava:guava:26.0-jre") // NEW
//    implementation("org.springframework.boot:spring-boot-starter-web")
//    testImplementation("org.springframework.boot:spring-boot-starter-test")
}

repositories {
    jcenter()
}