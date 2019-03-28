class Services(services_pb2_grpc.InformationServicer):
    def SayHello(self, request, context):
        global counter
        counter += 1
        return services_pb2.HelloReply(message='Hello, %s!' % request.name + str(counter))

    def Chunker(self, request, unused_context):
        return _chunk_bytes(_CHUNKER_SIZE)