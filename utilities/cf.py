import json
import httpx


class CloudFlareUtil:
    def __init__(self, data):
        self.data = data
        self.api_key = data.get('api_key', None)
        self.cf_account = data.get('cf_account', None)
        self.zone_id = data.get('zone_id', None)
        self.dns_record_id = data.get('dns_record_id', None)
        self.a_record_name = data.get('a_record_name', None)
        self.base_url = 'https://api.cloudflare.com/client/v4'

    def verify_token(self) -> bool:
        request_url = (
            f'{self.base_url}/accounts/{self.cf_account}/tokens/verify'
        )
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
        }
        response = httpx.get(request_url, headers=headers)
        response_body = json.loads(response.content)
        if response_body['result']['status'] == 'active':
            return True
        else:
            return False

    def update_zone_record(self, ip=None) -> bool:
        request_url = f'{self.base_url}/zones/{self.zone_id}/dns_records/{self.dns_record_id}'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}',
        }
        body = {
            'id': self.dns_record_id,
            'name': self.a_record_name,
            'type': 'A',
            'content': ip,
            'ttl': 300,
            'comment': f'Auto updated record for {self.a_record_name}',
            'tags': [],
        }

        response = httpx.put(request_url, json=body, headers=headers)

        return response.status_code == 200

    def no_empty_data_values(self) -> bool:
        return all(self.data.values())
