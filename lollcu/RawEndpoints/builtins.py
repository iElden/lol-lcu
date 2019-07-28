from lollcu.RawRequester import RawRequester

class Builtins:

    def __init__(self, requester):
        """
        Args:
            requester (RawRequester): requester module for make request
        """
        self.requester = requester  # type: RawRequester


    async def async_delete(self, async_token):
        """
        Cancels the asynchronous operation or removes its completion status.
        Args:
            async_token (int): ID of the asynchronous operation to remove
        Returns:
            dict:
        """
        return await self.requester.post("/AsyncDelete", query={"asyncToken": async_token})

    async def async_result(self, async_token):
        """
        Retrieves the result of a completed asynchronous operation.
        Args:
            async_token (int): ID of the asynchronous operation to check
        Returns:
            dict:
        """
        return await self.requester.post("/AsyncResult", query={"asyncToken": async_token})

    async def async_status(self, async_token):
        """
        Retrieves details on the current state of an asynchronous operation
        Args:
            async_token (int): ID of the asynchronous operation to check
        Returns:
            dict:
        """
        return await self.requester.post("/AsyncResult", query={"asyncToken": async_token})

    async def cancel(self, async_token):
        """
        Attempts to cancel an asynchronous operation
        Args:
            async_token (int): Operation to cancel
        Returns:
            dict:
        """
        return await self.requester.post("/Cancel", query={"asyncToken": async_token})

    async def exit(self):
        """
        Closes the connection.
        Returns:
            dict:
        """
        return await self.requester.post("/Exit")

    async def help(self, target=None, format=None):
        """
        Returns information on available functions and types
        Args:
            target (Optional[str]): Name of the function or type to describe
            format (Optional[str]): Format for returned information
        Returns:
            dict: With no arguments, returns a list of all available functions and types along with a short description.
            If a function or type is specified, returns detailed information about it.
        """
        data = {}
        if target:
            data["target"] = target
        if format:
            # TODO: do a assert for check if format is valid
            data["format"] = format
        return await self.requester.post("/Help", query=data if data else None)

    async def subscribe(self, event_name, format=None):
        """
        Subscribes to a given event
        Args:
            event_name (str): Name of the event to subscribe to
            format (Optional[str]): Desired format to receive events in. If unspecified, events will be sent in the active result format at the time.
        Returns:
            dict:
        """
        data = {"eventName": event_name}
        if format:
            data["format"] = format
        return await self.requester.post("/Subscribe", query=data)

    async def unsubscribe(self, event_name):
        """
        Unsubscribes from a given event
        Args:
            event_name (str): Name of the event to unsubscribe from
        Returns:
            dict:
        """
        return await self.requester.post("/Unsubscribe", query={"eventName": event_name})

    async def web_socket_format(self, format=None):
        """
        Controls the console output format
        Args:
            format (Optional[str]): Output format to switch to
        Returns:
            dict: With no arguments, returns the current output format being used.
            If a format is specified, switches the console output to that format.
        """
        return await self.requester.post("/WebSocketFormat", query={"format": format} if format else None)

    async def get_async_result(self, async_token):
        """
        Retrieves the result of a completed asynchronous operation.
        Args:
            async_token (int): ID of the asynchronous operation to check
        Returns:
            dict:
        """
        return await self.requester.get(f"/async/v1/result/{async_token}")

    async def delete_async_status(self, async_token):
        """
        Cancels the asynchronous operation or removes its completion status.
        Args:
            async_token (int): ID of the asynchronous operation to remove
        Returns:
            dict:
        """
        return await self.requester.delete(f"/async/v1/status/{async_token}")

    async def get_async_status(self, async_token):
        """
        Retrieves details on the current state of an asynchronous operation.
        Args:
            async_token (int): ID of the asynchronous operation to check
        Returns:
            dict:
        """
        return await self.requester.get(f"/async/v1/status/{async_token}")

    async def get_swagger_api_doc(self, api=None):
        """
        if API is given, retrieves the API declaration for a supported API.
        Else, retrieves the API documentation resource listing.
        Args:
            api (Optional[str]): API to get a declaration for
        Returns:
            dict:
        """
        if api:
            return await self.requester.get(f"/swagger/v1/api-docs/{api}")
        return await self.requester.get(f"/swagger/v1/api-docs")

    async def get_swagger(self):
        """
        Retrieves the API documentation
        Returns:
            dict:
        """
        return await self.requester.get("/swagger/v2/swagger.json")

    async def get_swagger_openapi(self):
        """
        Retrieves the API documentation
        Returns:
            dict:
        """
        return await self.requester.get("/swagger/v3/openapi.json")