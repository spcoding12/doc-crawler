# Building images

Back

[Get started](https://docs.docker.com/get-started/)

  * [Guides](/guides/)
  * [Manuals](/manuals/)
  * [Reference](/reference/)

  * [Get Docker](https://docs.docker.com/get-started/get-docker/ "Get Docker")
  * [What is Docker?](https://docs.docker.com/get-started/docker-overview/ "What is Docker?")
  * [Introduction](https://docs.docker.com/get-started/introduction/)

    * [Get Docker Desktop](https://docs.docker.com/get-started/introduction/get-docker-desktop/ "Get Docker Desktop")
    * [Develop with containers](https://docs.docker.com/get-started/introduction/develop-with-containers/ "Develop with containers")
    * [Build and push your first image](https://docs.docker.com/get-started/introduction/build-and-push-first-image/ "Build and push your first image")
    * [What's next](https://docs.docker.com/get-started/introduction/whats-next/ "What's next")
  * Docker concepts

    * The basics

      * [What is a container?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/ "What is a container?")
      * [What is an image?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-an-image/ "What is an image?")
      * [What is a registry?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-registry/ "What is a registry?")
      * [What is Docker Compose?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-docker-compose/ "What is Docker Compose?")
    * [Building images](https://docs.docker.com/get-started/docker-concepts/building-images/)

      * [Understanding the image layers](https://docs.docker.com/get-started/docker-concepts/building-images/understanding-image-layers/ "Understanding the image layers")
      * [Writing a Dockerfile](https://docs.docker.com/get-started/docker-concepts/building-images/writing-a-dockerfile/ "Writing a Dockerfile")
      * [Build, tag, and publish an image](https://docs.docker.com/get-started/docker-concepts/building-images/build-tag-and-publish-an-image/ "Build, tag, and publish an image")
      * [Using the build cache](https://docs.docker.com/get-started/docker-concepts/building-images/using-the-build-cache/ "Using the build cache")
      * [Multi-stage builds](https://docs.docker.com/get-started/docker-concepts/building-images/multi-stage-builds/ "Multi-stage builds")
    * Running containers

      * [Publishing and exposing ports](https://docs.docker.com/get-started/docker-concepts/running-containers/publishing-ports/ "Publishing and exposing ports")
      * [Overriding container defaults](https://docs.docker.com/get-started/docker-concepts/running-containers/overriding-container-defaults/ "Overriding container defaults")
      * [Persisting container data](https://docs.docker.com/get-started/docker-concepts/running-containers/persisting-container-data/ "Persisting container data")
      * [Sharing local files with containers](https://docs.docker.com/get-started/docker-concepts/running-containers/sharing-local-files/ "Sharing local files with containers")
      * [Multi-container applications](https://docs.docker.com/get-started/docker-concepts/running-containers/multi-container-applications/ "Multi-container applications")
  * [Docker workshop](https://docs.docker.com/get-started/workshop/)

    * [Part 1: Containerize an application](https://docs.docker.com/get-started/workshop/02_our_app/ "Part 1: Containerize an application")
    * [Part 2: Update the application](https://docs.docker.com/get-started/workshop/03_updating_app/ "Part 2: Update the application")
    * [Part 3: Share the application](https://docs.docker.com/get-started/workshop/04_sharing_app/ "Part 3: Share the application")
    * [Part 4: Persist the DB](https://docs.docker.com/get-started/workshop/05_persisting_data/ "Part 4: Persist the DB")
    * [Part 5: Use bind mounts](https://docs.docker.com/get-started/workshop/06_bind_mounts/ "Part 5: Use bind mounts")
    * [Part 6: Multi-container apps](https://docs.docker.com/get-started/workshop/07_multi_container/ "Part 6: Multi-container apps")
    * [Part 7: Use Docker Compose](https://docs.docker.com/get-started/workshop/08_using_compose/ "Part 7: Use Docker Compose")
    * [Part 8: Image-building best practices](https://docs.docker.com/get-started/workshop/09_image_best/ "Part 8: Image-building best practices")
    * [Part 9: What next](https://docs.docker.com/get-started/workshop/10_what_next/ "Part 9: What next")
  * [Educational resources](https://docs.docker.com/get-started/resources/ "Educational resources")

[Home](https://docs.docker.com/) / [Get started](https://docs.docker.com/get-started/) / [Docker concepts]() / Building images

# Building images

Building container images is both technical and an art. You want to keep the image small and focused to increase your security posture, but also need to balance potential tradeoffs, such as caching impacts. In this series, you’ll deep dive into the secrets of images, how they are built and best practices.

**Skill level** Beginner

**Time to complete** 25 minutes

**Prerequisites** None

## [About this series](#about-this-series)

Learn how to build production-ready images that are lean and efficient Docker images, essential for minimizing overhead and enhancing deployment in production environments.

## [What you'll learn](#what-youll-learn)

  * Understanding image layers
  * Writing a Dockerfile
  * Build, tag and publish an image
  * Using the build cache
  * Multi-stage builds

## [Modules](#modules)

1\. Understanding the image layers

Have you ever wondered how images work? This guide will help you to understand image layers - the fundamental building blocks of container images. You'll gain a comprehensive understanding of how layers are created, stacked, and utilized to ensure efficient and optimized containers.

[Start](https://docs.docker.com/get-started/docker-concepts/building-images/understanding-image-layers/)

2\. Writing a Dockerfile

Mastering Dockerfile practices is vital for leveraging container technology effectively, enhancing application reliability and supporting DevOps and CI/CD methodologies. In this guide, you’ll learn how to write a Dockerfile, how to define a base image and setup instructions, including software installation and copying necessary files.

[Start](https://docs.docker.com/get-started/docker-concepts/building-images/writing-a-dockerfile/)

3\. Build, tag, and publish an image

Building, tagging, and publishing Docker images are key steps in the containerization workflow. In this guide, you’ll learn how to create Docker images, how to tag those images with a unique identifier, and how to publish your image to a public registry.

[Start](https://docs.docker.com/get-started/docker-concepts/building-images/build-tag-and-publish-an-image/)

4\. Using the build cache

Using the build cache effectively allows you to achieve faster builds by reusing results from previous builds and skipping unnecessary steps. To maximize cache usage and avoid resource-intensive and time-consuming rebuilds, it's crucial to understand how cache invalidation works. In this guide, you’ll learn how to use the Docker build cache efficiently for streamlined Docker image development and continuous integration workflows.

[Start](https://docs.docker.com/get-started/docker-concepts/building-images/using-the-build-cache/)

5\. Multi-stage builds

By separating the build environment from the final runtime environment, you can significantly reduce the image size and attack surface. In this guide, you'll unlock the power of multi-stage builds to create lean and efficient Docker images, essential for minimizing overhead and enhancing deployment in production environments.

[Start](https://docs.docker.com/get-started/docker-concepts/building-images/multi-stage-builds/)