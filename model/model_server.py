from concurrent import futures
import logging
import pickle

import grpc
import numpy as np

import model_pb2
import model_pb2_grpc


class Model(model_pb2_grpc.ModelServiceServicer):
    __model = pickle.load(open('./model.sav', 'rb'))

    def MakePrediction(self, request, context):
        data = np.array(request.features).reshape(1, -1)
        res = self.__model.predict(data)
        return model_pb2.PredictionResponse(prediction=res[0])


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    model_pb2_grpc.add_ModelServiceServicer_to_server(Model(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()