"""Example of using the Adapter pattern."""
import socket
# pylint: disable=missing-docstring,too-few-public-methods


class HttpClient(object):
    """HttpClient is an adapter for socket."""
    MAX_RECV_SIZE = 1024
    HTTP_PORT = 80

    def __init__(self, host):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = self.HTTP_PORT

    def get(self, path=None):
        if path is None:
            path = "/"

        self.socket.connect((self.host, self.port))
        self.socket.sendall(
            "GET %s HTTP/1.0\nHost: %s\n\n" % (path, self.host))

        parts = []
        while True:
            part = self.socket.recv(self.MAX_RECV_SIZE)
            if not part:
                break
            parts.append(part)
        self.socket.close()

        return "".join(parts)


def run_http_client():
    client = HttpClient("www.hotnews.ro")
    page = client.get()
    print page


if __name__ == "__main__":
    run_http_client()
