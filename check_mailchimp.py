import urllib.request
import json
import base64

api_key = '5d84d84bf7ac96ea6f7e9c0e01f8923a-us11'
url = 'https://us11.api.mailchimp.com/3.0/lists'

req = urllib.request.Request(url)
base64str = base64.b64encode(f'anystring:{api_key}'.encode('utf-8')).decode('utf-8')
req.add_header('Authorization', f'Basic {base64str}')

try:
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode('utf-8'))
        print('Total Lists:', data.get('total_items', 0))
        for lst in data.get('lists', []):
            print(f"List Name: {lst.get('name')}, List ID: {lst.get('id')}")
            stats = lst.get('stats', {})
            print(f"Subscribers: {stats.get('member_count')}")
            print(f"Web ID (u): {lst.get('web_id')}")
            print(f"List UUID: {lst.get('id')}")
except Exception as e:
    print('API Error:', e)
