from __future__ import print_function
import logging
import grpc
import sys
sys.path.append("python_proto")
from python_proto import jsf_pb2 as js
from python_proto import jsf_pb2_grpc as js_grpc


def run1():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = js_grpc.GymStub(channel)
        response = stub.BodyBuilding(
            js.Person(
            name='chenqionghe', actions=['深蹲', '卧推', '硬拉']
            )
        )
    print('code: %s, msg: %s' % (response.code, response.msg))


def run2():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = js_grpc.GymStub(channel)
        response = stub.StudentName(
            js.Student(code=1)
        )
    print('code: %s, msg: %s' % (response.code, response.name))


if __name__ == '__main__':
    logging.basicConfig()
    run2()