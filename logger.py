class Logger:
    __instance = None

    @staticmethod
    def getInstace():
        if Logger.__instance is None:
            Logger()
        return Logger.__instance

    def __init__(self):
        if Logger.__instance!= None:
            raise Exception("there already exists an instance for this class")
        else:
            self.log_file = open("webapp_log.txt", "a")  # Open log file in append mode
            Logger.__instance = self

    def log_request(self, request):
        self.log_file.write(f"Request: {request}\n")

    def log_response(self, response):
        self.log_file.write(f"Response: {response}\n")

    def close_log(self):
        self.log_file.close()


logger = Logger()


logger.log_request("GET /home")
logger.log_response("200 OK")

logger.log_request("POST /submit")
logger.log_response("404 Bad response")
logger.close_log()

Logger2 = Logger()

