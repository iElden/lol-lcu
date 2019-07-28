import aiohttp
import json
from typing import Dict, Tuple, Optional, Any
from .exceptions import HTTPException


class RawRequester:
    def __init__(self, base_url : str, login : str, passwd : str, headers: Dict[str, str]):
        self.base_url = base_url
        self.auth = aiohttp.BasicAuth(login, password=passwd, encoding='UTF-8')
        self.headers = headers

    async def raw_request(self, method: str, url: str, query : Optional[Dict[str, Any]]=None, body : Optional[Any]=None, headers : Optional[dict]=None) -> Optional[Any]:
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            response = await session.request(method, self.base_url + url,
                                             headers={**self.headers, **headers} if headers else self.headers,
                                             auth=self.auth,
                                             params=query,
                                             json=body)
            if response.status // 100 in [4, 5]:
                raise HTTPException(f"Request {method} {url} return status code {response.status}")
            r = await response.text()
            if r:
                return json.loads(r)
            return None

    async def get(self, url : str, headers : Optional[dict]=None) -> Optional[Any]:
        return await self.raw_request('GET', url, headers=headers)

    async def post(self, url : str, query : Optional[Dict[str, Any]], body : Optional[Any]=None, headers : Optional[dict]=None) -> Optional[Any]:
        return await self.raw_request('POST', url, query=query, body=body, headers=headers)

    async def put(self, url : str, query : Optional[Dict[str, Any]], body : Optional[Any]=None, headers : Optional[dict]=None) -> Optional[Any]:
        return await self.raw_request('PUT', url, query=query, body=body, headers=headers)

    async def patch(self, url : str, query : Optional[Dict[str, Any]], body : Optional[Any]=None, headers : Optional[dict]=None) -> Optional[Any]:
        return await self.raw_request('PATCH', url, query=query, body=body, headers=headers)

    async def delete(self, url : str, headers : Optional[dict]=None) -> Optional[Any]:
        return await self.raw_request('PATCH', url, headers=headers)
