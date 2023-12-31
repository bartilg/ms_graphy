import requests

class RestAdapter:
    def __init__(self,hostname: str, api_key: str = '', ver: str = 'v1', ssl_verify: bool = True):
        self.url = "https://{}/{}/".format(hostname, ver)
        self._api_key = api_key
        self._ssl_verify = ssl_verify
        if not ssl_verify:
            # noinspection PyUnresolvedReferences
            requests.packages.urllib3.disable_warnings()

    def get(self, endpoint: str) -> List[Dict]:
        full_url = self.url + endpoint
        headers = {'x-api-key': self._api_key}
        response = requests.get(url=full_url, verify=self._ssl_verify, headers=headers)
        data_out = response.json()
        if response.status_code >= 200 and response.status_code <= 299:     # OK
            return data_out
        raise Exception(data_out["message"])    # Todo: raise custom exception later