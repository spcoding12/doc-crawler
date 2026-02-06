# Connected mode

sparkleAskchevron-down

  1. [User guide](/sonarqube-server/user-guide)

# Connected mode

SonarQube for IDEÂ is a free IDE extension that integrates with SonarQube Server. Like a spell checker, it highlights issues as you type.

Connected mode binds your SonarQube (Server, Cloud) project to a project open in SonarQube for IDE so that you can catch issues immediately, even before you commit them.

[SonarQube for IDEarrow-up-right](https://www.sonarsource.com/products/sonarlint/) is a free IDE extension that integrates with SonarQube (Server, Cloud) using connected mode. Like a spell checker, SonarQube for IDE highlights issues as you type. When an issue is identified, SonarQube for IDE provides you with clear remediation guidance so you can fix it before the code is even committed. In many cases, it also provides a _quick fix_ that can automatically fix the issue for you.

### 

[hashtag](#supported-ides)

Supported IDEs

VS CODE

INTELLIJ

VISUAL STUDIO

ECLIPSE

SonarQube for VS Code will automatically identify and fix quality and security issues as you code with enhanced linting capabilities directly in your VS Code IDE.

  * [Feature overviewarrow-up-right](https://www.sonarsource.com/products/sonarlint/features/vs-code/)

  * [Installation](/sonarqube-for-vs-code/getting-started/installation) instructions

  * Supported [Rules and languages](/sonarqube-for-vs-code/using/rules)

  * [Connected mode setup](/sonarqube-for-vs-code/connect-your-ide/setup) and list of [Connected mode](/sonarqube-for-vs-code/connect-your-ide/connected-mode) benefits.

  * [Downloadarrow-up-right](https://marketplace.visualstudio.com/items?itemName=SonarSource.sonarlint-vscode)

SonarQube for IDE integrates with most JetBrains IDEs including IntelliJ IDEA, CLion, GoLand, WebStorm, PHPStorm, PyCharm, Rider, Android Studio & RubyMine.

  * [Feature overviewarrow-up-right](https://www.sonarsource.com/products/sonarlint/features/jetbrains/)

  * [Installation](/sonarqube-for-intellij/getting-started/installation) instructions

  * Supported [Rules and languages](/sonarqube-for-intellij/using/rules)

  * [Connected mode setup](/sonarqube-for-intellij/connect-your-ide/setup) and list of [Connected mode](/sonarqube-for-intellij/connect-your-ide/connected-mode) benefits.

  * [Downloadarrow-up-right](https://plugins.jetbrains.com/plugin/7973-sonarlint)

SonarQube for IDE provides Visual Studio developers with a comprehensive in-IDE solution for improving the quality and security of the code they deliver.

  * [Feature overviewarrow-up-right](https://www.sonarsource.com/products/sonarlint/features/visual-studio/)

  * [Installation](/sonarqube-for-visual-studio/getting-started/installation) instructions

  * Supported [Rules and languages](/sonarqube-for-visual-studio/using/rules)

  * [Connected mode setup](/sonarqube-for-visual-studio/connect-your-ide/setup) and list of [Connected mode](/sonarqube-for-visual-studio/connect-your-ide/connected-mode) benefits.

  * Downloads for:

    * [VS-2022arrow-up-right](https://marketplace.visualstudio.com/items?itemName=SonarSource.SonarLintforVisualStudio2022)

    * [VS-2019arrow-up-right](https://marketplace.visualstudio.com/items?itemName=SonarSource.SonarLintforVisualStudio2019)

    * [VS-2017arrow-up-right](https://marketplace.visualstudio.com/items?itemName=SonarSource.SonarLintforVisualStudio2017)

SonarQube for Eclipse will automatically identify and fix quality and security issues as you code with enhanced linting capabilities right in your Eclipse IDE.

  * [Feature overviewarrow-up-right](https://www.sonarsource.com/products/sonarlint/features/eclipse/)

  * [Installation](/sonarqube-for-eclipse/getting-started/installation) instructions

  * Supported [Rules and languages](/sonarqube-for-eclipse/using/rules)

  * [Connected mode setup](/sonarqube-for-eclipse/connect-your-ide/setup) and list of [Connected mode](/sonarqube-for-eclipse/connect-your-ide/connected-mode) benefits.

  * [Downloadarrow-up-right](https://marketplace.eclipse.org/content/sonarlint)

The supported languages vary by IDE. Check the Rules page for your IDE to learn which languages are supported out-of-the-box and which require the use of connected mode.

Though SonarQube for IDE can run local analyses in standalone mode, we highly recommend that you set up connected mode with SonarQube Server. Running SonarQube Server and SonarQube for IDE in connected mode provides additional [valuable featuresarrow-up-right](https://www.sonarsource.com/products/sonarlint/features/connected-mode/).

### 

[hashtag](#connected-mode-benefits)

Connected mode benefits

  * Combining SonarQube for IDE-supported rules with those supported by SonarQube Server allows you to analyze more languages and detect more issues. See [Rules and languages](/sonarqube-for-intellij/using/rules) for more information.

  * Highlight advanced issues (in the IDE) like injection vulnerabilities , detected by SonarQube Server. See [Security-related rules](/sonarqube-server/quality-standards-administration/managing-rules/security-related-rules) for more information.

  * Use the same quality profile locally as is defined on SonarQube Server. See [Understanding quality profiles](/sonarqube-server/quality-standards-administration/managing-quality-profiles/understanding-quality-profiles) for more information.

  * Apply settings, such as rule selection and file exclusion defined on SonarQube Server, to your local analysis.

  * Define specific [Analysis parameters](/sonarqube-server/analyzing-source-code/analysis-parameters) on SonarQube Server, and have those parameters applied locally.

  * Automatically suppress issues that are marked as Accepted or False Positive on SonarQube Server so that locally reported issues match those found on the server.

  * Use the SonarQube for IDE focus on new code features to concentrate detection of issues only in new code. See [Quality standards and new code](/sonarqube-server/user-guide/about-new-code) for more information.

  * Changes in your SonarQube Server quality gate will arrive in your IDE when you accept Smart notifications. See [Understanding quality gates](/sonarqube-server/quality-standards-administration/managing-quality-gates/introduction-to-quality-gates) for more information.

#### 

[hashtag](#using-the-open-in-ide-feature)

Using the Open in IDE feature

If youâ€™re using SonarQube for IDE (IntelliJ, Visual Studio, VS Code, or Eclipse), itâ€™s possible to use the **Open in IDE** button to open most issues in the code editor, speeding up the time it takes to find and fix the issue. Simply select the **Open in IDE** button from SonarQube Server to view it in your IDE; youâ€™ll be prompted to set up Connected Mode if the project is not already bound.

Opening Security hotspots using the **Open in IDE** feature is available for all of the supported IDEs. See [Opening issues in your IDE](/sonarqube-server/user-guide/issues/fixing#opening-in-ide) for more details.

### 

[hashtag](#open-in-ide)

Reviewing issues in your IDE

Seeing an issue directly in the IDE can help you better understand its context. This is the purpose of the **Open in IDE** button that youâ€™ll see as an authenticated user.

This feature is available if youâ€™re using a compatible version and flavor of SonarQube for IDE. The project must be open in the appropriate IDE and bound to the server through connected mode. To learn more about managing issues locally, please check the SonarQube for IDE documentation for your IDE:

  * [Investigating issues](/sonarqube-for-vs-code/using/investigating-issues) in SonarQube for VS Code

  * [Investigating issues](/sonarqube-for-intellij/using/investigating-issues) in SonarQube for IntelliJ

  * [Investigating issues](/sonarqube-for-visual-studio/using/investigating-issues) in SonarQube for Visual Studio

  * [Investigating issues](/sonarqube-for-eclipse/using/investigating-issues) in SonarQube for Eclipse

Simply open a file of a supported language and start coding, and you will start seeing issues highlighted in your code. For example, here is SonarQube for VSCode:

![Issues are highlighted by SonarQube for VS Code in your editor, as you type.](images/img_000_b3750cc8.gif)

Keep in mind that the revision or branch analyzed by SonarQube (Server, Cloud) may not be the same as what you have opened in the IDE. In this case, SonarQube for IDE will do its best to locate the issue in your local code.

### 

[hashtag](#commercial-edition-rules)

Commercial edition rules

There are rules that are available in SonarQube Server but not in SonarQube Community Build. These rules are available only in connected mode in SonarQube for IDE.

### 

[hashtag](#understanding-sonarlint-usage)

Understanding SonarQube for IDE usage

SonarQube Server Instance Admins can access an overview of usersâ€™ usage of SonarQube for IDE by going to **Administration** > **Security** > **Users.**

The **Last SonarQube for IDE connection** column indicates the last time the user used SonarQube for IDE in connected mode.

You can filter users based on their activity. The available options are:

  * **All users**

  * **Active users with SonarQube for IDE** : users of SonarQube for IDE in connected mode who were active at least once in the past 30 days.

  * **Active users without SonarQube for IDE** : users who have connected to SonarQube Server at least once in the past 30 days.

  * **Inactive users** : users who have not connected to SonarQube Server or used SonarQube for IDE in connected mode in the past 30 days.

### 

[hashtag](#smart-notifications)

Smart notifications

Connected mode allows SonarQube (Server, Cloud) to send smart alerts to individuals or teams when new issues are discovered. With everyone in the loop, issues can be addressed promptly, improving the overall software quality and delivery. Youâ€™ll receive smart notifications in your IDE when:

  * the quality gate status of a project _open in your IDE_ changes

  * a SonarQube Server analysis raises new issues _that youâ€™ve introduced in a project open in your IDE_

Each developer must individually activate or deactivate SonarQube for IDE smart notifications directly in SonarQube for IDE on the IDE side. When setting up connected mode for the first time, thereâ€™s a box to check to decide whether or not you want to receive Smart Notifications from SonarQube Server in your IDE.

For all the details about managing notifications, check the SonarQube for IDE documentation that matches your IDE:

  * [Notificationsarrow-up-right](https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/connected-mode#notifications) in SonarQube for VS Code

  * [Notificationsarrow-up-right](https://docs.sonarsource.com/sonarqube-for-intellij/connect-your-ide/connected-mode#notifications) in SonarQube for IntelliJ

  * [Notificationsarrow-up-right](https://docs.sonarsource.com/sonarqube-for-visual-studio/connect-your-ide/connected-mode#notifications) in SonarQube for Visual Studio

  * [Notificationsarrow-up-right](https://docs.sonarsource.com/sonarqube-for-eclipse/connect-your-ide/connect-your-ide/connected-mode#notifications) in SonarQube for Eclipse

### 

[hashtag](#version-support-policy)

SonarQube for IDE - SonarQube Server version support policy

SonarQube for IDE enables users to establish a connection to the latest SonarQube Server version and to the latest LTA (Long-Term Active) version. When a new LTA version is released, we still enable connecting SonarQube for IDE to the previous LTA version for a certain period of time (currently 9 months after the latest LTA release) to allow enough time for organizations to update their SonarQube Server version.

circle-exclamation

 _The 8.9LTA reached its support expiration date (in November â€™23)_.

For more information about long-term support of SonarQube Server, check out our page describing the [Release cycle model](/sonarqube-server/server-update-and-maintenance/update/release-cycle-model). Review your SonarQube for IDE-specific requirements for version-to-version differences.

### 

[hashtag](#troubleshooting-unexpected-analysis-results)

Troubleshooting unexpected analysis results

chevron-rightUnexpected analysis results[hashtag](#unexpected-analysis-results)

Observing different analysis results between SonarQube (Server, Cloud) and SonarQube for IDE can have different causes.

**Some issues might be detected by a third-party**

Due to extensive resource requirements, injection vulnerability and some advanced bug detection rules are ignored by SonarQube for IDE. Please check the analyzer (PMD, Checkstyle, ESLint, PyLint, â€¦). SonarQube for IDE will only run rules from Sonar analyzers including custom rules extending SonarSource analyzers. See [Adding coding rules](/sonarqube-server/extension-guide/adding-coding-rules) for more information. Third-party analyzers usually have their own IDE integration, so we have no plan to run them in SonarQube for IDE.

**Your test files might be mistaken as source files**

Test files can be defined on the server or in the IDE, and when running in connected mode, these test sources will be used by SonarQube for IDE. Each SonarQube for IDE flavor has its own way of detecting which file is considered a test file; in SonarQube for IntelliJ, you must define your test files as a [Test Sources Rootarrow-up-right](https://www.jetbrains.com/help/idea/testing.html#add-test-root). To define test files on the server, see the Setting analysis scope[Introduction](/sonarqube-server/project-administration/adjusting-analysis/setting-analysis-scope/introduction) page.

**Some complex rules are not run in SonarQube for IDE**

Due to extensive resource requirements, injection vulnerabilities and some advanced bug detection rules are ignored by SonarQube for IDE. See [SonarQube for IDE roadmaparrow-up-right](https://www.sonarsource.com/products/sonarlint/roadmap/) for a list of features and enhancements on the horizon.

**Only line-level issues are reported**

Such issues are not displayed in SonarQube for IDE, only in SonarQube Server.

**When analyzing Java files, the analyzer might need some context for some issues to be found**

In IntelliJ, there is no incremental compilation of the .class files found in the compiler output folder; these are only produced or refreshed when the project is built. The workaround is to simply build your project with the green hammer (when using SonarQube for IntelliJ) in the top-right toolbar. The project should be built on a regular basis to keep the compiled files up-to-date and overcome this [known limitationarrow-up-right](https://sonarsource.atlassian.net/browse/SLI-488).

[PreviousUser guidechevron-left](/sonarqube-server/user-guide)[NextViewing projectschevron-right](/sonarqube-server/user-guide/viewing-projects)

Last updated 21 hours ago

Was this helpful?