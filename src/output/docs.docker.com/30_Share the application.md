# Share the application

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

[Home](https://docs.docker.com/) / [Get started](https://docs.docker.com/get-started/) / [Docker workshop](https://docs.docker.com/get-started/workshop/) / Part 3: Share the application

# Share the application

Copy as Markdown

Open Markdown Ask Docs AI Claude Open in Claude

Table of contents

  * [Create a repository](#create-a-repository)
  * [Push the image](#push-the-image)
  * [Run the image on a new instance](#run-the-image-on-a-new-instance)
  * [Summary](#summary)
  * [Next steps](#next-steps)

* * *

Now that you've built an image, you can share it. To share Docker images, you have to use a Docker registry. The default registry is Docker Hub and is where all of the images you've used have come from.

> **Docker ID**
> 
> A Docker ID lets you access Docker Hub, which is the world's largest library and community for container images. Create a [Docker ID](https://hub.docker.com/signup) for free if you don't have one.

## [Create a repository](#create-a-repository)

To push an image, you first need to create a repository on Docker Hub.

  1. [Sign up](https://www.docker.com/pricing?utm_source=docker&utm_medium=webreferral&utm_campaign=docs_driven_upgrade) or Sign in to [Docker Hub](https://hub.docker.com).

  2. Select the **Create Repository** button.

  3. For the repository name, use `getting-started`. Make sure the **Visibility** is **Public**.

  4. Select **Create**.

In the following image, you can see an example Docker command from Docker Hub. This command will push to this repository.

![Docker command with push example](images/img_000_ef85d42a.webp)

![Docker command with push example](images/img_000_ef85d42a.webp)

## [Push the image](#push-the-image)

Let's try to push the image to Docker Hub.

  1. In the command line, run the following command:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         docker push docker/getting-started
         

You'll see an error like this:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         $ docker push docker/getting-started
         The push refers to repository [docker.io/docker/getting-started]
         An image does not exist locally with the tag: docker/getting-started
         

This failure is expected because the image isn't tagged correctly yet. Docker is looking for an image name `docker/getting-started`, but your local image is still named `getting-started`.

You can confirm this by running:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         docker image ls
         

  2. To fix this, first sign in to Docker Hub using your Docker ID: `docker login YOUR-USER-NAME`.

  3. Use the `docker tag` command to give the `getting-started` image a new name. Replace `YOUR-USER-NAME` with your Docker ID.

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         $ docker tag getting-started YOUR-USER-NAME/getting-started
         

  4. Now run the `docker push` command again. If you're copying the value from Docker Hub, you can drop the `tagname` part, as you didn't add a tag to the image name. If you don't specify a tag, Docker uses a tag called `latest`.

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         $ docker push YOUR-USER-NAME/getting-started
         

## [Run the image on a new instance](#run-the-image-on-a-new-instance)

Now that your image has been built and pushed into a registry, you can run your app on any machine that has Docker installed. Try pulling and running your image on another computer or a cloud instance.

## [Summary](#summary)

In this section, you learned how to share your images by pushing them to a registry. You then went to a brand new instance and were able to run the freshly pushed image. This is quite common in CI pipelines, where the pipeline will create the image and push it to a registry and then the production environment can use the latest version of the image.

Related information:

  * [docker CLI reference](/reference/cli/docker/)
  * [Multi-platform images](https://docs.docker.com/build/building/multi-platform/)
  * [Docker Hub overview](https://docs.docker.com/docker-hub/)

## [Next steps](#next-steps)

In the next section, you'll learn how to persist data in your containerized application.

[Persist the DB](https://docs.docker.com/get-started/workshop/05_persisting_data/)

[Edit this page](https://github.com/docker/docs/edit/main/content/get-started/workshop/04_sharing_app.md)

[Request changes](https://github.com/docker/docs/issues/new?template=doc_issue.yml&location=https%3a%2f%2fdocs.docker.com%2fget-started%2fworkshop%2f04_sharing_app%2f&labels=status%2Ftriage)

Table of contents

  * [Create a repository](#create-a-repository)
  * [Push the image](#push-the-image)
  * [Run the image on a new instance](#run-the-image-on-a-new-instance)
  * [Summary](#summary)
  * [Next steps](#next-steps)