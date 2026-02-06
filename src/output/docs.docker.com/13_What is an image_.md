# What is an image?

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

[Home](https://docs.docker.com/) / [Get started](https://docs.docker.com/get-started/) / [Docker concepts]() / [The basics]() / What is an image?

# What is an image?

Copy as Markdown

Open Markdown Ask Docs AI Claude Open in Claude

Table of contents

  * [Explanation](#explanation)
    * [Finding images](#finding-images)
  * [Try it out](#try-it-out)
  * [Additional resources](#additional-resources)
  * [Next steps](#next-steps)

* * *

## [Explanation](#explanation)

Seeing as a [container](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/) is an isolated process, where does it get its files and configuration? How do you share those environments?

That's where container images come in. A container image is a standardized package that includes all of the files, binaries, libraries, and configurations to run a container.

For a [PostgreSQL](https://hub.docker.com/_/postgres) image, that image will package the database binaries, config files, and other dependencies. For a Python web app, it'll include the Python runtime, your app code, and all of its dependencies.

There are two important principles of images:

  1. Images are immutable. Once an image is created, it can't be modified. You can only make a new image or add changes on top of it.

  2. Container images are composed of layers. Each layer represents a set of file system changes that add, remove, or modify files.

These two principles let you to extend or add to existing images. For example, if you are building a Python app, you can start from the [Python image](https://hub.docker.com/_/python) and add additional layers to install your app's dependencies and add your code. This lets you focus on your app, rather than Python itself.

### [Finding images](#finding-images)

[Docker Hub](https://hub.docker.com) is the default global marketplace for storing and distributing images. It has over 100,000 images created by developers that you can run locally. You can search for Docker Hub images and run them directly from Docker Desktop.

Docker Hub provides a variety of Docker-supported and endorsed images known as Docker Trusted Content. These provide fully managed services or great starters for your own images. These include:

  * [Docker Official Images](https://hub.docker.com/search?badges=official) \- a curated set of Docker repositories, serve as the starting point for the majority of users, and are some of the most secure on Docker Hub
  * [Docker Hardened Images](https://hub.docker.com/hardened-images/catalog) \- minimal, secure, production-ready images with near-zero CVEs, designed to reduce attack surface and simplify compliance. Free and open source under Apache 2.0
  * [Docker Verified Publishers](https://hub.docker.com/search?badges=verified_publisher) \- high-quality images from commercial publishers verified by Docker
  * [Docker-Sponsored Open Source](https://hub.docker.com/search?badges=open_source) \- images published and maintained by open-source projects sponsored by Docker through Docker's open source program

For example, [Redis](https://hub.docker.com/_/redis) and [Memcached](https://hub.docker.com/_/memcached) are a few popular ready-to-go Docker Official Images. You can download these images and have these services up and running in a matter of seconds. There are also base images, like the [Node.js](https://hub.docker.com/_/node) Docker image, that you can use as a starting point and add your own files and configurations. For production workloads requiring enhanced security, Docker Hardened Images offer minimal variants of popular images like Node.js, Python, and Go.

## [Try it out](#try-it-out)

Using the GUI  Using the CLI

In this hands-on, you will learn how to search and pull a container image using the Docker Desktop GUI.

### [Search for and download an image](#search-for-and-download-an-image)

  1. Open the Docker Desktop Dashboard and select the **Images** view in the left-hand navigation menu.

![A screenshot of the Docker Desktop Dashboard showing the image view on the left sidebar](images/img_000_b4735772.webp)

![A screenshot of the Docker Desktop Dashboard showing the image view on the left sidebar](images/img_000_b4735772.webp)

  2. Select the **Search images to run** button. If you don't see it, select the _global search bar_ at the top of the screen.

![A screenshot of the Docker Desktop Dashboard showing the search ta](images/img_001_2d61164c.webp)

![A screenshot of the Docker Desktop Dashboard showing the search ta](images/img_001_2d61164c.webp)

  3. In the **Search** field, enter "welcome-to-docker". Once the search has completed, select the `docker/welcome-to-docker` image.

![A screenshot of the Docker Desktop Dashboard showing the search results for the docker/welcome-to-docker image](images/img_002_a4fa553f.webp)

![A screenshot of the Docker Desktop Dashboard showing the search results for the docker/welcome-to-docker image](images/img_002_a4fa553f.webp)

  4. Select **Pull** to download the image.

### [Learn about the image](#learn-about-the-image)

Once you have an image downloaded, you can learn quite a few details about the image either through the GUI or the CLI.

  1. In the Docker Desktop Dashboard, select the **Images** view.

  2. Select the **docker/welcome-to-docker** image to open details about the image.

![A screenshot of the Docker Desktop Dashboard showing the images view with an arrow pointing to the docker/welcome-to-docker image](images/img_003_ea7d357c.webp)

![A screenshot of the Docker Desktop Dashboard showing the images view with an arrow pointing to the docker/welcome-to-docker image](images/img_003_ea7d357c.webp)

  3. The image details page presents you with information regarding the layers of the image, the packages and libraries installed in the image, and any discovered vulnerabilities.

![A screenshot of the image details view for the docker/welcome-to-docker image](images/img_004_78215616.webp)

![A screenshot of the image details view for the docker/welcome-to-docker image](images/img_004_78215616.webp)

Follow the instructions to search and pull a Docker image using CLI to view its layers.

### [Search for and download an image](#search-for-and-download-an-image)

  1. Open a terminal and search for images using the [`docker search`](https://docs.docker.com/reference/cli/docker/search/) command:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         docker search docker/welcome-to-docker
         

You will see output like the following:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         NAME                       DESCRIPTION                                     STARS     OFFICIAL
         docker/welcome-to-docker   Docker image for new users getting started w…   20
         

This output shows you information about relevant images available on Docker Hub.

  2. Pull the image using the [`docker pull`](https://docs.docker.com/reference/cli/docker/image/pull/) command.

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         docker pull docker/welcome-to-docker
         

You will see output like the following:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         Using default tag: latest
         latest: Pulling from docker/welcome-to-docker
         579b34f0a95b: Download complete
         d11a451e6399: Download complete
         1c2214f9937c: Download complete
         b42a2f288f4d: Download complete
         54b19e12c655: Download complete
         1fb28e078240: Download complete
         94be7e780731: Download complete
         89578ce72c35: Download complete
         Digest: sha256:eedaff45e3c78538087bdd9dc7afafac7e110061bbdd836af4104b10f10ab693
         Status: Downloaded newer image for docker/welcome-to-docker:latest
         docker.io/docker/welcome-to-docker:latest
         

Each of line represents a different downloaded layer of the image. Remember that each layer is a set of filesystem changes and provides functionality of the image.

### [Learn about the image](#learn-about-the-image)

  1. List your downloaded images using the [`docker image ls`](https://docs.docker.com/reference/cli/docker/image/ls/) command:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         docker image ls
         

You will see output like the following:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         REPOSITORY                 TAG       IMAGE ID       CREATED        SIZE
         docker/welcome-to-docker   latest    eedaff45e3c7   4 months ago   29.7MB
         

The command shows a list of Docker images currently available on your system. The `docker/welcome-to-docker` has a total size of approximately 29.7MB.

> **Image size**
> 
> The image size represented here reflects the uncompressed size of the image, not the download size of the layers.

  2. List the image's layers using the [`docker image history`](https://docs.docker.com/reference/cli/docker/image/history/) command:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         docker image history docker/welcome-to-docker
         

You will see output like the following:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         IMAGE          CREATED        CREATED BY                                      SIZE      COMMENT
         648f93a1ba7d   4 months ago   COPY /app/build /usr/share/nginx/html # buil…   1.6MB     buildkit.dockerfile.v0
         <missing>      5 months ago   /bin/sh -c #(nop)  CMD ["nginx" "-g" "daemon…   0B
         <missing>      5 months ago   /bin/sh -c #(nop)  STOPSIGNAL SIGQUIT           0B
         <missing>      5 months ago   /bin/sh -c #(nop)  EXPOSE 80                    0B
         <missing>      5 months ago   /bin/sh -c #(nop)  ENTRYPOINT ["/docker-entr…   0B
         <missing>      5 months ago   /bin/sh -c #(nop) COPY file:9e3b2b63db9f8fc7…   4.62kB
         <missing>      5 months ago   /bin/sh -c #(nop) COPY file:57846632accc8975…   3.02kB
         <missing>      5 months ago   /bin/sh -c #(nop) COPY file:3b1b9915b7dd898a…   298B
         <missing>      5 months ago   /bin/sh -c #(nop) COPY file:caec368f5a54f70a…   2.12kB
         <missing>      5 months ago   /bin/sh -c #(nop) COPY file:01e75c6dd0ce317d…   1.62kB
         <missing>      5 months ago   /bin/sh -c set -x     && addgroup -g 101 -S …   9.7MB
         <missing>      5 months ago   /bin/sh -c #(nop)  ENV PKG_RELEASE=1            0B
         <missing>      5 months ago   /bin/sh -c #(nop)  ENV NGINX_VERSION=1.25.3     0B
         <missing>      5 months ago   /bin/sh -c #(nop)  LABEL maintainer=NGINX Do…   0B
         <missing>      5 months ago   /bin/sh -c #(nop)  CMD ["/bin/sh"]              0B
         <missing>      5 months ago   /bin/sh -c #(nop) ADD file:ff3112828967e8004…   7.66MB
         

This output shows you all of the layers, their sizes, and the command used to create the layer.

> **Viewing the full command**
> 
> If you add the `--no-trunc` flag to the command, you will see the full command. Note that, since the output is in a table-like format, longer commands will cause the output to be very difficult to navigate.

In this walkthrough, you searched and pulled a Docker image. In addition to pulling a Docker image, you also learned about the layers of a Docker Image.

## [Additional resources](#additional-resources)

The following resources will help you learn more about exploring, finding, and building images:

  * [Docker trusted content](https://docs.docker.com/docker-hub/image-library/trusted-content/)
  * [Explore the Image view in Docker Desktop](https://docs.docker.com/desktop/use-desktop/images/)
  * [Docker Build overview](https://docs.docker.com/build/concepts/overview/)
  * [Docker Hub](https://hub.docker.com)

## [Next steps](#next-steps)

Now that you have learned the basics of images, it's time to learn about distributing images through registries.

[What is a registry?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-registry/)

[Edit this page](https://github.com/docker/docs/edit/main/content/get-started/docker-concepts/the-basics/what-is-an-image.md)

[Request changes](https://github.com/docker/docs/issues/new?template=doc_issue.yml&location=https%3a%2f%2fdocs.docker.com%2fget-started%2fdocker-concepts%2fthe-basics%2fwhat-is-an-image%2f&labels=status%2Ftriage)

Table of contents

  * [Explanation](#explanation)
    * [Finding images](#finding-images)
  * [Try it out](#try-it-out)
  * [Additional resources](#additional-resources)
  * [Next steps](#next-steps)