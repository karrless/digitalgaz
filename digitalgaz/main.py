from loguru import logger


def main():
    logger.remove()
    logger.add("logs/{time}.log",
               level="DEBUG")
    logger.info("Старт скрипта")


if __name__ == '__main__':
    main()
    