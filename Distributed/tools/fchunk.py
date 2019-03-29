import services_pb2

_CHUNKER_SIZE = 64 * 1024

def chunk_bytes(path_of_watched_file):
    index = 0
    f = open(path_of_watched_file,"rb")
    data = f.read()
    while index < len(data):
        yield services_pb2.File(chunk=data[index:index+_CHUNKER_SIZE])
        index += _CHUNKER_SIZE