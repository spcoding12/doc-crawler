# Project analysis setup

sparkleAskchevron-down

  1. [Analyzing source code](/sonarqube-server/analyzing-source-code)

# Project analysis setup

This page introduces briefly the prerequisites and the setup steps necessary for a project analysis with SonarQube Server.

This page introduces briefly the prerequisites and the setup steps necessary for a project analysis.

For an overview of the analysis process, see the [SonarQube Server analysis overview](/sonarqube-server/analyzing-source-code/analysis-overview) page.

### 

[hashtag](#prerequisites)

Prerequisites and recommendations

chevron-rightSonarQube Server is integrated with your DevOps platform / CI tool[hashtag](#sonarqube-server-is-integrated-with-your-devops-platform-ci-tool)

It is highly recommended that you integrate SonarQube Server with your DevOps platform or CI tool. See [DevOps platform integration](/sonarqube-server/devops-platform-integration).

chevron-rightThe SCM integration is properly set up[hashtag](#the-scm-integration-is-properly-set-up)

The SCM data used during the analysis will be automatically imported from Git and SVN. Other providers require additional plugins. We highly recommend using the full depth during the cloning of the code from the project repository.

circle-exclamation

A full Git clone is required. If a shallow clone is found, the blame information retrieval will be skipped and the analysis may fail.

For more information, see [SCM integration](/sonarqube-server/analyzing-source-code/scm-integration).

chevron-rightThe SonarScanner is installed on the CI/CD host[hashtag](#the-sonarscanner-is-installed-on-the-ci-cd-host)

The SonarScanner must be installed on the CI/CD host. You must install the scanner that is most appropriate for your needs depending on your build system: Gradle, Maven, .NET, NPM, or Python. For other project types, use the SonarScanner CLI which requires more manual configuration.

For installation requirements, see [General requirements](/sonarqube-server/analyzing-source-code/scanners/scanner-environment/general-requirements).

For installation instructions, see the corresponding SonarScanner section: 

  * [SonarScanner for Maven](/sonarqube-server/analyzing-source-code/scanners/sonarscanner-for-maven)

  * [SonarScanner for Gradle](/sonarqube-server/analyzing-source-code/scanners/sonarscanner-for-gradle)

  * SonarScanner for .Net: [Installing the scanner](/sonarqube-server/analyzing-source-code/scanners/dotnet/installing)

  * SonarScanner for NPM: [Installing the scanner](/sonarqube-server/analyzing-source-code/scanners/npm/installing)

  * [SonarScanner for Python](/sonarqube-server/analyzing-source-code/scanners/sonarscanner-for-python)

  * [SonarScanner CLI](/sonarqube-server/analyzing-source-code/scanners/sonarscanner)

### 

[hashtag](#creating-sq-project)

Creating your SonarQube Server project

Your project repository is represented in SonarQube Server by a project.

You can create a SonarQube Server project in the SonarQube Server UI before starting the first project analysis. Or you can start your first project analysis to automatically create the SonarQube Server project on the server (SonarQube Server creates automatically a new project if the received project key does not exist in its database).

To create a project, see [Importing your DevOps platform repository](/sonarqube-server/project-administration/creating-your-project/importing-repo).

### 

[hashtag](#integrating-into-ci-or-build)

Integrating the SonarQube Server analysis into your CI or build pipeline

To integrate the SonarQube Server analysis into your CI pipeline, see the corresponding section:

  * Jenkins: [Adding analysis to a Jenkins job](/sonarqube-server/analyzing-source-code/ci-integration/jenkins-integration/add-analysis-to-job)

  * GitHub Actions: [Adding analysis to GitHub Actions workflow](/sonarqube-server/devops-platform-integration/github-integration/adding-analysis-to-github-actions-workflow)

  * GitLab CI/CD: [Adding analysis to GitLab CI/CD pipeline](/sonarqube-server/devops-platform-integration/gitlab-integration/adding-analysis-to-gitlab-ci-cd)

  * Azure Pipelines: [Adding analysis to Azure pipeline](/sonarqube-server/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline)

  * Bitbucket Pipelines: [Adding analysis to Bitbucket pipeline](/sonarqube-server/devops-platform-integration/bitbucket-integration/bitbucket-cloud-integration/bitbucket-pipelines)

To integrate the SonarQube Server analysis into your build pipeline, see the scanner invoking instructions in the corresponding section:

  * [SonarScanner for Maven](/sonarqube-server/analyzing-source-code/scanners/sonarscanner-for-maven)

  * [SonarScanner for Gradle](/sonarqube-server/analyzing-source-code/scanners/sonarscanner-for-gradle)

  * SonarScanner for .NET: [Using the scanner](/sonarqube-server/analyzing-source-code/scanners/dotnet/using)

  * SonarScanner for NPM: [Using the scanner](/sonarqube-server/analyzing-source-code/scanners/npm/using)

  * [SonarScanner for Python](/sonarqube-server/analyzing-source-code/scanners/sonarscanner-for-python)

  * [SonarScanner CLI](/sonarqube-server/analyzing-source-code/scanners/sonarscanner)

For general information about SonarQube Server integration with a CI or build pipeline, see [SonarQube Server analysis overview](/sonarqube-server/analyzing-source-code/analysis-overview).

### 

[hashtag](#adjusting-analysis)

Adjusting the analysis of your project

The analysis performed by the SonarScanner is configured through analysis parameters. The following applies:

  * A few analysis parameters are mandatory.

  * Many analysis parameters, such as those defining the analysis scope, have a default value and can be adjusted.

  * Analysis parameters allow you to include the code and test coverage in your analysis, or to import issues generated by a third-party analyzer, etc.

SonarQube Server manages the analysis parameters through sonar properties (The sonar property key has the following syntax: `sonar.<property>`.).

You can configure the analysis parameters in different places. For more information, see [Configuration overview](/sonarqube-server/analyzing-source-code/analysis-parameters/configuration-overview).

You can:

  * Include the code and test coverage in your analysis: see [Overview](/sonarqube-server/analyzing-source-code/test-coverage/overview).

  * Adjust the analysis scope: see [Setting analysis scope](/sonarqube-server/project-administration/adjusting-analysis/setting-analysis-scope).

  * Import issues generated by third-party analyzers: see the [External analyzer reports](/sonarqube-server/analyzing-source-code/importing-external-issues/external-analyzer-reports) section.

[PreviousSonarQube Server analysis overviewchevron-left](/sonarqube-server/analyzing-source-code/analysis-overview)[NextScannerschevron-right](/sonarqube-server/analyzing-source-code/scanners)

Was this helpful?