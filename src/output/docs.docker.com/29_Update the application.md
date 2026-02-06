# Update the application

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

[Home](https://docs.docker.com/) / [Get started](https://docs.docker.com/get-started/) / [Docker workshop](https://docs.docker.com/get-started/workshop/) / Part 2: Update the application

# Update the application

Copy as Markdown

Open Markdown Ask Docs AI Claude Open in Claude

Table of contents

  * [Update the source code](#update-the-source-code)
  * [Remove the old container](#remove-the-old-container)
    * [Start the updated app container](#start-the-updated-app-container)
  * [Summary](#summary)
  * [Next steps](#next-steps)

* * *

In [part 1](https://docs.docker.com/get-started/workshop/02_our_app/), you containerized a todo application. In this part, you'll update the application and image. You'll also learn how to stop and remove a container.

## [Update the source code](#update-the-source-code)

In the following steps, you'll change the "empty text" when you don't have any todo list items to "You have no todo items yet! Add one above!"

  1. In the `src/static/js/app.js` file, update line 56 to use the new empty text.

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         - <p className="text-center">No items yet! Add one above!</p>
         + <p className="text-center">You have no todo items yet! Add one above!</p>
         

  2. Build your updated version of the image, using the `docker build` command.

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         $ docker build -t getting-started .
         

  3. Start a new container using the updated code.

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         $ docker run -dp 127.0.0.1:3000:3000 getting-started
         

You probably saw an error like this:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
    
    
    docker: Error response from daemon: driver failed programming external connectivity on endpoint laughing_burnell 
    (bb242b2ca4d67eba76e79474fb36bb5125708ebdabd7f45c8eaf16caaabde9dd): Bind for 127.0.0.1:3000 failed: port is already allocated.
    

The error occurred because you aren't able to start the new container while your old container is still running. The reason is that the old container is already using the host's port 3000 and only one process on the machine (containers included) can listen to a specific port. To fix this, you need to remove the old container.

## [Remove the old container](#remove-the-old-container)

To remove a container, you first need to stop it. Once it has stopped, you can remove it. You can remove the old container using the CLI or Docker Desktop's graphical interface. Choose the option that you're most comfortable with.

CLI  Docker Desktop

### [Remove a container using the CLI](#remove-a-container-using-the-cli)

  1. Get the ID of the container by using the `docker ps` command.

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         $ docker ps
         

  2. Use the `docker stop` command to stop the container. Replace `<the-container-id>` with the ID from `docker ps`.

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         $ docker stop <the-container-id>
         

  3. Once the container has stopped, you can remove it by using the `docker rm` command.

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         $ docker rm <the-container-id>
         

> Note
> 
> You can stop and remove a container in a single command by adding the `force` flag to the `docker rm` command. For example: `docker rm -f <the-container-id>`

### [Remove a container using Docker Desktop](#remove-a-container-using-docker-desktop)

  1. Open Docker Desktop to the **Containers** view.
  2. Select the trash can icon under the **Actions** column for the container that you want to delete.
  3. In the confirmation dialog, select **Delete forever**.

### [Start the updated app container](#start-the-updated-app-container)

  1. Now, start your updated app using the `docker run` command.

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         $ docker run -dp 127.0.0.1:3000:3000 getting-started
         

  2. Refresh your browser on <http://localhost:3000> and you should see your updated help text.

## [Summary](#summary)

In this section, you learned how to update and rebuild an image, as well as how to stop and remove a container.

Related information:

  * [docker CLI reference](/reference/cli/docker/)

## [Next steps](#next-steps)

Next, you'll learn how to share images with others.

[Share the application](https://docs.docker.com/get-started/workshop/04_sharing_app/)

[Edit this page](https://github.com/docker/docs/edit/main/content/get-started/workshop/03_updating_app.md)

[Request changes](https://github.com/docker/docs/issues/new?template=doc_issue.yml&location=https%3a%2f%2fdocs.docker.com%2fget-started%2fworkshop%2f03_updating_app%2f&labels=status%2Ftriage)

Table of contents

  * [Update the source code](#update-the-source-code)
  * [Remove the old container](#remove-the-old-container)
    * [Start the updated app container](#start-the-updated-app-container)
  * [Summary](#summary)
  * [Next steps](#next-steps)