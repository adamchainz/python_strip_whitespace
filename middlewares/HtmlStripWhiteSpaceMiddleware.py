"""
This module strips unnecessary whitespaces from HTML.
"""

from django.utils.deprecation import MiddlewareMixin
from .lib import minify


class HTMLStripWhiteSpace(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)  # Get response from view function.

        if not response.streaming:
            content = minify(response.content)
            response.content = content

        return response
