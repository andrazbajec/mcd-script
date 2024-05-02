from dotenv import load_dotenv
from service.DiscordService import DiscordService
from service.ImageService import ImageService

if __name__ == '__main__':
    load_dotenv()

    discord_service = DiscordService()
    image_service = ImageService()

    image_path = image_service.screenshot()
    discord_service.send('Message with image', file=image_path)
    discord_service.send('Message without image')

