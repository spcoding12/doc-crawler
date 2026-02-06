# What is a container?

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

[Home](https://docs.docker.com/) / [Get started](https://docs.docker.com/get-started/) / [Docker concepts]() / [The basics]() / What is a container?

# What is a container?

Copy as Markdown

Open Markdown Ask Docs AI Claude Open in Claude

Table of contents

  * [Explanation](#explanation)
    * [Containers versus virtual machines (VMs)](#containers-versus-virtual-machines-vms)
  * [Try it out](#try-it-out)
  * [Additional resources](#additional-resources)
  * [Next steps](#next-steps)

* * *

## [Explanation](#explanation)

Imagine you're developing a killer web app that has three main components - a React frontend, a Python API, and a PostgreSQL database. If you wanted to work on this project, you'd have to install Node, Python, and PostgreSQL.

How do you make sure you have the same versions as the other developers on your team? Or your CI/CD system? Or what's used in production?

How do you ensure the version of Python (or Node or the database) your app needs isn't affected by what's already on your machine? How do you manage potential conflicts?

Enter containers!

What is a container? Simply put, containers are isolated processes for each of your app's components. Each component - the frontend React app, the Python API engine, and the database - runs in its own isolated environment, completely isolated from everything else on your machine.

Here's what makes them awesome. Containers are:

  * Self-contained. Each container has everything it needs to function with no reliance on any pre-installed dependencies on the host machine.
  * Isolated. Since containers run in isolation, they have minimal influence on the host and other containers, increasing the security of your applications.
  * Independent. Each container is independently managed. Deleting one container won't affect any others.
  * Portable. Containers can run anywhere! The container that runs on your development machine will work the same way in a data center or anywhere in the cloud!

### [Containers versus virtual machines (VMs)](#containers-versus-virtual-machines-vms)

Without getting too deep, a VM is an entire operating system with its own kernel, hardware drivers, programs, and applications. Spinning up a VM only to isolate a single application is a lot of overhead.

A container is simply an isolated process with all of the files it needs to run. If you run multiple containers, they all share the same kernel, allowing you to run more applications on less infrastructure.

> **Using VMs and containers together**
> 
> Quite often, you will see containers and VMs used together. As an example, in a cloud environment, the provisioned machines are typically VMs. However, instead of provisioning one machine to run one application, a VM with a container runtime can run multiple containerized applications, increasing resource utilization and reducing costs.

## [Try it out](#try-it-out)

In this hands-on, you will see how to run a Docker container using the Docker Desktop GUI.

Using the GUI  Using the CLI

Use the following instructions to run a container.

  1. Open Docker Desktop and select the **Search** field on the top navigation bar.

  2. Specify `welcome-to-docker` in the search input and then select the **Pull** button.

![A screenshot of the Docker Desktop Dashboard showing the search result for welcome-to-docker Docker image ](images/img_000_8db7093e.webp)

![A screenshot of the Docker Desktop Dashboard showing the search result for welcome-to-docker Docker image ](images/img_000_8db7093e.webp)

  3. Once the image is successfully pulled, select the **Run** button.

  4. Expand the **Optional settings**.

  5. In the **Container name** , specify `welcome-to-docker`.

  6. In the **Host port** , specify `8080`.

![A screenshot of Docker Desktop Dashboard showing the container run dialog with welcome-to-docker typed in as the container name and 8080 specified as the port number](images/img_001_632aee0f.webp)

![A screenshot of Docker Desktop Dashboard showing the container run dialog with welcome-to-docker typed in as the container name and 8080 specified as the port number](images/img_001_632aee0f.webp)

  7. Select **Run** to start your container.

Congratulations! You just ran your first container! ðŸŽ‰

### [View your container](#view-your-container)

You can view all of your containers by going to the **Containers** view of the Docker Desktop Dashboard.

![Screenshot of the container view of the Docker Desktop GUI showing the welcome-to-docker container running on the host port 8080](images/img_002_f8b3cc32.webp)

![Screenshot of the container view of the Docker Desktop GUI showing the welcome-to-docker container running on the host port 8080](images/img_002_f8b3cc32.webp)

This container runs a web server that displays a simple website. When working with more complex projects, you'll run different parts in different containers. For example, you might run a different container for the frontend, backend, and database.

### [Access the frontend](#access-the-frontend)

When you launched the container, you exposed one of the container's ports onto your machine. Think of this as creating configuration to let you to connect through the isolated environment of the container.

For this container, the frontend is accessible on port `8080`. To open the website, select the link in the **Port(s)** column of your container or visit <http://localhost:8080> in your browser.

![Screenshot of the landing page coming from the running container](images/img_003_3dfccc24.webp)

![Screenshot of the landing page coming from the running container](images/img_003_3dfccc24.webp)

### [Explore your container](#explore-your-container)

Docker Desktop lets you explore and interact with different aspects of your container. Try it out yourself.

  1. Go to the **Containers** view in the Docker Desktop Dashboard.

  2. Select your container.

  3. Select the **Files** tab to explore your container's isolated file system.

![Screenshot of the Docker Desktop Dashboard showing the files and directories inside a running container](images/img_004_09873b91.webp)

![Screenshot of the Docker Desktop Dashboard showing the files and directories inside a running container](images/img_004_09873b91.webp)

### [Stop your container](#stop-your-container)

The `docker/welcome-to-docker` container continues to run until you stop it.

  1. Go to the **Containers** view in the Docker Desktop Dashboard.

  2. Locate the container you'd like to stop.

  3. Select the **Stop** action in the **Actions** column.

![Screenshot of the Docker Desktop Dashboard with the welcome container selected and being prepared to stop](images/img_005_583863ef.webp)

![Screenshot of the Docker Desktop Dashboard with the welcome container selected and being prepared to stop](images/img_005_583863ef.webp)

Follow the instructions to run a container using the CLI:

  1. Open your CLI terminal and start a container by using the [`docker run`](/reference/cli/docker/container/run/) command:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         $ docker run -d -p 8080:80 docker/welcome-to-docker
         

The output from this command is the full container ID.

Congratulations! You just fired up your first container! ðŸŽ‰

### [View your running containers](#view-your-running-containers)

You can verify if the container is up and running by using the [`docker ps`](/reference/cli/docker/container/ls/) command:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
    
    
    docker ps
    

You will see output like the following:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
    
    
     CONTAINER ID   IMAGE                      COMMAND                  CREATED          STATUS          PORTS                      NAMES
     a1f7a4bb3a27   docker/welcome-to-docker   "/docker-entrypoint.â€¦"   11 seconds ago   Up 11 seconds   0.0.0.0:8080->80/tcp       gracious_keldysh
    

This container runs a web server that displays a simple website. When working with more complex projects, you'll run different parts in different containers. For example, a different container for the `frontend`, `backend`, and `database`.

> Tip
> 
> The `docker ps` command will show you _only_ running containers. To view stopped containers, add the `-a` flag to list all containers: `docker ps -a`

### [Access the frontend](#access-the-frontend)

When you launched the container, you exposed one of the container's ports onto your machine. Think of this as creating configuration to let you to connect through the isolated environment of the container.

For this container, the frontend is accessible on port `8080`. To open the website, select the link in the **Port(s)** column of your container or visit <http://localhost:8080> in your browser.

![Screenshot of the landing page of the Nginx web server, coming from the running container](images/img_003_3dfccc24.webp)

![Screenshot of the landing page of the Nginx web server, coming from the running container](images/img_003_3dfccc24.webp)

### [Stop your container](#stop-your-container)

The `docker/welcome-to-docker` container continues to run until you stop it. You can stop a container using the `docker stop` command.

  1. Run `docker ps` to get the ID of the container

  2. Provide the container ID or name to the [`docker stop`](/reference/cli/docker/container/stop/) command:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         docker stop <the-container-id>
         

> Tip
> 
> When referencing containers by ID, you don't need to provide the full ID. You only need to provide enough of the ID to make it unique. As an example, the previous container could be stopped by running the following command:
> 
> ]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
>     
>     
>     docker stop a1f
>     

## [Additional resources](#additional-resources)

The following links provide additional guidance into containers:

  * [Running a container](/engine/containers/run/)
  * [Overview of container](https://www.docker.com/resources/what-container/)
  * [Why Docker?](https://www.docker.com/why-docker/)

## [Next steps](#next-steps)

Now that you have learned the basics of a Docker container, it's time to learn about Docker images.

[What is an image?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-an-image/)

[Edit this page](https://github.com/docker/docs/edit/main/content/get-started/docker-concepts/the-basics/what-is-a-container.md)

[Request changes](https://github.com/docker/docs/issues/new?template=doc_issue.yml&location=https%3a%2f%2fdocs.docker.com%2fget-started%2fdocker-concepts%2fthe-basics%2fwhat-is-a-container%2f&labels=status%2Ftriage)

Table of contents

  * [Explanation](#explanation)
    * [Containers versus virtual machines (VMs)](#containers-versus-virtual-machines-vms)
  * [Try it out](#try-it-out)
  * [Additional resources](#additional-resources)
  * [Next steps](#next-steps)