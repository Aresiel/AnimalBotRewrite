import aiohttp
import asyncio
from colorama import Fore, Back, Style


class Response:
    text = None
    status = None
    headers = None

    def __init__(self, text, status, headers):
        self.text = text
        self.status = status
        self.headers = headers


async def async_request(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            text = await res.text()
            status = res.status
            headers = res.headers

            built_res = Response(text=text, status=status, headers=headers)
            return built_res


def info(text):
    print(Fore.WHITE + "[INFO] " + Fore.RESET + text)


def warn(text):
    print(Fore.YELLOW + "[WARN] " + Fore.RESET + text)


def error(text):
    print(Fore.RED + "[ERROR] " + Fore.RESET + text)


def critical(text):
    print(Fore.BLACK + Back.RED + "[CRITICAL] " + text + Style.RESET_ALL)
