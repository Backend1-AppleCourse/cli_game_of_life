import functools
import logging

# Configure logging to write to a file
log_filename = 'app.log'
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename=log_filename,
                    filemode='a')  # 'a' for append, 'w' for overwrite

def log_function_call(func):
    """
    Decorator to log function execution details, modified to log to a file.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Executing {func.__qualname__} with args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Executed {func.__qualname__}")
        return result
    return wrapper
