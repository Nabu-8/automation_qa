import logging
from datetime import datetime

logging.basicConfig(
    filename='hb_test.log',
    level=logging.WARNING,
    format='%(asctime)s - %(levelname)s - %(message)s',
    force=True
)

def extract_monitoring_signals_analys_time():
    try:
        with open('hblog.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            filtered_log = []
            for line in lines:
                if "Key TSTFEED0300|7E3E|0400" in line:
                    index = line.find("Timestamp ")
                    if index != -1:
                        time = line[index + len("Timestamp "):index + len("Timestamp ") + 8]
                        filtered_log.append(time)
            return [datetime.strptime(log, "%H:%M:%S") for log in filtered_log]

    except Exception as e:
        return f"Error: {e}"

def create_log_file():
    for index in range(len(sigmals_time) - 1):
        if len(sigmals_time) < 2:
            return  "Not enough sigmals time for calculation"
        delta = (sigmals_time[index] - sigmals_time[index + 1]).total_seconds()

        if 31 < delta < 33:
            logging.warning(
                f"Heartbeat between {sigmals_time[index + 1].time()} and {sigmals_time[index].time()} = {delta:.0f} is > 31 and < 33")
        elif delta >= 33:
            logging.error(f"Heartbeat between {sigmals_time[index + 1].time()} and {sigmals_time[index].time()} = {delta:.0f} >= 33")

if __name__ == "__main__":
    sigmals_time = extract_monitoring_signals_analys_time()

    if isinstance(sigmals_time, list):
        create_log_file()
        print("Done")
    else:
        print(sigmals_time)