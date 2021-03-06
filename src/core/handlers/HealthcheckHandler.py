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

from aiohttp import web
from core.server.HandlerBase import  HandlerBase

class HealthcheckHandler(HandlerBase):

    def __init__(self):
        super().__init__(r'/status/healthcheck')

    async def get(self, request):
        response_obj = {'status': 'success'}
        return web.json_response(response_obj)