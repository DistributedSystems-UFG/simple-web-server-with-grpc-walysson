
import grpc
import TemperatureService_pb2
import TemperatureService_pb2_grpc

import const

def createClient():
    with grpc.insecure_channel(const.IP+':'+const.PORT) as channel:
        stub = TemperatureService_pb2_grpc.TemperatureServiceStub(channel)

        while True:
            date = input("Enter date: ")
            location = input("Enter location: ")
            response = stub.SearchTemperature(TemperatureService_pb2.Query(date=date, location=location))
            print(f"Found {len(response.temperature_data)} registers for {date}.")
            for event in response.temperature_data:
                print(event)
        

if __name__ == '__main__':
    createClient()