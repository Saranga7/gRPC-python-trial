import grpc
from concurrent import futures
import time
import functions.calculator as calculator
from python_generated_files import calculator_pb2, calculator_pb2_grpc

_ONE_DAY_IN_SECONDS=86400

class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    def SquareRoot(self, request, context):
        response=calculator_pb2.Number()
        response.value=calculator.square_root(request.value)
        return response

def run():
    server=grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(),server)
    print('Server starting on port 80')
    server.add_insecure_port('[::]:80')
    server.start()

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__=='__main__':
    run()

