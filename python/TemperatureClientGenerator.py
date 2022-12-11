import datetime
import random
import time
import grpc
import TemperatureService_pb2
import TemperatureService_pb2_grpc

import const

def generate():
    with grpc.insecure_channel(const.IP+':'+const.PORT) as channel:
        stub = TemperatureService_pb2_grpc.TemperatureServiceStub(channel)

        while True:
            time.sleep(5)
            date = datetime.datetime.now().strftime("%Y-%m-%d")
            location = random.choice(['London', 'Paris', 'Berlin', 'Madrid', 'Rome'])
            temperature = random.uniform(20.00, 40.00)
            event = TemperatureService_pb2.Temperature(date=date, location=location, temperature=temperature)
            response = stub.Createtemperature(event)
            print('Generated event:' + response.status)
        

if __name__ == '__main__':
    generate()