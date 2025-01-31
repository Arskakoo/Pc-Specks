import platform
import psutil
import GPUtil

class FindComponents:
    def __init__(self):
        # Initialize attributes
        self.os = platform.system()
        self.processor = platform.processor()
        self.ram = psutil.virtual_memory().total

        # Search net ports
        try:
            self.net = [ni for ni, tieto in psutil.net_if_addrs().items()]
        except Exception as e:
            self.net = []
            print(f"Error searching network data: {e}")

        # Try searching GPU
        try:
            gpus = GPUtil.getGPUs()
            self.gpu = gpus[0].name if gpus else "Not available"
        except Exception as e:
            self.gpu = "Not available"
            print(f"Error searching graphics card: {e}")

# Create an instance of the class
components_instance = FindComponents()

