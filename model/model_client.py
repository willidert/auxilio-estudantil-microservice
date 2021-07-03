from __future__ import print_function
import logging

import grpc

import model_pb2
import model_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = model_pb2_grpc.ModelServiceStub(channel)
        feat = [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 3, 1, 2, 3, 3, 5, 2, 1, 3, 2, 1, 0, 0, 0]
        response = stub.MakePrediction(model_pb2.Features(features=feat))
    print(f'Prediction: {response.prediction}')


if __name__ == '__main__':
    logging.basicConfig()
    run()