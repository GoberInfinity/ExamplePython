from google.protobuf import empty_pb2
import grpc, services_pb2_grpc

def callService(name_service, ip_server, port):
    with grpc.insecure_channel(ip_server + ':' + port) as channel:
        stub = services_pb2_grpc.InformationStub(channel)
        if name_service == "GetBooks":
            response = stub.SendBooks(empty_pb2.Empty())
        elif name_service == "GetHour":
            response = stub.SendHour(empty_pb2.Empty())
        elif name_service == "GetCounter":
            response = stub.SendCounter(empty_pb2.Empty())
        elif name_service == "GetFile":
            response_iterator = stub.SendDB(empty_pb2.Empty())
            response = bytes()
            for chunk_response in response_iterator:
                        response += chunk_response.chunk
                        print('Received %d bytes...', len(chunk_response.chunk))
        return response
