import uvicorn
from loguru import logger
from dotenv import load_dotenv
load_dotenv()

from digitalgaz.app import app

from digitalgaz.app import app

def main():
    
    logger.remove()
    logger.add("logs/{time}.log",
               level="DEBUG")
    logger.info("Старт скрипта")
    
    uvicorn.run("digitalgaz.app:app", host="localhost", port=3005, reload=True)

if __name__ == '__main__':
    main()

