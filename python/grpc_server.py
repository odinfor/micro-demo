from concurrent import futures
import logging
import grpc

import sys
sys.path.append("python_proto")

from python_proto import jsf_pb2 as js
from python_proto import jsf_pb2_grpc as js_grpc


class Gym(js_grpc.GymServicer):

    def BodyBuilding(self, request, context):
        print("%s在健身, 动作: %s" % (request.name, list(request.actions)))
        return js.Reply(code=0, msg='ok')

    def StudentName(self, request, context):
        print("学员学号: %s" % (request.code))
        student = ["aa", "bb", "cc"]
        return js.StudentReply(code=request.code, name=student[request.code])


def gprc_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    js_grpc.add_GymServicer_to_server(Gym(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    gprc_server()