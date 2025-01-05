import logging

class Logger:
    def __init__(self, name='MatrixPiChain'):
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(name)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def debug(self, message):
        self.logger.debug(message)

    def critical(self, message):
        self.logger.critical(message)

    def __repr__(self):
        return f"Logger(name={self.logger.name})"

# Example usage
if __name__ == "__main__":
    logger = Logger()
    logger.info("This is an info message.")
