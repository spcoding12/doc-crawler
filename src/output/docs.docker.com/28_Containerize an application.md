# Containerize an application

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

[Home](https://docs.docker.com/) / [Get started](https://docs.docker.com/get-started/) / [Docker workshop](https://docs.docker.com/get-started/workshop/) / Part 1: Containerize an application

# Containerize an application

Copy as Markdown

Open Markdown Ask Docs AI Claude Open in Claude

Table of contents

  * [Prerequisites](#prerequisites)
  * [Get the app](#get-the-app)
  * [Build the app's image](#build-the-apps-image)
  * [Start an app container](#start-an-app-container)
  * [Summary](#summary)
  * [Next steps](#next-steps)

* * *

For the rest of this guide, you'll be working with a simple todo list manager that runs on Node.js. If you're not familiar with Node.js, don't worry. This guide doesn't require any prior experience with JavaScript.

## [Prerequisites](#prerequisites)

  * You have installed the latest version of [Docker Desktop](https://docs.docker.com/get-started/get-docker/).
  * You have installed a [Git client](https://git-scm.com/downloads).
  * You have an IDE or a text editor to edit files. Docker recommends using [Visual Studio Code](https://code.visualstudio.com/).

## [Get the app](#get-the-app)

Before you can run the application, you need to get the application source code onto your machine.

  1. Clone the [getting-started-app repository](https://github.com/docker/getting-started-app/tree/main) using the following command:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         $ git clone https://github.com/docker/getting-started-app.git
         

  2. View the contents of the cloned repository. You should see the following files and sub-directories.

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         ├── getting-started-app/
         │ ├── .dockerignore
         │ ├── package.json
         │ ├── package-lock.json   
         │ ├── README.md
         │ ├── spec/
         │ ├── src/

## [Build the app's image](#build-the-apps-image)

To build the image, you'll need to use a Dockerfile. A Dockerfile is simply a text-based file with no file extension that contains a script of instructions. Docker uses this script to build a container image.

  1. In the `getting-started-app` directory, the same location as the `package.json` file, create a file named `Dockerfile` with the following contents:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         # syntax=docker/dockerfile:1
         
         FROM node:24-alpine
         WORKDIR /app
         COPY . .
         RUN npm install --omit=dev
         CMD ["node", "src/index.js"]
         EXPOSE 3000

This Dockerfile does the following:

     * Uses `node:24-alpine` as the base image, a lightweight Linux image with Node.js pre-installed
     * Sets `/app` as the working directory
     * Copies source code into the image
     * Installs the necessary dependencies
     * Specifies the command to start the application
     * Documents that the app listens on port 3000
  2. Build the image using the following commands:

In the terminal, make sure you're in the `getting-started-app` directory. Replace `/path/to/getting-started-app` with the path to your `getting-started-app` directory.

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         $ cd /path/to/getting-started-app
         

Build the image.

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         $ docker build -t getting-started .
         

The `docker build` command uses the Dockerfile to build a new image. You might have noticed that Docker downloaded a lot of "layers". This is because you instructed the builder that you wanted to start from the `node:24-alpine` image. But, since you didn't have that on your machine, Docker needed to download the image.

After Docker downloaded the image, the instructions from the Dockerfile copied in your application and used `npm` to install your application's dependencies.

Finally, the `-t` flag tags your image. Think of this as a human-readable name for the final image. Since you named the image `getting-started`, you can refer to that image when you run a container.

The `.` at the end of the `docker build` command tells Docker that it should look for the `Dockerfile` in the current directory.

## [Start an app container](#start-an-app-container)

Now that you have an image, you can run the application in a container using the `docker run` command.

  1. Run your container using the `docker run` command and specify the name of the image you just created:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         $ docker run -d -p 127.0.0.1:3000:3000 getting-started
         

The `-d` flag (short for `--detach`) runs the container in the background. This means that Docker starts your container and returns you to the terminal prompt. Also, it does not display logs in the terminal.

The `-p` flag (short for `--publish`) creates a port mapping between the host and the container. The `-p` flag takes a string value in the format of `HOST:CONTAINER`, where `HOST` is the address on the host, and `CONTAINER` is the port on the container. The command publishes the container's port 3000 to `127.0.0.1:3000` (`localhost:3000`) on the host. Without the port mapping, you wouldn't be able to access the application from the host.

  2. After a few seconds, open your web browser to <http://localhost:3000>. You should see your app.

![Empty todo list](images/img_000_54b2a1b8.webp)

![Empty todo list](images/img_000_54b2a1b8.webp)

  3. Add an item or two and see that it works as you expect. You can mark items as complete and remove them. Your frontend is successfully storing items in the backend.

At this point, you have a running todo list manager with a few items.

If you take a quick look at your containers, you should see at least one container running that's using the `getting-started` image and on port `3000`. To see your containers, you can use the CLI or Docker Desktop's graphical interface.

CLI  Docker Desktop

Run the `docker ps` command in a terminal to list your containers.

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
    
    
    $ docker ps
    

Output similar to the following should appear.

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
    
    
    CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                      NAMES
    df784548666d        getting-started     "docker-entrypoint.s…"   2 minutes ago       Up 2 minutes        127.0.0.1:3000->3000/tcp   priceless_mcclintock
    

In Docker Desktop, select the **Containers** tab to see a list of your containers.

![Docker Desktop with get-started container running](images/img_001_3e4deb82.webp)

![Docker Desktop with get-started container running](images/img_001_3e4deb82.webp)

## [Summary](#summary)

In this section, you learned the basics about creating a Dockerfile to build an image. Once you built an image, you started a container and saw the running app.

Related information:

  * [Dockerfile reference](/reference/dockerfile/)
  * [docker CLI reference](/reference/cli/docker/)

## [Next steps](#next-steps)

Next, you're going to make a modification to your app and learn how to update your running application with a new image. Along the way, you'll learn a few other useful commands.

[Update the application](https://docs.docker.com/get-started/workshop/03_updating_app/)

[Edit this page](https://github.com/docker/docs/edit/main/content/get-started/workshop/02_our_app.md)

[Request changes](https://github.com/docker/docs/issues/new?template=doc_issue.yml&location=https%3a%2f%2fdocs.docker.com%2fget-started%2fworkshop%2f02_our_app%2f&labels=status%2Ftriage)

Table of contents

  * [Prerequisites](#prerequisites)
  * [Get the app](#get-the-app)
  * [Build the app's image](#build-the-apps-image)
  * [Start an app container](#start-an-app-container)
  * [Summary](#summary)
  * [Next steps](#next-steps)