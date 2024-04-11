import http.server


class NoCacheHTTPHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        """
        Overrides default end_headers method
        """
        self.send_cache_headers()
        http.server.SimpleHTTPRequestHandler.end_headers(self)

    def send_cache_headers(self):
        """
        New method to send cache control headers
        """
        cache_control_value = "no-cache, no-store, must-revalidate"
        self.send_header("Cache-Control", cache_control_value)
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")


if __name__ == '__main__':
    http.server.test(HandlerClass=NoCacheHTTPHandler)
