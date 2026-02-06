# Publishing and exposing ports

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

[Home](https://docs.docker.com/) / [Get started](https://docs.docker.com/get-started/) / [Docker concepts]() / [Running containers]() / Publishing and exposing ports

# Publishing and exposing ports

Copy as Markdown

Open Markdown Ask Docs AI Claude Open in Claude

Table of contents

  * [Explanation](#explanation)
    * [Publishing ports](#publishing-ports)
    * [Publishing to ephemeral ports](#publishing-to-ephemeral-ports)
    * [Publishing all ports](#publishing-all-ports)
  * [Try it out](#try-it-out)
    * [Use the Docker CLI](#use-the-docker-cli)
    * [Use Docker Compose](#use-docker-compose)
  * [Additional resources](#additional-resources)
  * [Next steps](#next-steps)

* * *

## [Explanation](#explanation)

If you've been following the guides so far, you understand that containers provide isolated processes for each component of your application. Each component - a React frontend, a Python API, and a Postgres database - runs in its own sandbox environment, completely isolated from everything else on your host machine. This isolation is great for security and managing dependencies, but it also means you can’t access them directly. For example, you can’t access the web app in your browser.

That’s where port publishing comes in.

### [Publishing ports](#publishing-ports)

Publishing a port provides the ability to break through a little bit of networking isolation by setting up a forwarding rule. As an example, you can indicate that requests on your host’s port `8080` should be forwarded to the container’s port `80`. Publishing ports happens during container creation using the `-p` (or `--publish`) flag with `docker run`. The syntax is:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
    
    
    $ docker run -d -p HOST_PORT:CONTAINER_PORT nginx
    

  * `HOST_PORT`: The port number on your host machine where you want to receive traffic
  * `CONTAINER_PORT`: The port number within the container that's listening for connections

For example, to publish the container's port `80` to host port `8080`:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
    
    
    $ docker run -d -p 8080:80 nginx
    

Now, any traffic sent to port `8080` on your host machine will be forwarded to port `80` within the container.

> Important
> 
> When a port is published, it's published to all network interfaces by default. This means any traffic that reaches your machine can access the published application. Be mindful of publishing databases or any sensitive information. [Learn more about published ports here](/engine/network/#published-ports).

### [Publishing to ephemeral ports](#publishing-to-ephemeral-ports)

At times, you may want to simply publish the port but don’t care which host port is used. In these cases, you can let Docker pick the port for you. To do so, simply omit the `HOST_PORT` configuration.

For example, the following command will publish the container’s port `80` onto an ephemeral port on the host:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
    
    
    $ docker run -p 80 nginx
    

Once the container is running, using `docker ps` will show you the port that was chosen:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
    
    
    docker ps
    CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS          PORTS                    NAMES
    a527355c9c53   nginx         "/docker-entrypoint.…"   4 seconds ago    Up 3 seconds    0.0.0.0:54772->80/tcp    romantic_williamson
    

In this example, the app is exposed on the host at port `54772`.

### [Publishing all ports](#publishing-all-ports)

When creating a container image, the `EXPOSE` instruction is used to indicate the packaged application will use the specified port. These ports aren't published by default.

With the `-P` or `--publish-all` flag, you can automatically publish all exposed ports to ephemeral ports. This is quite useful when you’re trying to avoid port conflicts in development or testing environments.

For example, the following command will publish all of the exposed ports configured by the image:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
    
    
    $ docker run -P nginx
    

## [Try it out](#try-it-out)

In this hands-on guide, you'll learn how to publish container ports using both the CLI and Docker Compose for deploying a web application.

### [Use the Docker CLI](#use-the-docker-cli)

In this step, you will run a container and publish its port using the Docker CLI.

  1. [Download and install](/get-started/get-docker/) Docker Desktop.

  2. In a terminal, run the following command to start a new container:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         $ docker run -d -p 8080:80 docker/welcome-to-docker
         

The first `8080` refers to the host port. This is the port on your local machine that will be used to access the application running inside the container. The second `80` refers to the container port. This is the port that the application inside the container listens on for incoming connections. Hence, the command binds to port `8080` of the host to port `80` on the container system.

  3. Verify the published port by going to the **Containers** view of the Docker Desktop Dashboard.

![A screenshot of Docker Desktop Dashboard showing the published port](images/img_000_a7defec9.webp)

![A screenshot of Docker Desktop Dashboard showing the published port](images/img_000_a7defec9.webp)

  4. Open the website by either selecting the link in the **Port(s)** column of your container or visiting <http://localhost:8080> in your browser.

![A screenshot of the landing page of the Nginx web server running in a container](/get-started/docker-concepts/the-basics/images/access-the-frontend.webp?border=true)

![A screenshot of the landing page of the Nginx web server running in a container](/get-started/docker-concepts/the-basics/images/access-the-frontend.webp?border=true)

### [Use Docker Compose](#use-docker-compose)

This example will launch the same application using Docker Compose:

  1. Create a new directory and inside that directory, create a `compose.yaml` file with the following contents:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         services:
           app:
             image: docker/welcome-to-docker
             ports:
               - 8080:80

The `ports` configuration accepts a few different forms of syntax for the port definition. In this case, you’re using the same `HOST_PORT:CONTAINER_PORT` used in the `docker run` command.

  2. Open a terminal and navigate to the directory you created in the previous step.

  3. Use the `docker compose up` command to start the application.

  4. Open your browser to <http://localhost:8080>.

## [Additional resources](#additional-resources)

If you’d like to dive in deeper on this topic, be sure to check out the following resources:

  * [`docker container port` CLI reference](/reference/cli/docker/container/port/)
  * [Published ports](/engine/network/#published-ports)

## [Next steps](#next-steps)

Now that you understand how to publish and expose ports, you're ready to learn how to override the container defaults using the `docker run` command.

[Overriding container defaults](https://docs.docker.com/get-started/docker-concepts/running-containers/overriding-container-defaults/)

[Edit this page](https://github.com/docker/docs/edit/main/content/get-started/docker-concepts/running-containers/publishing-ports.md)

[Request changes](https://github.com/docker/docs/issues/new?template=doc_issue.yml&location=https%3a%2f%2fdocs.docker.com%2fget-started%2fdocker-concepts%2frunning-containers%2fpublishing-ports%2f&labels=status%2Ftriage)

Table of contents

  * [Explanation](#explanation)
    * [Publishing ports](#publishing-ports)
    * [Publishing to ephemeral ports](#publishing-to-ephemeral-ports)
    * [Publishing all ports](#publishing-all-ports)
  * [Try it out](#try-it-out)
    * [Use the Docker CLI](#use-the-docker-cli)
    * [Use Docker Compose](#use-docker-compose)
  * [Additional resources](#additional-resources)
  * [Next steps](#next-steps)