import requests

access_token = 'YOUR_ACCESS_TOKEN'

url = 'https://graph.facebook.com/v13.0/YOUR_PAGE_ID/posts?access_token=' + access_token

response = requests.get(url)
data = response.json()

for post in data['data']:
    post_id = post['id']
    comments_url = f'https://graph.facebook.com/v13.0/{post_id}/reactions?access_token={access_token}'
    comments_response = requests.get(comments_url)
    comments_data = comments_response.json()
    
    for reaction in comments_data['data']:
        if reaction['type'] == 'ANGRY':
            user_id = reaction['id']
