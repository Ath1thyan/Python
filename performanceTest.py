import time

def performance_test():
    start_time = time.time()
    
    # Adjust the range for the loop to test different performance levels
    for i in range(100**10):
        pass  # Do nothing, just loop
    
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")

if __name__ == "__main__":
    performance_test()
