"""Simple JSONPlaceholder API client"""
import requests


class JsonPlaceholder:
    """Simple JSONPlaceholder API client"""
    def __init__(self):
        """
        Create a client to interact with the JSONPlaceholder API
        """
        self.base_url = "https://jsonplaceholder.typicode.com"

    def api_request(self, method, resource, data=None, return_type="json"):
        """
        This method is used to make all REST requests to the API.
        Wrapper methods corresponding to each supported API action are
        used for clarity and allow for expanded functionality as needed.

        :param method: limited to 'get' or 'put' for the purposes of this assessment
        :param resource: The actual API resource to be targeted, i.e. '/posts'
        :param data: dict object that can be used as the body for put requests
        :param return_type: defaults to json, but allows for
        "raw" or "full to obtain the Response content object
        :return: The API response
        """

        request_url = f"{self.base_url}/{resource}"

        # Build GET request
        if method.lower() == "get":
            r = requests.get(request_url, timeout=60)
        # Build PUT request
        elif method.lower() == "put":
            r = requests.put(request_url, data=data, timeout=60)
        else:
            return ValueError("Unsupported method: api_request supports GET & PUT")

        # Verify return_type and return the appropriate data
        if return_type == "json":
            return r.json()
        elif return_type == "raw":
            return r.content
        elif return_type == "full":
            # Returning the full Response object
            return r
        else:
            return ValueError("Unsupported return type: Valid options are json, raw, and full.")

    def get(self, resource, resource_number=None, return_type="json"):
        """
        Wrapper for GET requests

        :param resource:  The actual API resource to be targeted, i.e. '/posts'.
        :param resource_number: Option to return only a select resource number. None = all resources
        :param return_type: defaults to json, but allows for
        "raw" or "full to obtain the Response content object
        :return: The API response
        """
        # Format resource string with post_number. None will retrieve all posts
        full_resource = f"{resource}/{resource_number}" \
            if resource_number is not None else f"{resource}/"
        req = self.api_request("get", full_resource, return_type=return_type)
        return req

    def put(self, resource, data, resource_number=None, return_type="json"):
        """
        Wrapper for PUT requests

        :param resource: The actual API resource to be targeted, i.e. '/posts'.
        :param data: The dict payload object to send as the body for the request
        :param resource_number: Option to return only a select resource number. None = all resources
        :param return_type: defaults to json, but allows for
        "raw" or "full" to obtain the Response content object
        :return: The API response
        """
        # Format resource string with post_number. None will retrieve all posts
        full_resource = f"{resource}/{resource_number}" \
            if resource_number is not None else f"{resource}/"
        req = self.api_request("put", full_resource, data=data, return_type=return_type)
        return req
