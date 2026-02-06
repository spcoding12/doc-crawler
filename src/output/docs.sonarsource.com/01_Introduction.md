# Introduction

sparkleAskchevron-down

  1. [Server installation and setup](/sonarqube-server/server-installation)

# Introduction

This section explains how to install and setup your SonarQube Server.

### 

[hashtag](#developer-and-enterprise-editions)

Developer and Enterprise editions

  * [Server components](/sonarqube-server/server-installation/server-components-overview)

  * [Server host requirements](/sonarqube-server/server-installation/server-host-requirements)

  * [Networking requirements](/sonarqube-server/server-installation/networking-requirements)

  * **Pre-installation steps** :

    * [On Linux systems](/sonarqube-server/server-installation/pre-installation/linux)

    * [On Unix-based systems](/sonarqube-server/server-installation/pre-installation/unix)

    * [On macOS systems](/sonarqube-server/server-installation/pre-installation/macos)

  * **Installing** :

    * [From ZIP file](/sonarqube-server/server-installation/from-zip-file)

    * [From Docker image](/sonarqube-server/server-installation/from-docker-image)

    * [Installing on Kubernetes or OpenShift](/sonarqube-server/server-installation/on-kubernetes-or-openshift)

  * **Post-installation** By default, the `sonar-users` group has the **Execute Analysis** global permission, which means that its users can see the branch status of any project, even if they donâ€™t have explicit permissions for it. We recommend that after your trial, you review all global permissions and ensure they comply with your company policy. See [Setting the global permissions](/sonarqube-server/instance-administration/user-management/user-permissions#global-permissions) for more information.

  * **Network security:**

    * [Securing behind a proxy](/sonarqube-server/server-installation/network-security/securing-behind-proxy)

    * [Network rules](/sonarqube-server/server-installation/network-security/network-rules)

  * **Reference architectures:**

    * [Up to 10 M LOC](/sonarqube-server/server-installation/reference-architectures/up-to-10m-loc)

    * [Up to 50 M LOC](/sonarqube-server/server-installation/reference-architectures/up-to-50m-loc)

### 

[hashtag](#data-center-edition)

Data Center Edition

  * [DCE topology](/sonarqube-server/server-installation/data-center-edition/dce-topology)

  * [Installation requirements](/sonarqube-server/server-installation/data-center-edition/installation-requirements)

  * [Pre-installation steps](/sonarqube-server/server-installation/data-center-edition/pre-installation)

  * **Installing:**

    * [Installing from ZIP file](/sonarqube-server/server-installation/data-center-edition/from-zip-file)

    * [Installing on Kubernetes or Openshift](/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift)

  * **Network security:**

    * [Securing behind a proxy](/sonarqube-server/server-installation/data-center-edition/network-security/securing-behind-proxy)

    * [Elasticsearch security features](/sonarqube-server/server-installation/data-center-edition/network-security/elasticsearch-security-features)

    * [Network rules](/sonarqube-server/server-installation/data-center-edition/network-security/network-rules)

### 

[hashtag](#database)

Database

  * [Installing database](/sonarqube-server/server-installation/installing-the-database)

### 

[hashtag](#next-steps)

Next steps

After your server is up and running, youâ€™ll need to install one or more Sonar scanners on the machines where the analysis will be performed. See [Project analysis setup](/sonarqube-server/analyzing-source-code/overview).

[PreviousServer installation and setupchevron-left](/sonarqube-server/server-installation)[NextServer componentschevron-right](/sonarqube-server/server-installation/server-components-overview)

Last updated 17 days ago

Was this helpful?