# Importing your DevOps platform repository

sparkleAskchevron-down

  1. [Project administration](/sonarqube-server/project-administration)chevron-right
  2. [Creating your project](/sonarqube-server/project-administration/creating-your-project)

# Importing your DevOps platform repository

Creating and importing projects from a DevOps platform repository.

Once the global-level integration with your DevOps platform is complete, you can create your SonarQube Server project by importing your DevOps platform repository. The so-created SonarQube Server project is "bound" to its Azure DevOps repository. With a bound project, you benefit from integration features, such as pull request decoration, code scanning alerts, permission synchronization, etc.

To import your repository, you need the Create Projects permission in SonarQube Server and the corresponding access rights on the repository.

To import a DevOps platform repository into SonarQube Server:

  1. In the top navigation bar of SonarQube Server, select the **Projects** tab.

  2. In the top right corner, select the **Create Project > From <DevOps Platform>** button.

  3. If your instance has multiple DevOps platform Integrations, select the configuration from which you want to import your project.

  4. Select the repository to be imported.

For more information, see the section corresponding to your DevOps platform:

  * [Importing GitHub repositories](/sonarqube-server/devops-platform-integration/github-integration/importing-github-repositories)

  * [Importing Bitbucket Cloud repositories](/sonarqube-server/devops-platform-integration/bitbucket-integration/bitbucket-cloud-integration/import-repos)

  * [Importing your Bitbucket Data Center repositories](/sonarqube-server/devops-platform-integration/bitbucket-integration/bitbucket-server-integration/import-repos)

  * [Importing your GitLab repositories](/sonarqube-server/devops-platform-integration/gitlab-integration/importing-repos)

  * [Creating and configuring your Azure DevOps project](/sonarqube-server/devops-platform-integration/azure-devops-integration/creating-your-project)

circle-info

Starting in [Enterprise Editionarrow-up-right](https://www.sonarsource.com/plans-and-pricing/enterprise/), you can import a monorepo. See [Managing monorepo projects](/sonarqube-server/project-administration/monorepos).

[PreviousCreating your projectchevron-left](/sonarqube-server/project-administration/creating-your-project)[NextAutomating project creation and importchevron-right](/sonarqube-server/project-administration/creating-your-project/automating-project-creation-and-import)

Was this helpful?