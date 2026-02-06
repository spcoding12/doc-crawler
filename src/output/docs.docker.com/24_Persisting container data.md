# Persisting container data

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

[Home](https://docs.docker.com/) / [Get started](https://docs.docker.com/get-started/) / [Docker concepts]() / [Running containers]() / Persisting container data

# Persisting container data

Copy as Markdown

Open Markdown Ask Docs AI Claude Open in Claude

Table of contents

  * [Explanation](#explanation)
    * [Container volumes](#container-volumes)
    * [Managing volumes](#managing-volumes)
  * [Try it out](#try-it-out)
    * [Use volumes](#use-volumes)
    * [View volume contents](#view-volume-contents)
    * [Remove volumes](#remove-volumes)
  * [Additional resources](#additional-resources)
  * [Next steps](#next-steps)

* * *

## [Explanation](#explanation)

When a container starts, it uses the files and configuration provided by the image. Each container is able to create, modify, and delete files and does so without affecting any other containers. When the container is deleted, these file changes are also deleted.

While this ephemeral nature of containers is great, it poses a challenge when you want to persist the data. For example, if you restart a database container, you might not want to start with an empty database. So, how do you persist files?

### [Container volumes](#container-volumes)

Volumes are a storage mechanism that provide the ability to persist data beyond the lifecycle of an individual container. Think of it like providing a shortcut or symlink from inside the container to outside the container.

As an example, imagine you create a volume named `log-data`.

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
    
    
    $ docker volume create log-data
    

When starting a container with the following command, the volume will be mounted (or attached) into the container at `/logs`:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
    
    
    $ docker run -d -p 80:80 -v log-data:/logs docker/welcome-to-docker
    

If the volume `log-data` doesn't exist, Docker will automatically create it for you.

When the container runs, all files it writes into the `/logs` folder will be saved in this volume, outside of the container. If you delete the container and start a new container using the same volume, the files will still be there.

> **Sharing files using volumes**
> 
> You can attach the same volume to multiple containers to share files between containers. This might be helpful in scenarios such as log aggregation, data pipelines, or other event-driven applications.

### [Managing volumes](#managing-volumes)

Volumes have their own lifecycle beyond that of containers and can grow quite large depending on the type of data and applications you’re using. The following commands will be helpful to manage volumes:

  * `docker volume ls` \- list all volumes
  * `docker volume rm <volume-name-or-id>` \- remove a volume (only works when the volume is not attached to any containers)
  * `docker volume prune` \- remove all unused (unattached) volumes

## [Try it out](#try-it-out)

In this guide, you'll practice creating and using volumes to persist data created by a Postgres container. When the database runs, it stores files into the `/var/lib/postgresql` directory. By attaching the volume here, you will be able to restart the container multiple times while keeping the data.

### [Use volumes](#use-volumes)

  1. [Download and install](/get-started/get-docker/) Docker Desktop.

  2. Start a container using the [Postgres image](https://hub.docker.com/_/postgres) with the following command:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         $ docker run --name=db -e POSTGRES_PASSWORD=secret -d -v postgres_data:/var/lib/postgresql postgres:18
         

This will start the database in the background, configure it with a password, and attach a volume to the directory PostgreSQL will persist the database files.

  3. Connect to the database by using the following command:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         $ docker exec -ti db psql -U postgres
         

  4. In the PostgreSQL command line, run the following to create a database table and insert two records:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         CREATE TABLE tasks (
             id SERIAL PRIMARY KEY,
             description VARCHAR(100)
         );
         INSERT INTO tasks (description) VALUES ('Finish work'), ('Have fun');

  5. Verify the data is in the database by running the following in the PostgreSQL command line:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         SELECT * FROM tasks;

You should get output that looks like the following:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         id | description
         ----+-------------
           1 | Finish work
           2 | Have fun
         (2 rows)

  6. Exit out of the PostgreSQL shell by running the following command:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         \q
         

  7. Stop and remove the database container. Remember that, even though the container has been deleted, the data is persisted in the `postgres_data` volume.

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         $ docker stop db
         $ docker rm db
         

  8. Start a new container by running the following command, attaching the same volume with the persisted data:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         $ docker run --name=new-db -d -v postgres_data:/var/lib/postgresql postgres:18
         

You might have noticed that the `POSTGRES_PASSWORD` environment variable has been omitted. That’s because that variable is only used when bootstrapping a new database.

  9. Verify the database still has the records by running the following command:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         $ docker exec -ti new-db psql -U postgres -c "SELECT * FROM tasks"
         

### [View volume contents](#view-volume-contents)

The Docker Desktop Dashboard provides the ability to view the contents of any volume, as well as the ability to export, import, empty, delete and clone volumes.

  1. Open the Docker Desktop Dashboard and navigate to the **Volumes** view. In this view, you should see the **postgres_data** volume.

  2. Select the **postgres_data** volume’s name.

  3. The **Stored Data** tab shows the contents of the volume and provides the ability to navigate the files. The **Container in-use** tab displays the name of the container using the volume, the image name, the port number used by the container, and the target. A target is a path inside a container that gives access to the files in the volume. The **Exports** tab lets you export the volume. Double-clicking on a file will let you see the contents and make changes.

  4. Right-click on any file to save it or delete it.

### [Remove volumes](#remove-volumes)

Before removing a volume, it must not be attached to any containers. If you haven’t removed the previous container, do so with the following command (the `-f` will stop the container first and then remove it):

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
    
    
    $ docker rm -f new-db
    

There are a few methods to remove volumes, including the following:

  * Select the **Delete Volume** option on a volume in the Docker Desktop Dashboard.

  * Use the `docker volume rm` command:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
        
        $ docker volume rm postgres_data
        

  * Use the `docker volume prune` command to remove all unused volumes:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
        
        $ docker volume prune
        

## [Additional resources](#additional-resources)

The following resources will help you learn more about volumes:

  * [Manage data in Docker](/engine/storage)
  * [Volumes](/engine/storage/volumes)
  * [Volume mounts](/engine/containers/run/#volume-mounts)

## [Next steps](#next-steps)

Now that you have learned about persisting container data, it’s time to learn about sharing local files with containers.

[Sharing local files with containers](https://docs.docker.com/get-started/docker-concepts/running-containers/sharing-local-files/)

[Edit this page](https://github.com/docker/docs/edit/main/content/get-started/docker-concepts/running-containers/persisting-container-data.md)

[Request changes](https://github.com/docker/docs/issues/new?template=doc_issue.yml&location=https%3a%2f%2fdocs.docker.com%2fget-started%2fdocker-concepts%2frunning-containers%2fpersisting-container-data%2f&labels=status%2Ftriage)

Table of contents

  * [Explanation](#explanation)
    * [Container volumes](#container-volumes)
    * [Managing volumes](#managing-volumes)
  * [Try it out](#try-it-out)
    * [Use volumes](#use-volumes)
    * [View volume contents](#view-volume-contents)
    * [Remove volumes](#remove-volumes)
  * [Additional resources](#additional-resources)
  * [Next steps](#next-steps)