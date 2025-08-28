def log_error(msg,log=[]):
    log.append(msg)
    return log
print(log_error("E1"))
print(log_error("E2"))
print(log_error("E3",[]))
