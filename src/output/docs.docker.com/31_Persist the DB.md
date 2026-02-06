# Persist the DB

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

[Home](https://docs.docker.com/) / [Get started](https://docs.docker.com/get-started/) / [Docker workshop](https://docs.docker.com/get-started/workshop/) / Part 4: Persist the DB

# Persist the DB

Copy as Markdown

Open Markdown Ask Docs AI Claude Open in Claude

Table of contents

  * [The container's filesystem](#the-containers-filesystem)
    * [See this in practice](#see-this-in-practice)
  * [Container volumes](#container-volumes)
  * [Persist the todo data](#persist-the-todo-data)
    * [Create a volume and start the container](#create-a-volume-and-start-the-container)
    * [Verify that the data persists](#verify-that-the-data-persists)
  * [Dive into the volume](#dive-into-the-volume)
  * [Summary](#summary)
  * [Next steps](#next-steps)

* * *

In case you didn't notice, your todo list is empty every single time you launch the container. Why is this? In this part, you'll dive into how the container is working.

## [The container's filesystem](#the-containers-filesystem)

When a container runs, it uses the various layers from an image for its filesystem. Each container also gets its own "scratch space" to create/update/remove files. Any changes won't be seen in another container, even if they're using the same image.

### [See this in practice](#see-this-in-practice)

To see this in action, you're going to start two containers. In one container, you'll create a file. In the other container, you'll check whether that same file exists.

  1. Start an Alpine container and create a new file in it.

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         $ docker run --rm alpine touch greeting.txt
         

> Tip
> 
> Any commands you specify after the image name (in this case, `alpine`) are executed inside the container. In this case, the command `touch greeting.txt` puts a file named `greeting.txt` on the container's filesystem.

  2. Run a new Alpine container and use the `stat` command to check whether the file exists.

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         $ docker run --rm alpine stat greeting.txt
         

You should see output similar to the following that indicates the file does not exist in the new container.

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         stat: can't stat 'greeting.txt': No such file or directory
         

The `greeting.txt` file created by the first container did not exist in the second container. That is because the writeable "top layer" of each container is isolated. Even though both containers shared the same underlying layers that make up the base image, the writable layer is unique to each container.

## [Container volumes](#container-volumes)

With the previous experiment, you saw that each container starts from the image definition each time it starts. While containers can create, update, and delete files, those changes are lost when you remove the container and Docker isolates all changes to that container. With volumes, you can change all of this.

[Volumes](https://docs.docker.com/engine/storage/volumes/) provide the ability to connect specific filesystem paths of the container back to the host machine. If you mount a directory in the container, changes in that directory are also seen on the host machine. If you mount that same directory across container restarts, you'd see the same files.

There are two main types of volumes. You'll eventually use both, but you'll start with volume mounts.

## [Persist the todo data](#persist-the-todo-data)

By default, the todo app stores its data in a SQLite database at `/etc/todos/todo.db` in the container's filesystem. If you're not familiar with SQLite, no worries! It's simply a relational database that stores all the data in a single file. While this isn't the best for large-scale applications, it works for small demos. You'll learn how to switch this to a different database engine later.

With the database being a single file, if you can persist that file on the host and make it available to the next container, it should be able to pick up where the last one left off. By creating a volume and attaching (often called "mounting") it to the directory where you stored the data, you can persist the data. As your container writes to the `todo.db` file, it will persist the data to the host in the volume.

As mentioned, you're going to use a volume mount. Think of a volume mount as an opaque bucket of data. Docker fully manages the volume, including the storage location on disk. You only need to remember the name of the volume.

### [Create a volume and start the container](#create-a-volume-and-start-the-container)

You can create the volume and start the container using the CLI or Docker Desktop's graphical interface.

CLI  Docker Desktop

  1. Create a volume by using the `docker volume create` command.

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         $ docker volume create todo-db
         

  2. Stop and remove the todo app container once again with `docker rm -f <id>`, as it is still running without using the persistent volume.

  3. Start the todo app container, but add the `--mount` option to specify a volume mount. Give the volume a name, and mount it to `/etc/todos` in the container, which captures all files created at the path.

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         $ docker run -dp 127.0.0.1:3000:3000 --mount type=volume,src=todo-db,target=/etc/todos getting-started
         

> Note
> 
> If you're using Git Bash, you must use different syntax for this command.
> 
> ]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
>          
>          $ docker run -dp 127.0.0.1:3000:3000 --mount type=volume,src=todo-db,target=//etc/todos getting-started
>          
> 
> For more details about Git Bash's syntax differences, see [Working with Git Bash](/desktop/troubleshoot-and-support/troubleshoot/topics/#docker-commands-failing-in-git-bash).

To create a volume:

  1. Select **Volumes** in Docker Desktop.
  2. In **Volumes** , select **Create**.
  3. Specify `todo-db` as the volume name, and then select **Create**.

To stop and remove the app container:

  1. Select **Containers** in Docker Desktop.
  2. Select **Delete** in the **Actions** column for the container.

To start the todo app container with the volume mounted:

  1. Select the search box at the top of Docker Desktop.

  2. In the search window, select the **Images** tab.

  3. In the search box, specify the image name, `getting-started`.

> Tip
> 
> Use the search filter to filter images and only show **Local images**.

  4. Select your image and then select **Run**.

  5. Select **Optional settings**.

  6. In **Host port** , specify the port, for example, `3000`.

  7. In **Host path** , specify the name of the volume, `todo-db`.

  8. In **Container path** , specify `/etc/todos`.

  9. Select **Run**.

### [Verify that the data persists](#verify-that-the-data-persists)

  1. Once the container starts up, open the app and add a few items to your todo list.

![Items added to todo list](images/img_000_b0304acf.webp)

![Items added to todo list](images/img_000_b0304acf.webp)

  2. Stop and remove the container for the todo app. Use Docker Desktop or `docker ps` to get the ID and then `docker rm -f <id>` to remove it.

  3. Start a new container using the previous steps.

  4. Open the app. You should see your items still in your list.

  5. Go ahead and remove the container when you're done checking out your list.

You've now learned how to persist data.

## [Dive into the volume](#dive-into-the-volume)

A lot of people frequently ask "Where is Docker storing my data when I use a volume?" If you want to know, you can use the `docker volume inspect` command.

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
    
    
    $ docker volume inspect todo-db
    

You should see output like the following:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
    
    
    [
        {
            "CreatedAt": "2019-09-26T02:18:36Z",
            "Driver": "local",
            "Labels": {},
            "Mountpoint": "/var/lib/docker/volumes/todo-db/_data",
            "Name": "todo-db",
            "Options": {},
            "Scope": "local"
        }
    ]
    

The `Mountpoint` is the actual location of the data on the disk. Note that on most machines, you will need to have root access to access this directory from the host.

## [Summary](#summary)

In this section, you learned how to persist container data.

Related information:

  * [docker CLI reference](/reference/cli/docker/)
  * [Volumes](https://docs.docker.com/engine/storage/volumes/)

## [Next steps](#next-steps)

Next, you'll learn how you can develop your app more efficiently using bind mounts.

[Use bind mounts](https://docs.docker.com/get-started/workshop/06_bind_mounts/)

[Edit this page](https://github.com/docker/docs/edit/main/content/get-started/workshop/05_persisting_data.md)

[Request changes](https://github.com/docker/docs/issues/new?template=doc_issue.yml&location=https%3a%2f%2fdocs.docker.com%2fget-started%2fworkshop%2f05_persisting_data%2f&labels=status%2Ftriage)

Table of contents

  * [The container's filesystem](#the-containers-filesystem)
    * [See this in practice](#see-this-in-practice)
  * [Container volumes](#container-volumes)
  * [Persist the todo data](#persist-the-todo-data)
    * [Create a volume and start the container](#create-a-volume-and-start-the-container)
    * [Verify that the data persists](#verify-that-the-data-persists)
  * [Dive into the volume](#dive-into-the-volume)
  * [Summary](#summary)
  * [Next steps](#next-steps)