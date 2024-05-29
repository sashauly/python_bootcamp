import socket
import sys
import json
from urllib.parse import parse_qs


def app(environ, start_response):
    """
    The application interface is a callable object

    Args:
        environ (_type_): points to a dictionary containing CGI like
            environment variables which is populated by the server
            for each received request from the client

        start_response (_type_): callback function supplied by the server
            which takes the HTTP status and headers as arguments

    Returns:
        _type_: response_body
    """

    query = environ['QUERY_STRING']
    parameters = parse_query(query)

    # Default response
    status = '404 Not Found'
    credentials = "Unknown"
    print(parameters)

    if 'species' in parameters:
        species = parameters['species']
        if species == "Time Lord":
            credentials = "Rassilon"
            status = '200 OK'

    data = {'credentials': credentials}
    response = json.dumps(data)

    # HTTP headers expected by the client
    # They must be wrapped as a list of tupled pairs:
    # [(Header name, Header value)].
    response_headers = [('Content-Type', 'application/json'),
                        ('Content-Length', str(len(response)))]

    # Send them to the server using the supplied function
    response_header = start_response(status, response_headers)

    # Return the response body.
    return [response_header.encode(), response.encode()]


def start_response(status, response_headers):
    """Start the WSGI response"""
    print('STATUS: ', status)
    response = [f"HTTP/1.1 {status}"]
    for header in response_headers:
        response.append(f"{header[0]}: {header[1]}")
    response.append("\r\n")
    return "\r\n".join(response)


def parse_query(query):
    """Parse the query parameters from a URL"""
    parameters = parse_qs(query)
    for key in parameters:
        # Only keep the first value for each parameter
        parameters[key] = parameters[key][0]
    return parameters


def parse_request(request_data):
    """Parse an HTTP request into a WSGI environment"""
    lines = request_data.splitlines()
    method, path, version = lines[0].split()

    # Split the URI into path and query string
    path_parts = path.split('?')
    if len(path_parts) > 1:
        path, query_string = path_parts
    else:
        path = path_parts[0]
        query_string = ''

    environ = {
        'REQUEST_METHOD': method,
        'PATH_INFO': path,
        'QUERY_STRING': query_string,
        'SERVER_NAME': HOST,
        'SERVER_PORT': str(PORT),
        'wsgi.version': (1, 0),
        'wsgi.input': request_data,
        'wsgi.errors': sys.stderr,
        'wsgi.multithread': False,
        'wsgi.multiprocess': False,
        'wsgi.run_once': False,
    }
    return environ


HOST, PORT = '127.0.0.1', 8888

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))

server.listen(5)
print(f"Listening on http://{HOST}:{PORT}/")

while True:
    client, address = server.accept()
    print(f"New connection from {address}")

    request_data = client.recv(1024).decode('utf-8')

    environ = parse_request(request_data)

    response_body = app(environ, start_response)

    for response_part in response_body:
        client.sendall(response_part)

    client.close()
