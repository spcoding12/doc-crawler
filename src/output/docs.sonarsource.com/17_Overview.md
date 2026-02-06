# Overview

sparkleAskchevron-down

  1. [Analyzing source code](/sonarqube-server/analyzing-source-code)chevron-right
  2. [CI integration](/sonarqube-server/analyzing-source-code/ci-integration)

# Overview

SonarQube Server supports integration on multiple platforms allowing you to maintain code quality and security in your projects.

_Pull request analysis is available as part of_ [_Developer Edition_ arrow-up-right](https://www.sonarsource.com/plans-and-pricing/developer/) _and_ [_above_ arrow-up-right](https://www.sonarsource.com/plans-and-pricing/) _._

### 

[ hashtag](#quality-gate-fails)

Failing a pipeline job when the quality gate fails

You can ensure your code meets your quality standards by failing your pipeline job when your [quality gate](/sonarqube-server/quality-standards-administration/managing-quality-gates/introduction-to-quality-gates) fails. The operation depends on the CI tool used.

JENKINS

GITHUB

BITBUCKET PIPELINES

OTHER CI TOOLS

With Jenkins, you can suspend pipeline execution until the analysisâ€™ quality gate status is known. See the [Key features](/sonarqube-server/analyzing-source-code/ci-integration/jenkins-integration/key-features) integration pages.

With GitHub Actions, you can fail the pipeline job when the quality gate fails using the [SonarQube Quality Gate Check Actionarrow-up-right](https://github.com/marketplace/actions/sonarqube-quality-gate-check).

See [Failing the workflow when the quality gate fails](/sonarqube-server/devops-platform-integration/github-integration/adding-analysis-to-github-actions-workflow#fail-workflow-on-quality-gate-failure).

With Bitbucket Pipelines, you can fail the pipeline job when the quality gate fails using the [SonarQube Quality Gate Check Pipearrow-up-right](https://bitbucket.org/sonarsource/sonarqube-quality-gate).

See [Failing the pipeline job when the quality gate fails](/sonarqube-server/devops-platform-integration/bitbucket-integration/bitbucket-cloud-integration/bitbucket-pipelines#failing-the-pipeline-job-when-the-quality-gate-fails).

You can configure the SonarScanner to wait for the quality gate result. This setting will force the pipeline to fail if the quality gate fails.

To do so:

  1. Set the `sonar.qualitygate.wait` analysis parameter to `true`.

  2. You can set the `sonar.qualitygate.timeout` analysis parameters to the number of seconds that the scanner should wait for a report to be processed. The default is 300 seconds.

For general information on setting up analysis parameters, see [Configuration overview](/sonarqube-server/analyzing-source-code/analysis-parameters/configuration-overview).

### 

[hashtag](#gitlab)

GitLab CI/CD

For GitLab CI/CD configuration, see the [Adding analysis to GitLab CI/CD pipeline](/sonarqube-server/devops-platform-integration/gitlab-integration/adding-analysis-to-gitlab-ci-cd) page.

### 

[hashtag](#github-actions)

GitHub Actions

For GitHub Actions configuration, see the [Adding analysis to GitHub Actions workflow](/sonarqube-server/devops-platform-integration/github-integration/adding-analysis-to-github-actions-workflow) page.

### 

[hashtag](#azure-pipelines)

Azure Pipelines

For Azure Pipelines configuration, see the [Adding analysis to Azure pipeline](/sonarqube-server/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline) section.

### 

[hashtag](#bitbucket-pipeline)

Bitbucket Pipelines

For Bitbucket Pipelines configuration, see the [Adding analysis to Bitbucket pipeline](/sonarqube-server/devops-platform-integration/bitbucket-integration/bitbucket-cloud-integration/bitbucket-pipelines) page.

### 

[hashtag](#jenkins-1)

Jenkins

For Jenkins configuration, see [Adding analysis to a Jenkins job](/sonarqube-server/analyzing-source-code/ci-integration/jenkins-integration/add-analysis-to-job).

[PreviousCI integrationchevron-left](/sonarqube-server/analyzing-source-code/ci-integration)[NextJenkins integrationchevron-right](/sonarqube-server/analyzing-source-code/ci-integration/jenkins-integration)

Was this helpful?