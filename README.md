# Github GCP cloud function Webhook
This webhook gets triggered when a repository gets created in 'sidshuklaorg'. It performs the following operations:

1. *It automates application of restriction on master branch*
1. *It then creates an issue and notifies the owner with restrictions that have been applied on the branch*

The url of the webhook is :

https://us-central1-automlproject-242700.cloudfunctions.net/GitHubWebhook

## Runtime Variables

1. AUTH_TOKEN - is the authorized Github API access token. In this example, it uses a Personal access token (PAT)
1. REPO_BASE_URL - is the repository base url (https://api.github.com/repos/orguser/)

## Key behavior

1. This function only gets executed when a repository is created. For all other events such as 'deleted', it returns 'repo action different than created' message back
1. A timer of 10 seconds delay has been applied before the code actually tries to apply restrictions on the master branch. This has been done to remediate an issue that was identified and was related to race condition between the creation of the branch and the application of permissions
1. The apply branch permissions API uses an extra header parameter - "Accept": "application/vnd.github.luke-cage-preview+json"

## Considerations:

1. At the moment, the webhook cloud function is configured to allow un-authenticated invocations, but in future release, additional         measures could be applied to increase security.
1. There could be more robust exception handling in future release
1. The fucntion returns appropraite message string based on the execution path at runtime




