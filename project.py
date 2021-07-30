import re


class LogMessages():
    def __init__(self, priority, timestamp, task_name, partition_name, message) -> None:
        self.priority = priority
        self.timestamp = timestamp
        self.task_name = task_name
        self.partition_name = partition_name
        self.message = message


def get_logs(file_path, arr=[]):
    test_file = open(file_path, "r")
    lines = test_file.readlines()
    for i in range(len(lines)):
        target_string = lines[i]
        complete_string = re.findall('"([^"]*)"', target_string)
        complete_string[0] = '"'+complete_string[0]+'"'
        target_string = re.sub(complete_string[0], '', target_string)
        word_list = re.split(r"\s+", target_string)
        arr.append(LogMessages(
            word_list[0], word_list[1], word_list[2], word_list[3], complete_string[0]))
    return arr


# print(get_logs("log.txt"))
logMessages = get_logs("log.txt")
for logMessage in logMessages:
    print(logMessage.message)
