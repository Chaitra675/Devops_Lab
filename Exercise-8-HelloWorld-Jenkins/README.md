\# Exercise 8: Hello World Jenkins Job



\## Objective

To create a Jenkins Freestyle job that fetches a shell script from GitHub and executes it.



\## Tools Used

\- Git and GitHub

\- Jenkins running in Docker

\- Visual Studio Code

\- PowerShell



\## GitHub Repository

https://github.com/Chaitra675/devops-sample-code



\## Script: hello-world.sh

```bash

\#!/bin/bash

echo "Hello, Jenkins!"

```



\## Jenkins Configuration

\- Job Name: HelloWorld

\- Job Type: Freestyle project

\- Source Code Management: Git

\- Branch: main

\- Build Step: Execute shell

\- Command: `sh hello-world.sh`



\## Result

The Jenkins job successfully fetched the script from GitHub and executed it.



Console output included:

```text

Hello, Jenkins!

Finished: SUCCESS

```



\## Conclusion

Successfully configured and executed a Jenkins Freestyle job using a shell script stored in GitHub.

