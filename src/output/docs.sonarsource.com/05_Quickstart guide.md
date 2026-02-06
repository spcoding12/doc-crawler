# Quickstart guide

sparkleAskchevron-down

# Quickstart guide

A checklist for administrators setting up their initial installation of SonarQube Server.

By completing this guide you will:

  1. [Download, install and configure SonarQube Server.](/sonarqube-server/quickstart-guide#install-the-server)

  2. [Integrate SonarQube with your DevOps platform](/sonarqube-server/quickstart-guide#devops-platform-integration)

  3. [Create or import a project](/sonarqube-server/quickstart-guide#onboard-your-projects)

  4. [Configure CI analysis](/sonarqube-server/quickstart-guide#configure-your-ci-analysis)

  5. [Integrate with SonarQube for IDE](/sonarqube-server/quickstart-guide#connect-with-sonarqube-for-ide)

  6. [Review quality gates](/sonarqube-server/quickstart-guide#review-your-quality-gates)

     1. Review pull/merge request analysis for failed quality gates.

     2. Configure pull request decoration on your DevOps platform

### 

[hashtag](#before-you-begin)

Before you begin

Review the [Server host requirements](/sonarqube-server/server-installation/server-host-requirements) and [Pre-installation steps](/sonarqube-server/server-installation/pre-installation). This will help you establish a deployment plan (Zip, Docker, or Helm on Kubernetes) and then before you start [Installing database](/sonarqube-server/server-installation/installing-the-database).

Now you are ready to [download SonarQube Serverarrow-up-right](https://www.sonarsource.com/products/sonarqube/downloads/?_gl=1*1cb3ncb*_gcl_aw*R0NMLjE3NTY4MTY4NTAuQ2p3S0NBandxOXJGQmhBSUVpd0FHVkFaUDhpSnpMWFFYOFM0U1NYN1h6YUlEVkxqYWpaVzBENFoyaFZfNFlRMnU5ejVlZ2xkdE43dnd4b0M5ZFFRQXZEX0J3RQ..*_gcl_au*MTUyODQxMjM2OC4xNzU3OTQwNjA3LjIwNDk1NTUzMjIuMTc1OTkxNTc4Ny4xNzU5OTE1Nzg2*_ga*MzU0MTY0OTcwLjE3MjY2NzExODc.*_ga_9JZ0GZ5TC6*czE3NjA2MTUyNDkkbzEyMSRnMSR0MTc2MDYxNzkwOCRqNjAkbDAkaDA.).

### 

[hashtag](#install-the-server)

Install the server

Choose your installation target:

  * [From ZIP file](/sonarqube-server/server-installation/from-zip-file)

  * [From Docker image](/sonarqube-server/server-installation/from-docker-image)

  * [Installing on Kubernetes or OpenShift](/sonarqube-server/server-installation/on-kubernetes-or-openshift)

### 

[hashtag](#devops-platform-integration)

DevOps platform integration

Next you will integrate SonarQube with your DevOps platforms:

  * [GitHub integration](/sonarqube-server/devops-platform-integration/github-integration)

  * [Bitbucket integration](/sonarqube-server/devops-platform-integration/bitbucket-integration)

  * [GitLab integration](/sonarqube-server/devops-platform-integration/gitlab-integration)

  * [Azure DevOps integration](/sonarqube-server/devops-platform-integration/azure-devops-integration)

### 

[hashtag](#onboard-your-projects)

Onboard your projects

You can [import projects from your DevOps platform](/sonarqube-server/project-administration/creating-your-project/importing-repo#importing-repository) or [manually add local projects](/sonarqube-server/project-administration/creating-your-project/importing-repo#creating-project-manually), see [Importing your DevOps platform repository](/sonarqube-server/project-administration/creating-your-project/importing-repo) for more details including how to automate both methods using the [Web API](/sonarqube-server/extension-guide/web-api).

### 

[hashtag](#configure-your-ci-analysis)

Configure your CI analysis

Read [Project analysis setup](/sonarqube-server/analyzing-source-code/overview) for guidance on setting up analysis for your imported projects

  * [SonarQube Server is integrated with your DevOps platform / CI tool](/sonarqube-server/analyzing-source-code/overview#sonarqube-server-is-integrated-with-your-devops-platform-ci-tool)

  * [The SonarScanner is installed on the CI/CD host](/sonarqube-server/analyzing-source-code/overview#the-sonarscanner-is-installed-on-the-ci-cd-host)

### 

[hashtag](#connect-with-sonarqube-for-ide)

Connect with SonarQube for IDE

Have your developers install SonarQube for IDE to leverage the power of[Connected mode](/sonarqube-server/user-guide/connected-mode) in their IDE.

### 

[hashtag](#review-your-quality-gates)

Review your quality gates

The purpose of [quality gates](/sonarqube-server/quality-standards-administration/managing-quality-gates) is to tell you whether your code is good enough to be pushed to the next step:

  * For the main branch and other long-lived branches, the quality gate answers the question: "Can I release my code today?"

  * For pull requests (and short-lived branches), the quality gate answers the question: "Can I merge this pull request?"

By [Setting up the pull request analysis](/sonarqube-server/analyzing-source-code/pull-request-analysis/setting-up-the-pull-request-analysis) analysis occurs when a pull request is opened and every time a change is pushed to the pull request branch. You can also configure [pull request decoration](/sonarqube-server/analyzing-source-code/pull-request-analysis/introduction#decoration) to allow your developers to view the analysis from SonarQube server directly on the PRs they submit.

By keeping an eye on the quality gates, the decision makers can quickly judge the status of code and decide what to do next.

### 

[hashtag](#develop-with-sonar)

Develop with Sonar

Now that you have installed [SonarQube Server](/sonarqube-server#high-quality-code) with your DevOps platforms or CI pipeline, managers and tech leads can check out the [Security reports](/sonarqube-server/user-guide/viewing-reports/security-reports) and [Portfolios](/sonarqube-server/user-guide/viewing-reports/portfolios) features to begin monitoring the security and releasability of projects.

[PreviousBest practices for managing dependency riskschevron-left](/sonarqube-server/advanced-security/best-practices-for-managing-dependency-risks)[NextServer installation and setupchevron-right](/sonarqube-server/server-installation)

Was this helpful?