import base64, json, urllib.request

with open('/Users/' + __import__('os').environ['USER'] + '/Desktop/mc2/site.html', 'rb') as f:
    content = base64.b64encode(f.read()).decode()

sha_req = urllib.request.Request(
    'https://api.github.com/repos/bthnnzkn/mustafa-calban/contents/index.html',
    headers={'Authorization': 'token YOUR_GITHUB_TOKEN', 'User-Agent': 'Python'}
)
with urllib.request.urlopen(sha_req) as r:
    sha = json.loads(r.read())['sha']

data = json.dumps({'message': 'apple style site', 'content': content, 'sha': sha}).encode()
req = urllib.request.Request(
    'https://api.github.com/repos/bthnnzkn/mustafa-calban/contents/index.html',
    data=data, method='PUT',
    headers={'Authorization': 'token YOUR_GITHUB_TOKEN', 'Content-Type': 'application/json', 'User-Agent': 'Python'}
)
with urllib.request.urlopen(req) as r:
    print('SUCCESS:', json.loads(r.read())['commit']['sha'][:10])
