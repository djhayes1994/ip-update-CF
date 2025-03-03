import os

import httpx
import json
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("CLOUDFLARE_API_KEY")
cloudflare_account = os.getenv("CLOUDFLARE_ACCOUNT_ID")
cloudflare_email = os.getenv("CLOUDFLARE_EMAIL")
zone_id = os.getenv("CLOUDFLARE_ZONE_ID")
dns_record_id = os.getenv("CLOUDFLARE_DNS_RECORD_ID")
a_record_name = os.getenv("CLOUDFLARE_A_RECORD_NAME")


def get_ip():
    request = httpx.get('https://icanhazip.com')
    return request.text.rstrip()

def verify_token():
    request_url = f'https://api.cloudflare.com/client/v4/accounts/{cloudflare_account}/tokens/verify'
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    response = httpx.get(request_url, headers=headers)
    response_body = json.loads(response.content)
    if response_body['result']['status'] == "active":
        return True
    else:
        return False

def update_zone_record(z_id,dr_id, ip):
    request_url = f'https://api.cloudflare.com/client/v4/zones/{z_id}/dns_records/{dr_id}'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {api_key}"
    }
    body = {
            "id": "850dc78d22d1d122335df2ca0872c754",
            "name": a_record_name,
            "type": "A",
            "content": ip,
            "ttl": 300,
            "comment": "Rewsty Factorio",
            "tags": []
    }

    response = httpx.put(request_url, json=body, headers=headers)

    return response.status_code == 200



current_ip = get_ip()
valid_token = verify_token()

if valid_token:
    update_result = update_zone_record(zone_id, dns_record_id, current_ip)
    if update_result:
        print(f"Successfully updated zone record with value of: {current_ip}")
    else:
        print(f"Failed to update zone record with value of: {current_ip}")