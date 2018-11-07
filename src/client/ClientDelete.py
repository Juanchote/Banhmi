#!/usr/bin/python
'''
Copyright 2018 Albert Monfa

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

import aiohttp
import asyncio


class ClientDelete():

    URL_PATTERN = '{0}/file/delete?bucket={1}&key={2}'

    def delete(self, bucket, key, host):
        self.url = str(self.URL_PATTERN).format(host, bucket, key)

        async def async_delete():
            self.session = aiohttp.ClientSession()
            async with self.session.delete(self.url) as resp:
                await self.session.close()
                return resp
        loop = asyncio.get_event_loop()
        resp = loop.run_until_complete(async_delete())
        return resp