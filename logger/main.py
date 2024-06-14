from logger import log_message

def main():
    # Example usage of the logger
    log_message("Файл успешно сохранен")  # first call
    log_message("Файл не удалось сохранить")  # second call

if __name__ == "__main__":
    main()
