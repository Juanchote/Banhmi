#!/usr/bin/python
'''
Author: Albert Monfa

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

from aiohttp.web    import  Response
from aiohttp.web    import  middleware
from aiohttp.web    import  HTTPException, HTTPNotFound

class Authentication(object):

    @middleware
    async def hook(request, handler):

        # TODO
        # Implement something BEFORE executing the Handler

        try:
            response = await handler(request)

            # TODO
            # Implement something BEFORE executing the Handler

            return response
        except HTTPNotFound as ex:
            print(ex.reason)
            response = Response(
                status=404,
            )
            return response
        except HTTPException as ex:
            response = Response(
                status=501,
                reason='Not Implemented',
            )
            return response