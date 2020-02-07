# Github GCP cloud function Webhook
This webhook gets triggered when a repository gets created in 'sidshuklaorg'. 
It does the following:

1. *It automates the restrictions on the master branch*
1. *It automates application of restriction on master branch*
1. *It then creates an issue and notifies the owner with restrictions that have been applied on the branch*

The url of the webhook is :

https://us-central1-automlproject-242700.cloudfunctions.net/GitHubWebhook

## Considerations:

1. At the moment, the webhook cloud function is configured to allow un-authenticated invocations, but in next release, additional         measures would be put on to increase security.
1. There could be more robust exception handling in future release
1. The fucntion returns appropraite message string based on the execution path at runtime
1. Some of the variables used in this code could well be replaced with environment variables
1. Authorization used to call github APIs is Basic with bearer token. This could be further enhanced to use Oauth mechanism




