import json
import requests
import time
import os
def githubfunc(request):
  
    request_json = request.get_json()
    if 'created' in request_json['action']:
        print ('repo action is created')
    else:
        return ('repo action different than created')
    #urlid = 'https://api.github.com/repos/sidshuklaorg/'
    urlid = os.environ.get('REPO_BASE_URL')
    authtoken = os.environ.get('AUTH_TOKEN')
    nullobject = None
    booltrue = True
    """ print (request)"""
    """ print(request_json) """
    """ print (request_json['repository']['name']) """
    """ print (request_json['repository']['owner']['login']) """
    comurl = urlid+ request_json['repository']['name']+'/issues'
    permposturl = urlid + request_json['repository']['name'] + '/branches/master/protection'
    print('url for protection of branch is' + permposturl)
    
    """ ----------making explicit delay, as an issue was observed possibly due to a race condition """
    time.sleep(10)
    
    """  --------------   GET call to test if the branch has been created and has any restriction  """
    
    """
    
    headers = {
    "Authorization" : "Token 4038b25f6c8182b795cc5d303223da3c1e3443fb",
      "Content-Type": "application/json",
        "Accept": "application/vnd.github.luke-cage-preview+json"  
    }
    geturl = 'https://api.github.com/repos/sidshuklaorg/test/branches/master/protection'
    response = requests.request("GET", permposturl, headers=headers)
    print (response.status_code)
    print ('Response of get call ', response.content)
    
    """
    
    """ ------------------------------------ create permissions on the master branch -----------------------------"""
    
    headers = {
        "Authorization": authtoken,
        "Content-Type": "application/json",
        "Accept": "application/vnd.github.luke-cage-preview+json"
    }
      # Create our payload
    data = {
  "required_status_checks": {
                "strict": False,
                "contexts": []
            },
  "enforce_admins": booltrue,
  "required_pull_request_reviews": {
    "dismiss_stale_reviews": booltrue,
    "require_code_owner_reviews": booltrue,
    "required_approving_review_count": 1
  },
  "restrictions": {
    "users": [
      "sidshukla-github"
    ],
    "teams": [
      "github"
    ]
  },
  "required_linear_history": booltrue,
  "allow_force_pushes": booltrue,
  "allow_deletions": booltrue
}

    
    payload = json.dumps(data)

    # Make the post call to add permissions
    response = requests.request("PUT", permposturl, data=payload, headers=headers)
    print (response.status_code)
    print ('Response of put call ', response.content)
    """ permresponse = response.content"""
    permresponse = response.text
    
    
    if response.status_code == 200:
        print ('Successfully created permission')
    else:
        print ('Could not create permission')
    
    """ --------------------------   create an issue with @mention and the permissions on the branch ------------ """
    
    owner = '@' + request_json['repository']['owner']['login']
    headers = {
        "Authorization": authtoken,
        "Content-Type": "application/json"
    }
      # Create our issue
    issuedata = {
 			 "title": "Restrictions applied on master branch",
			  "body": owner + "  . restrictions applied on master is as follows:         "   + payload
			}

    payload = json.dumps(issuedata)

    # Add the issue to our repository
    response = requests.request("POST", comurl, data=payload, headers=headers)
    print (response.status_code)
    print ('Response of post issue call ', response.content)
    if response.status_code == 201:
        print ('Successfully created Issue')
    else:
        print ('Could not create Issue')
    
    
    
    
    return ("end of function execution")