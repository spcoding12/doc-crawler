# SonarQube glossary

sparkleAskchevron-down

# SonarQube glossary

A list of terms and their definitions that are referenced in the SonarQube Documentation

### 

[hashtag](#a)

A

**application** In SonarQube Server, the aggregation of multiple projects into a synthetic single project. Applications allow you to see your set of projects as a larger, overall meta-project.

**automated code review** A software development process in which static code analysis tools are used to automatically review and analyze the source code for potential issues and coding standard violations. Automated code review accelerates the identification and resolution of code issues and improves code quality (reliability, security, maintainability).

### 

[hashtag](#b)

B

**bug**

Issue type impacting your code in Standard Experience. It is called Reliability in MQR Mode.

### 

[hashtag](#c)

C

**CI/CD host** The host on which the CI/CD pipeline runs and the Sonar scanner analysis is performed.

**code smell**

Issue type impacting your code in Standard Experience. It is called Maintainability in MQR Mode.

**coding attributes**

  * **consistency** : the code is written in a uniform and conventional way. All the code looks similar and follows a regular pattern, even with multiple contributors at different times. Consistent code is:

    * **formatted** : the code presentation is systematic and regular. Non-semantic choices, such as spacing, indentation, and character placement, remain consistent throughout the codebase, maintaining uniformity across files and authors.

    * **conventional** : the code performs tasks with expected instructions. Faced with equally good options, the code adheres to a single choice across all instances, preferring language conventions. This includes using the appropriate programming interfaces and language features.

    * **identifiable** : the names follow a regular structure based on language conventions. The casing, word separators, suffixes, and prefixes used in the identifiers have purpose, without arbitrary differences.

  * **intentionality** : the code is precise and purposeful. Every instruction makes sense, is adequately formed, and clearly communicates its behavior. Intentional code is:

    * **clear** : the code is self-explanatory, transparently communicating its functionality. It is written in a straightforward way that minimizes ambiguity, avoiding unnecessary clever or intricate solutions.

    * **logical** : the code has well-formed and sound instructions that work together. It is free of explicit errors, contradictions, and commands that could be unpredictable or objectionable.

    * **complete** : the code constructs are comprehensive and used adequately and thoroughly. The code is functional and achieves its implied goals. There are no obviously incomplete or lacking solutions.

    * **efficient** : the code uses resources without needless waste. It prioritizes economical options when available, avoiding unnecessary consumption of memory, processor, disk, or network resources.

  * **adaptability** : the code is structured to be easy to evolve and develop with confidence. It makes extending or repurposing its parts easy and promotes localized changes without undesirable side-effects. Adaptable code is:

    * **focused** : the code has a single, narrow, and specific scope. Each unit should have only one concise purpose, without an overwhelming accumulation of instructions or excessive amounts of complexity.

    * **distinct** : the code procedures and data are unique and distinctive, without undue duplication. The codebase has no significant repetition where it could be decomposed into smaller shared segments.

    * **modular** : the code has automated checks that provide confidence in the functionality. It has enough test coverage which enables changes in implementation without the risk of functional regressions.

  * **responsibility** : the code takes into account its ethical obligations on data, as well as societal norms. Responsible code is:

    * **lawful** : the code respects licensing and copyright regulation. It exercises the creatorâ€™s rights and honors otherâ€™s rights to license their own code.

    * **trustworthy** : the code abstains from revealing or hard-coding private information. It preserves sensitive private information such as credentials and personally identifying information.

    * **respectful** : the code refrains from using discriminatory and offensive language. It chooses to prioritize inclusive terminology whenever an alternative exists that conveys the same meaning.

**cognitive complexity** A Sonar exclusive metric formulated to more accurately measure the relative understandability of methods. Cognitive complexity breaks from using mathematical models to assess software maintainability by combining cyclomatic complexity precedents with human assessment. It yields method complexity scores that align well with how developers perceive maintainability.

**connected mode** The mode used by SonarQube for IDE when connected to SonarQube (Cloud, Server) or SonarQube Community Build. This mode allows users to get the most out of the Sonar solution. The mode used by SonarQube for IDE when not in connected mode is called standalone mode.

**cyclomatic complexity** A software metric used to indicate the complexity of a program. It is a quantitative measure of the number of linearly independent paths through a programâ€™s source code.

### 

[hashtag](#d)

D

**deprecated** A warning related to a feature indicating that the feature still works but will not work at some point in the future.

### 

[hashtag](#e)

E

**external issue** An issue detected by an external, third-party analyzer and imported into SonarQube.

**external rule** A rule applied in an external, third-party analyzer, and that raises external issues.

### 

[hashtag](#f)

F

**false positive** Users can assign a false positive status to an issue raised during a code analysis that was wrongly classified as an issue.

### 

[hashtag](#i)

I

**inactive branch** A branch that has not been analyzed for more than seven consecutive days.

**injection vulnerability** This is a security issue that identifies injection risks in the code. SonarQube Server and SonarQube Cloud use taint analysis - a technology used to track tainted data - to detect injection vulnerabilities. Tainted data refers to unsanitized external data, which exposes the code to injection attacks. SonarQube for IDE, in connected mode, can show injection vulnerabilities (also known as taint vulnerabilities) found by SonarQube (Server, Cloud).

**issue** A problem in your code raised by a rule. Each issue is linked to one or more software qualities in MQR mode or one type in Standard Experience, each with a level of severity.

**issue assignee** The user assigned to the issue.

**issue author** The last committer on the issue line.

**issue flow** A path through the code shown in the UI from the source to the sink when the issue originated upstream.

**issue primary location** The location where the issue message is displayed.

**issue secondary location** A location additional to the primary location that may help to understand the issue.

**issue severity** SonarQube Server and SonarQube Community Build:

  * In MQR mode, it represents the impact level of the issue on a given software quality. It is inherited from the rule that raised the issue and may take the following values: Blocker, High, Medium, Low, Info.

  * In Standard mode, it represents the issueâ€™s severity level. It is inherited from the rule that raised the issue and may take the following values: Blocker, Critical, Major, Minor, or Info.

SonarQube Cloud:

  * Software quality severity represents the impact level of the issue on a given software quality. It is inherited from the rule that raised the issue and may take the following values: Blocker, High, Medium, Low, Info.

  * Type severity represents the issueâ€™s severity level. It is inherited from the rule that raised the issue and may take the following values: Blocker, Critical, Major, Minor, or Info.

### 

[hashtag](#k)

K

**keystore** A repository that contains personal certificates, plus the corresponding private keys that are used to identify the owner of the certificate for cryptographic protocols such as TLS.

### 

[hashtag](#l)

L

**language analyzer** An engine used by the SonarScanners to analyze the code files. Depending on the language, different analyzers are used.

**LOC** Lines of Code. Number of analyzed lines of code in all private projects of your SonarQube Cloud organization or of your SonarQube Server instance. The maximum allowed LOC depends on your SonarQube Server edition or SonarQube Cloud organizationâ€™s subscription.

**local user** In SonarQube Server and SonarQube Community Build, if the automatic provisioning mode is enabled with a third-party identity provider (e.g. GitHub or GitLab), all users that are not auto-provisioned (i.e., manually created users, or through another identity provider Just-in-Time-provisioned users), are called local users.

**long-lived branch** A branch that plays a continuous role within the development process of a software project. The main branch of a repository is always considered a long-lived branch, usually representing the next release of the project. SonarQube Cloud processes the analysis of long-lived branches differently from short-lived branches.

### 

[hashtag](#m)

M

**main branch** The default branch. This branch typically corresponds to whatâ€™s being developed for your next release. This branch is usually known within a development team as "main", "develop" or "head" and is analyzed when no specific branch parameters are provided.

**maintainability issue** Issue impacting the maintainability of your code in MQR Mode. It is called Code Smell in Standard Experience.

**measure** The value of a metric for a given file or project at a given time. For example, 125 lines of code on class MyClass or the density of duplicated lines = 30.5% on project myProject can be considered a measure.

**metric** A type of measurement. Metrics can have varying measures over time. A metric may be either qualitative (for example, the density of duplicated lines, line coverage by tests, etc.) or quantitative (for example, the number of lines of code, the complexity, etc.).

**monorepo** A software development strategy in which the code for a number of projects is stored in the same repository.

**MQR mode** Multiple-Quality Rule mode. In this mode, a rule measures the impact on one or several software qualities (e.g., a rule can impact your software reliability and security). A severity is assigned to each software quality associated with the rule and determines how much that software quality is impacted when the rule is broken. Compared to the Standard Experience, this mode offers a more accurate reflection of your softwareâ€™s health through different lenses. The MQR mode is supported in SonarQube (Cloud, Server) and SonarQube Community Build.

### 

[hashtag](#n)

N

**new code** Any line of code added or modified compared to a baseline. The baseline depends on the new code definition applied to the analysis.

**new code definition** The setting that determines what code is considered new code. For example, it may be code that has changed since the previous project version or since a specific date.

### 

[hashtag](#o)

O

**old code** Code that is not considered new code.

**organization** A group of projects on a repository platform. The organization (or workspace, or group) concept is represented in SonarQube Cloud but not in SonarQube Server or Community Build.

**overall code** All code. Consists of both new code and old code.

### 

[hashtag](#p)

P

**PDF report** PDF reports give a periodic, high-level overview of the code state through a number of lenses, including releasability, security, reliability, and maintainability.

**portfolio** A grouping of several projects that enables an aggregate view of the project metrics and risks.

**project** In the Sonar products, the entity that corresponds to a project in the DevOps platform and is related to the repository storing the project code.

**pull request decoration** The display in the DevOps platformsâ€™ interface of the pull request analysis results.

### 

[hashtag](#q)

Q

**quality gate** A set of conditions on quality measures to enforce a quality policy. A project passes its associated quality gate if its analysis results meet the quality gateâ€™s conditions.

**quality profile** Defines a set of rules to be applied during code analysis for a given language.

### 

[hashtag](#r)

R

**reference branch** In SonarQube Server, a new code definition refers to the code that has changed compared to a selected reference branch.

**regulatory report** In SonarQube Server, a zip file containing a snapshot of a branch including a branch overview, the relevant configuration items, and a list of findings (operational risks).

**reindexing** For a SonarQube Server or SonarQube Community Build project, the rebuild of the Elasticsearch indexes.

**reliability issue** Issue impacting the reliability of your code in MQR Mode. It is called Bug in Standard Experience.

**remediation cost** The estimated time required to fix code issues.

**rule** A coding standard or practice that should be followed. The analysis applies the rules defined through the quality profiles to the code. If a rule is broken, an issue is raised.

### 

[hashtag](#s)

S

**scanner** A standalone program that runs on the CI/CD host, manages the analysis of projects, and sends the results to the server. Sonar offers different scanners that can hook up into different systems to automatically extract the projectâ€™s configuration out of that system.

**security hotspot** A security-sensitive piece of code that needs to be manually reviewed. Upon review, users will either find that there is no threat or that there is vulnerable code that needs to be fixed.

**security issue** Issue impacting the security in MQR Mode. It is called Vulnerability in Standard Experience.

**security report** Security reports help users understand where they may have issues related to various security standards.

**short-lived branch** Branches that are intended to exist only temporarily. They are typically a child branch of a long-lived branch and are intended to be merged back into that parent branch within a relatively short period. SonarQube Cloud processes the analysis of short-lived branches differently from long-lived branches.

**snapshot** A set of measures and issues on a given project at a given time. A snapshot is generated for each analysis.

**sonar property** A key/value pair in which the key has the `sonar.<property>` syntax and used to manage parameters in Sonar products.

**Standard Experience** In this mode, a rule impacts either the reliability, maintainability, or security of your code (the respective issues raised are called bugs, code smells, or vulnerabilities). The rule severity measures the severity level of an issue raised by this rule. The Standard Experience is supported in SonarQube Server and SonarQube Community Build.

### 

[hashtag](#t)

T

**taint vulnerability** See _injection vulnerability_ , above.

**technical debt** The estimated time required to fix all issues impacting the maintainability.

### 

[hashtag](#v)

V

**vulnerability**

Issue type impacting your code in Standard Experience. It is called Security in MQR Mode.

[PreviousInternationalizationchevron-left](/sonarqube-server/extension-guide/internationalization)

Was this helpful?