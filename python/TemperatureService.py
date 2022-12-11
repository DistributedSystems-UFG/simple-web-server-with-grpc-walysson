from concurrent import futures
import logging

import grpc
import TemperatureService_pb2
import TemperatureService_pb2_grpc

eventsDB = []

class TemperatureServer(TemperatureService_pb2_grpc.TemperatureServiceServicer):

    def Createtemperature(self, request, context):
        data = {
            'date': request.date,
            'location': request.location,
            'temperature': request.temperature,
        }
        print(f"Received event: {data}")
        eventsDB.append(data)
        return TemperatureService_pb2.StatusReply(status='OK')
    
    def SearchTemperature(self, request, context):
      data = eventsDB
      if request.location:
          data = [event for event in data if event['location'] == request.location]
      if request.date:
          data = [event for event in data if event['date'] == request.date]
      return TemperatureService_pb2.TemperatureList(temperature_data=data)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    TemperatureService_pb2_grpc.add_TemperatureServiceServicer_to_server(TemperatureServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()