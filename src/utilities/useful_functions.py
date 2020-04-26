import time
if __name__ == "__main__":
    print("Useful funcions was executed.")
else:
    print("Useful funcions was imported.")
def show_execution_time(args=(1,), func=time.sleep):
    start = time.time()
    func(*args)
    end = time.time()
    return  end - start
