import logging
from rich.logging import RichHandler

# Configura logging para arquivo e terminal
file_handler = logging.FileHandler("app.log")
console_handler = RichHandler()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[file_handler, console_handler],
)

logger = logging.getLogger("rich_logger")

def info(message):
    logger.info(message)

def error(message):
    logger.error(message)