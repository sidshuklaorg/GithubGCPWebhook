import json
import requests
def githubfunc(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_json = request.get_json()
    if 'created' in request_json['action']:
        print ('repo action is created')
    else:
        return ('repo action different than created')
    urlid = 'https://api.github.com/repos/sidshuklaorg/'
    nullobject = None
    booltrue = True
    """ print (request)"""
    """ print(request_json) """
    """ print (request_json['repository']['name']) """
    """ print (request_json['repository']['owner']['login']) """
    comurl = urlid+ request_json['repository']['name']+'/issues'
    permposturl = urlid + request_json['repository']['name'] + '/branches/master/protection'
    
    """ ------------------------------------ create permissions on the master branch -----------------------------"""
    
    headers = {
        "Authorization": "Basic c2lkc2h1a2xhLWdpdGh1YjpBY3RpdmUwMDAk",
        "Content-Type": "application/json",
        "Accept": "application/vnd.github.luke-cage-preview+json"
    }
      # Create our payload
    data = {
  "required_status_checks": None,
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
        "Authorization": "Basic c2lkc2h1a2xhLWdpdGh1YjpBY3RpdmUwMDAk",
        "Content-Type": "application/json"
    }
      # Create our issue
    data = {
 			 "title": "Found a bug",
			  "body": owner + " " + permresponse
			}

    payload = json.dumps(data)

    # Add the issue to our repository
    response = requests.request("POST", comurl, data=payload, headers=headers)
    print (response.status_code)
    print ('Response of post issue call ', response.content)
    if response.status_code == 201:
        print ('Successfully created Issue')
    else:
        print ('Could not create Issue')
    
    
    
    
    return ("end of function execution")