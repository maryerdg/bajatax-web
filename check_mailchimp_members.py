import urllib.request
import json
import base64

api_key = '5d84d84bf7ac96ea6f7e9c0e01f8923a-us11'
list_id = '29dd34f8f4'
url = f'https://us11.api.mailchimp.com/3.0/lists/{list_id}/members'

req = urllib.request.Request(url)
base64str = base64.b64encode(f'anystring:{api_key}'.encode('utf-8')).decode('utf-8')
req.add_header('Authorization', f'Basic {base64str}')

try:
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode('utf-8'))
        for mbr in data.get('members', []):
            print(f"Email: {mbr.get('email_address')} - Status: {mbr.get('status')}")
except Exception as e:
    print('API Error:', e)
