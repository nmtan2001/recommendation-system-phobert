# middleware.py

from django.middleware import common

class CorsMiddleware(common.CommonMiddleware):
    def process_response(self, request, response):
        response["Access-Control-Allow-Origin"] = "*"
        return response
