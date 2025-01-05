class ErrorHandler:
    @staticmethod
    def handle_error(error):
        # Log the error and return a user-friendly message
        print(f"Error occurred: {str(error)}")
        return "An error occurred. Please try again later."

    @staticmethod
    def handle_validation_error(validation_errors):
        # Log validation errors and return a user-friendly message
        print(f"Validation errors: {validation_errors}")
        return "Validation failed. Please check your input."

    def __repr__(self):
        return "ErrorHandler()"

# Example usage
if __name__ == "__main__":
    handler = ErrorHandler()
    try:
        raise ValueError("This is a test error.")
    except Exception as e:
        print(handler.handle_error(e))
