# Writing a Dockerfile

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

[Home](https://docs.docker.com/) / [Get started](https://docs.docker.com/get-started/) / [Docker concepts]() / [Building images](https://docs.docker.com/get-started/docker-concepts/building-images/) / Writing a Dockerfile

# Writing a Dockerfile

Copy as Markdown

Open Markdown Ask Docs AI Claude Open in Claude

Table of contents

  * [Explanation](#explanation)
    * [Common instructions](#common-instructions)
  * [Try it out](#try-it-out)
    * [Set up](#set-up)
    * [Creating the Dockerfile](#creating-the-dockerfile)
  * [Additional resources](#additional-resources)
  * [Next steps](#next-steps)

* * *

## [Explanation](#explanation)

A Dockerfile is a text-based document that's used to create a container image. It provides instructions to the image builder on the commands to run, files to copy, startup command, and more.

As an example, the following Dockerfile would produce a ready-to-run Python application:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
    
    
    FROM python:3.13
    WORKDIR /usr/local/app
    
    # Install the application dependencies
    COPY requirements.txt ./
    RUN pip install --no-cache-dir -r requirements.txt
    
    # Copy in the source code
    COPY src ./src
    EXPOSE 8080
    
    # Setup an app user so the container doesn't run as the root user
    RUN useradd app
    USER app
    
    CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

### [Common instructions](#common-instructions)

Some of the most common instructions in a `Dockerfile` include:

  * `FROM <image>` \- this specifies the base image that the build will extend.
  * `WORKDIR <path>` \- this instruction specifies the "working directory" or the path in the image where files will be copied and commands will be executed.
  * `COPY <host-path> <image-path>` \- this instruction tells the builder to copy files from the host and put them into the container image.
  * `RUN <command>` \- this instruction tells the builder to run the specified command.
  * `ENV <name> <value>` \- this instruction sets an environment variable that a running container will use.
  * `EXPOSE <port-number>` \- this instruction sets configuration on the image that indicates a port the image would like to expose.
  * `USER <user-or-uid>` \- this instruction sets the default user for all subsequent instructions.
  * `CMD ["<command>", "<arg1>"]` \- this instruction sets the default command a container using this image will run.

To read through all of the instructions or go into greater detail, check out the [Dockerfile reference](https://docs.docker.com/engine/reference/builder/).

## [Try it out](#try-it-out)

Just as you saw with the previous example, a Dockerfile typically follows these steps:

  1. Determine your base image
  2. Install application dependencies
  3. Copy in any relevant source code and/or binaries
  4. Configure the final image

In this quick hands-on guide, you'll write a Dockerfile that builds a simple Node.js application. If you're not familiar with JavaScript-based applications, don't worry. It isn't necessary for following along with this guide.

### [Set up](#set-up)

[Download this ZIP file](https://github.com/docker/getting-started-todo-app/archive/refs/heads/build-image-from-scratch.zip) and extract the contents into a directory on your machine.

If you'd rather not download a ZIP file, clone the <https://github.com/docker/getting-started-todo-app> project and checkout the `build-image-from-scratch` branch.

### [Creating the Dockerfile](#creating-the-dockerfile)

Now that you have the project, you’re ready to create the `Dockerfile`.

  1. [Download and install](https://www.docker.com/products/docker-desktop/) Docker Desktop.

  2. Examine the project.

Explore the contents of `getting-started-todo-app/app/`. You'll notice that a `Dockerfile` already exists. It is a simple text file that you can open in any text or code editor.

  3. Delete the existing `Dockerfile`.

For this exercise, you'll pretend you're starting from scratch and will create a new `Dockerfile`.

  4. Create a file named `Dockerfile` in the `getting-started-todo-app/app/` folder.

> **Dockerfile file extensions**
> 
> It's important to note that the `Dockerfile` has _no_ file extension. Some editors will automatically add an extension to the file (or complain it doesn't have one).

  5. In the `Dockerfile`, define your base image by adding the following line:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         FROM node:22-alpine

  6. Now, define the working directory by using the `WORKDIR` instruction. This will specify where future commands will run and the directory files will be copied inside the container image.

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         WORKDIR /app

  7. Copy all of the files from your project on your machine into the container image by using the `COPY` instruction:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         COPY . .

  8. Install the app's dependencies by using the `yarn` CLI and package manager. To do so, run a command using the `RUN` instruction:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         RUN yarn install --production

  9. Finally, specify the default command to run by using the `CMD` instruction:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         CMD ["node", "./src/index.js"]

And with that, you should have the following Dockerfile:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         FROM node:22-alpine
         WORKDIR /app
         COPY . .
         RUN yarn install --production
         CMD ["node", "./src/index.js"]

> **This Dockerfile isn't production-ready yet**
> 
> It's important to note that this Dockerfile is _not_ following all of the best practices yet (by design). It will build the app, but the builds won't be as fast, or the images as secure, as they could be.
> 
> Keep reading to learn more about how to make the image maximize the build cache, run as a non-root user, and multi-stage builds.

> **Containerize new projects quickly with`docker init`**
> 
> The `docker init` command will analyze your project and quickly create a Dockerfile, a `compose.yaml`, and a `.dockerignore`, helping you get up and going. Since you're learning about Dockerfiles specifically here, you won't use it now. But, [learn more about it here](/engine/reference/commandline/init/).

## [Additional resources](#additional-resources)

To learn more about writing a Dockerfile, visit the following resources:

  * [Dockerfile reference](/reference/dockerfile/)
  * [Dockerfile best practices](/develop/develop-images/dockerfile_best-practices/)
  * [Base images](/build/building/base-images/)
  * [Getting started with Docker Init](/reference/cli/docker/init/)

## [Next steps](#next-steps)

Now that you have created a Dockerfile and learned the basics, it's time to learn about building, tagging, and pushing the images.

[Build, tag and publish the Image](https://docs.docker.com/get-started/docker-concepts/building-images/build-tag-and-publish-an-image/)

[Edit this page](https://github.com/docker/docs/edit/main/content/get-started/docker-concepts/building-images/writing-a-dockerfile.md)

[Request changes](https://github.com/docker/docs/issues/new?template=doc_issue.yml&location=https%3a%2f%2fdocs.docker.com%2fget-started%2fdocker-concepts%2fbuilding-images%2fwriting-a-dockerfile%2f&labels=status%2Ftriage)

Table of contents

  * [Explanation](#explanation)
    * [Common instructions](#common-instructions)
  * [Try it out](#try-it-out)
    * [Set up](#set-up)
    * [Creating the Dockerfile](#creating-the-dockerfile)
  * [Additional resources](#additional-resources)
  * [Next steps](#next-steps)