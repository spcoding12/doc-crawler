# Managing portfolios

sparkleAskchevron-down

  1. [Project administration](/sonarqube-server/project-administration)

# Managing portfolios

Setting up and managing portfolios in SonarQube Server.

Portfolios are available starting in [_Enterprise Edition_ arrow-up-right](https://www.sonarsource.com/plans-and-pricing/enterprise/).

### 

[hashtag](#permissions)

Permissions

#### 

[hashtag](#creating-portfolios)

Creating portfolios

Users with the **Create Portfolios** permission and global administrators can create portfolios:

  * **Create Portfolios permission** â€“ Users with the **Create Portfolios** permission (granted at the global level at **Administration** > **Security** > **Global Permissions**) can create portfolios by clicking the **Create Portfolio** button in the upper-right corner of the **Portfolios** homepage.

  * **Global Administrators** â€“ In addition to creating portfolios from the **Portfolios** homepage, global administrators (with the global **Administer System** permission granted at **Administration** > **Security** > **Global Permissions**) create portfolios from the overall portfolio administration interface at **Administration** > **Configuration** > **Portfolios**.

#### 

[hashtag](#editing-portfolios)

Editing portfolios

Users need to have either **Administer** permissions for any portfolios that they want to edit or the global **Administer System** permission.

circle-info

Giving a user **Administer** permission to an existing portfolio that was created using manual selection allows that user to see all project names and keys for the projects in the portfolio, even if the user doesnâ€™t have access to those projects.

#### 

[hashtag](#changing-portfoliolevel-permissions)

Changing portfolio-level permissions

With the **Create Portfolios** permission, you can make your portfolios public or private and control their visibility. This allows you to restrict portfolio visibility only to a specific group or individuals who manage a specific aspect of software development in your organization.

  * **Public** portfolios are visible to all users and you can assign specific **Users** and **Groups** to administer them.

  * **Private** portfolios are visible to selected users and groups, and you can assign specific **Users** and **Groups** to administer them.

To change the visibility of your portfolio:

  * Navigate to your portfolio.

  * Click on the **Portfolio Settings** in the top-right corner.

  * Select **Permissions** from the drop-down menu.

  * At the top of the page choose **Public** or **Private**.

  * Select appropriate **Browse** and **Administer** permissions to **Users** and **Groups** from the list.

### 

[hashtag](#populating-portfolios)

Populating portfolios

After youâ€™ve created a portfolio, you can populate it with projects, applications, and other portfolios.

circle-info

**Uniqueness in portfolios**

Project branches, applications, and portfolios can only appear once in any given hierarchy in order to avoid magnifying their impacts on aggregated ratings. The portfolio configuration interface has some logic to prevent obvious duplications (such as manually adding the same project). However, in case of more subtle duplications (for example, due to regular expression or other bulk definition), the calculation of that portfolio will fail with a helpful error message.

#### 

[hashtag](#adding-another-portfolio-to-a-portfolio)

Adding another portfolio to a portfolio

To add another portfolio to your portfolio, from **Administration** > **Configuration** > **Portfolios** click the **Add Portfolio** button at the top of the third column, and choose:

  * **Standard** \- This option allows you to create a new portfolio from scratch and add it to the currently selected portfolio. Once created, you can add projects, applications, and more layers of portfolios.

  * **Local Reference** \- This option allows you to reference an existing portfolio in the currently selected portfolio. Once added, it is not editable here, but must be chosen in the left-most column to be edited.

#### 

[hashtag](#adding-a-project-to-a-portfolio)

Adding a project to a portfolio

To add projects to a portfolio, navigate to the portfolio you want to add a project to. Select **Edit Definition** from **Portfolio Settings**. Click the pencil icon next to **Project selection mode** , and select one of the following options:

  * **Manual** â€“ choose the projects individually.

  * **Tags** \- select one or more project tags. Projects with those tags will automatically be included in the portfolio.

  * **Regular Expression** â€“ specify a regular expression and projects with a matching name OR key will be included.

  * **All Projects** â€“ choose this option to add all projects not already included in this portfolio (directly or via `-portfolio`).

By default, adding a project to a portfolio shows the analysis of the projectâ€™s main branch. See the following section if you want to select a non-main branch or multiple branches for your project.

**Selecting specific project branches for your portfolio**

In some situations, you may want to either monitor a project branch thatâ€™s not your main branch or multiple project branches. For example:

  * Your project has multiple release branches, and you want to monitor them all in a portfolio.

  * Your projectâ€™s main branch isnâ€™t your release branch, and you want to monitor your release branch in your portfolio.

To specify a project branch or branches to monitor in your portfolios, you can do the following:

  * **Manual** â€“ You can use manual selection to select one or multiple project branches. To do this:

    1. From the Portfolio you want to edit, go to **Portfolio Settings > Edit Definition**.

    2. Click the pencil icon next to the **Project selection mode** , set **Manual** as your **Project Selection Mode** , and click **Save**.

    3. Click the pencil icon next to the project you want to monitor.

    4. Select the branches you want to monitor. If you donâ€™t select a branch, the main branch is selected by default.

  * **Tags, Regular Expressions, All Remaining Projects** â€“ To specify a branch to monitor in your portfolios using the tags, regular expressions, or all remaining projects options, do the following:

    1. From the Portfolio you want to edit, go to **Portfolio Settings** > **Edit Definition**.

    2. Click the pencil icon next to the **Project selection mode** , and select your desired **Project Selection Mode**.

    3. Enter the name of the branch you want to monitor in the **Branch selection** field, and click **Save**.

#### 

[hashtag](#adding-applications-to-a-portfolio)

Adding applications to a portfolio

To add an application to a portfolio, make sure your application is already created. Then:

  1. Navigate to the **Portfolios** configuration page by going to **Administration** > **Configuration** > **Portfolios**.

  2. Select the portfolio where you want to add your application.

  3. Click **Add Portfolio**.

  4. Select **Local Reference**.

  5. Choose your application from the drop-down menu and click **Add**.

### 

[hashtag](#calculation)

Calculation

By default, portfolios are queued to be recalculated after each analysis of an included project. For each relevant portfolio, a background task is created, and you can follow the progress on each in the **Administration** > **Projects** > **Background Tasks** by looking at the logs available for each item.

If youâ€™re having performance issues related to the automatic recalculation of large portfolios, you can specify the hours at which you want them to be recalculated. Navigate to the **Administration** > **Configuration** > **General Settings** > **Governance** > **Recalculation** section, and set your **Portfolio Calculation Hours**. Portfolios are queued to be recalculated at the beginning of each hour that you specify. The format is an integer between 0-24. For example, to recalculate portfolios at 1 AM, 2 PM, and 11 PM enter 1, 14, and 23. If this value is empty or invalid, each portfolio will be recalculated immediately after it becomes outdated.

### 

[hashtag](#portfolio-pdf-reports)

Portfolio PDF reports

As a portfolio admin, you can configure how frequently SonarQube Server sends PDF reports for this portfolio:

  * Navigate to the portfolioâ€™s home page then **Portfolio Settings** > **Executive Report** and select an option under **Frequency**.

You have the following options for subscription frequency:

  * **Daily** : report is sent during the first portfolio calculation of the day (if any).

  * **Weekly** : report is sent during the first portfolio calculation of the week (if any) from Monday.

  * **Monthly (default)** : report is sent during the first portfolio calculation of the month (if any), starting from the first day of the current month.

#### 

[hashtag](#sending-portfolio-pdf-reports-to-nonsonarqube-server-users)

Sending portfolio PDF reports to non-SonarQube Server users

Users with administrative rights on a portfolio can send the portfolio PDF report to non-SonarQube Server users by adding their email in the **Other Recipients** field at **Portfolio Settings** > **Executive Report**.

### 

[hashtag](#disable-confidential-header)

Disable Confidential header in Portfolio PDF Reports

Because the toggle defaults to on, all portfolio reports display a Confidential header, but you can disable it.

Users with admin access can change this setting by navigating to **Administration - > Governance -> Portfolio PDF Reports** and switching the toggle off.

### 

[hashtag](#elasticsearch-reindexing)

Elasticsearch reindexing

During Elasticsearch reindexing due to disaster recovery or an upgrade, you wonâ€™t have access to portfolios until all projects are indexed. See [Reindexing](/sonarqube-server/server-update-and-maintenance/maintenance/reindexing) for more information.

[PreviousConfiguring webhookschevron-left](/sonarqube-server/project-administration/webhooks)[NextManaging applicationschevron-right](/sonarqube-server/project-administration/managing-applications)

Was this helpful?