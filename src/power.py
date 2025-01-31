import psutil

class Powerusage:
    def measure_power_usage(self):
        cpu_percent = psutil.cpu_percent(interval=0)
        return cpu_percent


Power_instance = Powerusage()