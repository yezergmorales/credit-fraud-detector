from dotenv import load_dotenv
import logging
from my_package.services.hello_world_service import HelloWorldService

load_dotenv()
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)


def main() -> None:
    """Main entry point of the application."""

    # Create an instance of HelloWorldService
    service = HelloWorldService()

    # Call the say_hello method and store the result
    message = service.say_hello()

    # Log the result
    logger.info(message)


if __name__ == "__main__":
    main()
