# Get Docker Desktop

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

[Home](https://docs.docker.com/) / [Get started](https://docs.docker.com/get-started/) / [Introduction](https://docs.docker.com/get-started/introduction/) / Get Docker Desktop

# Get Docker Desktop

Copy as Markdown

Open Markdown Ask Docs AI Claude Open in Claude

Table of contents

  * [Explanation](#explanation)
  * [Try it out](#try-it-out)
  * [Run your first container](#run-your-first-container)
  * [Access the frontend](#access-the-frontend)
  * [Manage containers using Docker Desktop](#manage-containers-using-docker-desktop)
  * [What's next?](#whats-next)

* * *

## [Explanation](#explanation)

Docker Desktop is the all-in-one package to build images, run containers, and so much more. This guide will walk you through the installation process, enabling you to experience Docker Desktop firsthand.

> **Docker Desktop terms**
> 
> Commercial use of Docker Desktop in larger enterprises (more than 250 employees OR more than $10 million USD in annual revenue) requires a [paid subscription](https://www.docker.com/pricing/?_gl=1*1nyypal*_ga*MTYxMTUxMzkzOS4xNjgzNTM0MTcw*_ga_XJWPQMJYHQ*MTcxNjk4MzU4Mi4xMjE2LjEuMTcxNjk4MzkzNS4xNy4wLjA.).

### Docker Desktop for Mac

[Download (Apple Silicon)](https://desktop.docker.com/mac/main/arm64/Docker.dmg?utm_source=docker&utm_medium=webreferral&utm_campaign=docs-driven-download-mac-arm64) | [Download (Intel)](https://desktop.docker.com/mac/main/amd64/Docker.dmg?utm_source=docker&utm_medium=webreferral&utm_campaign=docs-driven-download-mac-amd64) | [Install instructions](/desktop/setup/install/mac-install)

### Docker Desktop for Windows

[Download](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe?utm_source=docker&utm_medium=webreferral&utm_campaign=docs-driven-download-windows) | [Install instructions](/desktop/setup/install/windows-install)

### Docker Desktop for Linux

[Install instructions](/desktop/setup/install/linux/)

Once it's installed, complete the setup process and you're all set to run a Docker container.

## [Try it out](#try-it-out)

In this hands-on guide, you will see how to run a Docker container using Docker Desktop.

Follow the instructions to run a container using the CLI.

## [Run your first container](#run-your-first-container)

Open your CLI terminal and start a container by running the `docker run` command:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
    
    
    $ docker run -d -p 8080:80 docker/welcome-to-docker
    

## [Access the frontend](#access-the-frontend)

For this container, the frontend is accessible on port `8080`. To open the website, visit <http://localhost:8080> in your browser.

![Screenshot of the landing page of the Nginx web server, coming from the running container](images/img_000_3dfccc24.webp)

![Screenshot of the landing page of the Nginx web server, coming from the running container](images/img_000_3dfccc24.webp)

## [Manage containers using Docker Desktop](#manage-containers-using-docker-desktop)

  1. Open Docker Desktop and select the **Containers** field on the left sidebar.

  2. You can view information about your container including logs, and files, and even access the shell by selecting the **Exec** tab.

![Screenshot of exec into the running container in Docker Desktop](images/img_001_6366562f.webp)

![Screenshot of exec into the running container in Docker Desktop](images/img_001_6366562f.webp)

  3. Select the **Inspect** field to obtain detailed information about the container. You can perform various actions such as pause, resume, start or stop containers, or explore the **Logs** , **Bind mounts** , **Exec** , **Files** , and **Stats** tabs.

![Screenshot of inspecting the running container in Docker Desktop](images/img_002_dd70bd93.webp)

![Screenshot of inspecting the running container in Docker Desktop](images/img_002_dd70bd93.webp)

Docker Desktop simplifies container management for developers by streamlining the setup, configuration, and compatibility of applications across different environments, thereby addressing the pain points of environment inconsistencies and deployment challenges.

## [What's next?](#whats-next)

Now that you have Docker Desktop installed and ran your first container, it's time to start developing with containers.

[Develop with containers](https://docs.docker.com/get-started/introduction/develop-with-containers/)

[Edit this page](https://github.com/docker/docs/edit/main/content/get-started/introduction/get-docker-desktop.md)

[Request changes](https://github.com/docker/docs/issues/new?template=doc_issue.yml&location=https%3a%2f%2fdocs.docker.com%2fget-started%2fintroduction%2fget-docker-desktop%2f&labels=status%2Ftriage)

Table of contents

  * [Explanation](#explanation)
  * [Try it out](#try-it-out)
  * [Run your first container](#run-your-first-container)
  * [Access the frontend](#access-the-frontend)
  * [Manage containers using Docker Desktop](#manage-containers-using-docker-desktop)
  * [What's next?](#whats-next)