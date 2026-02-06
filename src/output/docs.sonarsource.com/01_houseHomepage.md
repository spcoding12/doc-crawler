# houseHomepage

sparkleAskchevron-down

# houseHomepage

SonarQube provides automated code quality and security reviews, delivering actionable intelligence that helps developers build better and faster.

### 

[hashtag](#what-is-sonarqube-server)

What is SonarQube Server?

SonarQube Server is an industry-standard on-premises automated code review and static analysis tool designed to detect coding issues in [30+ languages](/sonarqube-server/analyzing-source-code/languages/overview), frameworks, and IaC platforms. By integrating directly with your CI pipeline (see the [Overview](/sonarqube-server/analyzing-source-code/ci-integration/overview) page) or on one of our supported DevOps platforms, your code is checked against an extensive set of rules that cover many attributes of code, such as maintainability, reliability, and security issues on each merge/pull request.

As a core element of the SonarQube solution, SonarQube Server completes the analysis loop to help you deliver code that meets high-quality standards.

Please see the [Try out SonarQube Server](/sonarqube-server/try-out-sonarqube) page to learn how to get started. For a Software-as-a-Service (SaaS) cloud-based tool, see [SonarQube Cloud](https://docs.sonarsource.com/sonarqube-cloud/).

### 

[hashtag](#high-quality-code)

Achieving high quality code

SonarQube sets high standards for all code that results in secure, reliable, and maintainable software that is essential to maintaining a healthy codebase. This applies to all code: source code, test code, infrastructure as code, glue code, scripts, and more.

All new code, whether added or recently modified, should adhere to quality standards. SonarQube for IDE achieves this by providing automated code reviews that alert you to potential issues within your new code. This helps you maintain high standards and focus on code quality, ultimately leading to a healthier codebase over time.

SonarQube Server comes with a built-in quality profiles designed for each supported language, called the **Sonar way** profile, see [Understanding quality profiles](/sonarqube-server/quality-standards-administration/managing-quality-profiles/understanding-quality-profiles). The **Sonar way** activates a set of rules that should be applicable to most projects and is a starting point to help you implement good practices in your organization.

### 

[hashtag](#the-sonarqube-solution)

The SonarQube solution

SonarQube is designed to help you achieve a state of high quality code. By linking SonarQube for IDE ([VS Code](https://docs.sonarsource.com/sonarqube-for-vs-code/), [Intellij](https://docs.sonarsource.com/sonarqube-for-intellij/), [Visual Studio](https://docs.sonarsource.com/sonarqube-for-visual-studio/) , [Eclipse](https://docs.sonarsource.com/sonarqube-for-eclipse/)) with [SonarQube Cloud](https://docs.sonarsource.com/sonarqube-cloud/) or SonarQube Server, the automated code analysis and reviews are performed at every stage of the development process. We call this the SonarQube solution. This means your project settings, new code definitions, and quality profiles are applied locally to an analysis in the IDE. Your project settings, new code definitions, and the quality profiles managed in SonarQube (Server, Cloud) are applied locally to an analysis in the IDE.

  * SonarQube for IDE ([VS Code](https://docs.sonarsource.com/sonarqube-for-vs-code/), [Intellij](https://docs.sonarsource.com/sonarqube-for-intellij/), [Visual Studio](https://docs.sonarsource.com/sonarqube-for-visual-studio/) , [Eclipse](https://docs.sonarsource.com/sonarqube-for-eclipse/)) brings automated code reviews directly into your development environment, helping you catch issues as you write code. By providing immediate feedback, it enables engineers to identify and fix problems before they even commit, ensuring cleaner, higher-quality code from the start.

  * SonarQube delivers powerful static code analysis by thoroughly reviewing each pull request before itâ€™s merged. This proactive approach adds an essential layer of protection, ensuring code quality and preventing issues from entering your codebase. See the [introduction to PR analysis](/sonarqube-server/analyzing-source-code/pull-request-analysis) on SonarQube Server and the [Pull request analysis](/sonarqube-cloud/improving/pull-request-analysis) page on SonarQube Cloud.

  * Finally, SonarQube Server and SonarQube Cloud seamlessly integrate into your CI/CD pipeline, analyzing code on every build. By leveraging [quality profiles](/sonarqube-server/quality-standards-administration/managing-quality-profiles/understanding-quality-profiles), and [quality gates](/sonarqube-server/quality-standards-administration/managing-quality-gates/introduction-to-quality-gates), they automatically block code with issues from being released to production, ensuring only maintainable, reliable, and secure code makes it through.

The SonarQube solution helps you incorporate a proper methodology by helping engineers pay attention to new code. Focusing on writing high quality new code during development ensures that all code released for production will be incrementally improved over time.

### 

[hashtag](#connected-mode)

Connected Mode

Connected Mode joins SonarQube Server with SonarQube for IDE to deliver the full SonarQube solution. While in Connected Mode, SonarQube Server sends notifications to SonarQube for IDE when a quality gate changes or a new issue is assigned to the user. Smart notifications can be enabled or disabled from the SonarQube for IDE interface while creating or editing the connection settings. Additionally, SonarQube for IDE helps engineers focus on writing high quality code by using the new code definition from the server. Be sure to check out all of the benefits of [Connected mode](/sonarqube-server/user-guide/connected-mode).

### 

[hashtag](#getting-started)

Getting started

Now that youâ€™ve heard about how [SonarQube Serverarrow-up-right](https://www.sonarsource.com/products/sonarqube/) can help you write high quality code, you are ready to try out SonarQube Server for yourself. You can run a local non-production instance of SonarQube Server and the initial project analysis. Installing a local instance gets you up and running quickly, so you can experience SonarQube Server firsthand. Then, when youâ€™re ready to set up SonarQube Server in production, youâ€™ll need to follow this [Introduction](/sonarqube-server/server-installation/introduction) to installation before configuring your first code analysis.

The [Project analysis setup](/sonarqube-server/analyzing-source-code/overview) section explains how to connect your scanner to your CI pipeline and provides instructions for analyzing your projectâ€™s branches and pull requests.

Here is a page with everything you need to [Try out SonarQube Server](/sonarqube-server/try-out-sonarqube).

### 

[hashtag](#learn-more)

Learn more

Check out the entire suite of Sonar products: [SonarQube Serverarrow-up-right](https://www.sonarsource.com/products/sonarqube/), [SonarQube Cloudarrow-up-right](https://www.sonarsource.com/products/sonarcloud/), and [SonarQube for IDEarrow-up-right](https://www.sonarsource.com/products/sonarlint/) available for static code analysis.

Then, have a look at how to fix issues detected by SonarQube for IDE in

  * VS Code: [Fixing issues](/sonarqube-for-vs-code/using/fixing-issues)

  * IntelliJ: [Fixing issues](/sonarqube-for-intellij/using/fixing-issues)

  * Visual studio: [Fixing issues](/sonarqube-for-visual-studio/using/fixing-issues)

  * Eclipse: [Fixing issues](/sonarqube-for-eclipse/using/fixing-issues)

#### 

[hashtag](#more-getting-started-resources)

More getting started resources

  * [Introduction](/sonarqube-server/server-installation/introduction) to server installation and setup

  * [Importing your DevOps platform repository](/sonarqube-server/project-administration/creating-your-project/importing-repo)

  * [Introduction](/sonarqube-server/quality-standards-administration/managing-quality-profiles/introduction)

  * [Managing portfolios](/sonarqube-server/project-administration/managing-portfolios)

### 

[hashtag](#staying-connected)

Staying connected

If you need help, visit our [online communityarrow-up-right](https://community.sonarsource.com/c/sq/10) to search for answers and reach out with questions!

[NextTry out SonarQube Serverchevron-right](/sonarqube-server/try-out-sonarqube)

Last updated 20 hours ago

Was this helpful?