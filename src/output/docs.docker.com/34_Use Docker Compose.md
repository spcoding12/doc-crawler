# Use Docker Compose

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

[Home](https://docs.docker.com/) / [Get started](https://docs.docker.com/get-started/) / [Docker workshop](https://docs.docker.com/get-started/workshop/) / Part 7: Use Docker Compose

# Use Docker Compose

Copy as Markdown

Open Markdown Ask Docs AI Claude Open in Claude

Table of contents

  * [Create the Compose file](#create-the-compose-file)
  * [Define the app service](#define-the-app-service)
    * [Define the MySQL service](#define-the-mysql-service)
  * [Run the application stack](#run-the-application-stack)
  * [See the app stack in Docker Desktop Dashboard](#see-the-app-stack-in-docker-desktop-dashboard)
  * [Tear it all down](#tear-it-all-down)
  * [Summary](#summary)
  * [Next steps](#next-steps)

* * *

[Docker Compose](https://docs.docker.com/compose/) is a tool that helps you define and share multi-container applications. With Compose, you can create a YAML file to define the services and with a single command, you can spin everything up or tear it all down.

The big advantage of using Compose is you can define your application stack in a file, keep it at the root of your project repository (it's now version controlled), and easily enable someone else to contribute to your project. Someone would only need to clone your repository and start the app using Compose. In fact, you might see quite a few projects on GitHub/GitLab doing exactly this now.

## [Create the Compose file](#create-the-compose-file)

In the `getting-started-app` directory, create a file named `compose.yaml`.

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
    
    
    ├── getting-started-app/
    │ ├── Dockerfile
    │ ├── compose.yaml
    │ ├── node_modules/
    │ ├── package.json
    │ ├── package-lock.json
    │ ├── spec/
    │ └── src/

## [Define the app service](#define-the-app-service)

In [part 6](https://docs.docker.com/get-started/workshop/07_multi_container/), you used the following command to start the application service.

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
    
    
    $ docker run -dp 127.0.0.1:3000:3000 \
      -w /app -v ".:/app" \
      --network todo-app \
      -e MYSQL_HOST=mysql \
      -e MYSQL_USER=root \
      -e MYSQL_PASSWORD=secret \
      -e MYSQL_DB=todos \
      node:24-alpine \
      sh -c "npm install && npm run dev"
    

You'll now define this service in the `compose.yaml` file.

  1. Open `compose.yaml` in a text or code editor, and start by defining the name and image of the first service (or container) you want to run as part of your application. The name will automatically become a network alias, which will be useful when defining your MySQL service.

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         services:
           app:
             image: node:24-alpine

  2. Typically, you will see `command` close to the `image` definition, although there is no requirement on ordering. Add the `command` to your `compose.yaml` file.

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         services:
           app:
             image: node:24-alpine
             command: sh -c "npm install && npm run dev"

  3. Now migrate the `-p 127.0.0.1:3000:3000` part of the command by defining the `ports` for the service.

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         services:
           app:
             image: node:24-alpine
             command: sh -c "npm install && npm run dev"
             ports:
               - 127.0.0.1:3000:3000

  4. Next, migrate both the working directory (`-w /app`) and the volume mapping (`-v ".:/app"`) by using the `working_dir` and `volumes` definitions.

One advantage of Docker Compose volume definitions is you can use relative paths from the current directory.

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         services:
           app:
             image: node:24-alpine
             command: sh -c "npm install && npm run dev"
             ports:
               - 127.0.0.1:3000:3000
             working_dir: /app
             volumes:
               - ./:/app

  5. Finally, you need to migrate the environment variable definitions using the `environment` key.

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         services:
           app:
             image: node:24-alpine
             command: sh -c "npm install && npm run dev"
             ports:
               - 127.0.0.1:3000:3000
             working_dir: /app
             volumes:
               - ./:/app
             environment:
               MYSQL_HOST: mysql
               MYSQL_USER: root
               MYSQL_PASSWORD: secret
               MYSQL_DB: todos

### [Define the MySQL service](#define-the-mysql-service)

Now, it's time to define the MySQL service. The command that you used for that container was the following:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
    
    
    $ docker run -d \
      --network todo-app --network-alias mysql \
      -v todo-mysql-data:/var/lib/mysql \
      -e MYSQL_ROOT_PASSWORD=secret \
      -e MYSQL_DATABASE=todos \
      mysql:8.0
    

  1. First define the new service and name it `mysql` so it automatically gets the network alias. Also specify the image to use as well.

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         services:
           app:
             # The app service definition
           mysql:
             image: mysql:8.0

  2. Next, define the volume mapping. When you ran the container with `docker run`, Docker created the named volume automatically. However, that doesn't happen when running with Compose. You need to define the volume in the top-level `volumes:` section and then specify the mountpoint in the service config. By simply providing only the volume name, the default options are used.

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         services:
           app:
             # The app service definition
           mysql:
             image: mysql:8.0
             volumes:
               - todo-mysql-data:/var/lib/mysql
         
         volumes:
           todo-mysql-data:

  3. Finally, you need to specify the environment variables.

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         services:
           app:
             # The app service definition
           mysql:
             image: mysql:8.0
             volumes:
               - todo-mysql-data:/var/lib/mysql
             environment:
               MYSQL_ROOT_PASSWORD: secret
               MYSQL_DATABASE: todos
         
         volumes:
           todo-mysql-data:

At this point, your complete `compose.yaml` should look like this:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
    
    
    services:
      app:
        image: node:24-alpine
        command: sh -c "npm install && npm run dev"
        ports:
          - 127.0.0.1:3000:3000
        working_dir: /app
        volumes:
          - ./:/app
        environment:
          MYSQL_HOST: mysql
          MYSQL_USER: root
          MYSQL_PASSWORD: secret
          MYSQL_DB: todos
    
      mysql:
        image: mysql:8.0
        volumes:
          - todo-mysql-data:/var/lib/mysql
        environment:
          MYSQL_ROOT_PASSWORD: secret
          MYSQL_DATABASE: todos
    
    volumes:
      todo-mysql-data:

## [Run the application stack](#run-the-application-stack)

Now that you have your `compose.yaml` file, you can start your application.

  1. Make sure no other copies of the containers are running first. Use `docker ps` to list the containers and `docker rm -f <ids>` to remove them.

  2. Start up the application stack using the `docker compose up` command. Add the `-d` flag to run everything in the background.

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         $ docker compose up -d
         

When you run the previous command, you should see output like the following:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         Creating network "app_default" with the default driver
         Creating volume "app_todo-mysql-data" with default driver
         Creating app_app_1   ... done
         Creating app_mysql_1 ... done

You'll notice that Docker Compose created the volume as well as a network. By default, Docker Compose automatically creates a network specifically for the application stack (which is why you didn't define one in the Compose file).

  3. Look at the logs using the `docker compose logs -f` command. You'll see the logs from each of the services interleaved into a single stream. This is incredibly useful when you want to watch for timing-related issues. The `-f` flag follows the log, so will give you live output as it's generated.

If you have run the command already, you'll see output that looks like this:

]\s+/gm, '')); copying = true; setTimeout(() => copying = false, 2000);">
         
         mysql_1  | 2019-10-03T03:07:16.083639Z 0 [Note] mysqld: ready for connections.
         mysql_1  | Version: '8.0.31'  socket: '/var/run/mysqld/mysqld.sock'  port: 3306  MySQL Community Server (GPL)
         app_1    | Connected to mysql db at host mysql
         app_1    | Listening on port 3000

The service name is displayed at the beginning of the line (often colored) to help distinguish messages. If you want to view the logs for a specific service, you can add the service name to the end of the logs command (for example, `docker compose logs -f app`).

  4. At this point, you should be able to open your app in your browser on <http://localhost:3000> and see it running.

## [See the app stack in Docker Desktop Dashboard](#see-the-app-stack-in-docker-desktop-dashboard)

If you look at the Docker Desktop Dashboard, you'll see that there is a group named **getting-started-app**. This is the project name from Docker Compose and used to group the containers together. By default, the project name is simply the name of the directory that the `compose.yaml` was located in.

If you expand the stack, you'll see the two containers you defined in the Compose file. The names are also a little more descriptive, as they follow the pattern of `<service-name>-<replica-number>`. So, it's very easy to quickly see what container is your app and which container is the mysql database.

## [Tear it all down](#tear-it-all-down)

When you're ready to tear it all down, simply run `docker compose down` or hit the trash can on the Docker Desktop Dashboard for the entire app. The containers will stop and the network will be removed.

> Warning
> 
> By default, named volumes in your compose file are not removed when you run `docker compose down`. If you want to remove the volumes, you need to add the `--volumes` flag.
> 
> The Docker Desktop Dashboard does not remove volumes when you delete the app stack.

## [Summary](#summary)

In this section, you learned about Docker Compose and how it helps you simplify the way you define and share multi-service applications.

Related information:

  * [Compose overview](https://docs.docker.com/compose/)
  * [Compose file reference](https://docs.docker.com/reference/compose-file/)
  * [Compose CLI reference](https://docs.docker.com/reference/cli/docker/compose/)

## [Next steps](#next-steps)

Next, you'll learn about a few best practices you can use to improve your Dockerfile.

[Image-building best practices](https://docs.docker.com/get-started/workshop/09_image_best/)

[Edit this page](https://github.com/docker/docs/edit/main/content/get-started/workshop/08_using_compose.md)

[Request changes](https://github.com/docker/docs/issues/new?template=doc_issue.yml&location=https%3a%2f%2fdocs.docker.com%2fget-started%2fworkshop%2f08_using_compose%2f&labels=status%2Ftriage)

Table of contents

  * [Create the Compose file](#create-the-compose-file)
  * [Define the app service](#define-the-app-service)
    * [Define the MySQL service](#define-the-mysql-service)
  * [Run the application stack](#run-the-application-stack)
  * [See the app stack in Docker Desktop Dashboard](#see-the-app-stack-in-docker-desktop-dashboard)
  * [Tear it all down](#tear-it-all-down)
  * [Summary](#summary)
  * [Next steps](#next-steps)