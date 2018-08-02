from requests import request
import json

def make_post_request(url, payload=""):
    """
    Makes post request to blockchain net
        :param url: endpoint for the request
        :param payload: payload to send with the request
    """
    response = request("POST", url, data=payload)
    return json.loads(response.text)
