import asyncio
import json
import random
from async_cron.job import CronJob
from async_cron.schedule import Scheduler

import helpers

animals = {
    "cat": ["https://i.imgur.com/IzQ7BFu.jpeg"],
    "dog": ["https://i.some-random-api.ml/GgVmK0NYuF.jpg"],
    "panda": ["https://i.imgur.com/nxwRXLj.jpg"],
    "fox": ["https://i.imgur.com/leQhTWq.jpg"],
    "red_panda": ["https://i.imgur.com/WRgTbTg.png"],
    "koala": ["https://i.some-random-api.ml/RlGn3ccaDk.jpg"],
    "bird": ["https://i.some-random-api.ml/APPe6psfO6.png"],
    "raccoon": ["https://i.some-random-api.ml/4cXzHcEMgo.jpg"],
    "kangaroo": ["https://i.some-random-api.ml/i9NUUXkJi1.jpg"],
    "whale": ["https://api.animality.xyz/images/whale/24.jpg"],
    "bunny": ["https://api.animality.xyz/images/bunny/16.jpg"],
    "lion": ["https://api.animality.xyz/images/lion/8.png"],
    "bear": ["https://api.animality.xyz/images/bear/14.png"],
    "frog": ["https://api.animality.xyz/images/frog/14.png"],
    "duck": ["https://api.animality.xyz/images/duck/11.png"],
    "penguin": ["https://api.animality.xyz/images/penguin/22.png"]
}


def randomAnimal(animal: str) -> str:
    return random.sample(animals[animal], 1)[0] or "https://via.placeholder.com/666x666"


def cycle(item: any, array: list, amount: int) -> list:
    array += [item]
    array = array[max(len(array) - amount, 0):]
    return array


async def refreshSRACat(): cycle(
    json.loads((await helpers.async_request("https://some-random-api.ml/animal/cat")).text)['image'], animals["cat"],
    50)


async def refreshSRADog(): cycle(
    json.loads((await helpers.async_request("https://some-random-api.ml/animal/dog")).text)['image'], animals["dog"],
    50)


async def refreshSRAPanda(): cycle(
    json.loads((await helpers.async_request("https://some-random-api.ml/animal/panda")).text)['image'],
    animals["panda"], 50)


async def refreshSRAFox(): cycle(
    json.loads((await helpers.async_request("https://some-random-api.ml/animal/fox")).text)['image'], animals["fox"],
    50)


async def refreshSRARedPanda(): cycle(
    json.loads((await helpers.async_request("https://some-random-api.ml/animal/red_panda")).text)['image'],
    animals["red_panda"], 50)


async def refreshSRAKoala(): cycle(
    json.loads((await helpers.async_request("https://some-random-api.ml/animal/koala")).text)['image'],
    animals["koala"], 50)


async def refreshSRABird(): cycle(
    json.loads((await helpers.async_request("https://some-random-api.ml/animal/bird")).text)['image'], animals["bird"],
    50)


async def refreshSRARaccoon(): cycle(
    json.loads((await helpers.async_request("https://some-random-api.ml/animal/raccoon")).text)['image'],
    animals["raccoon"], 50)


async def refreshSRAKangaroo(): cycle(
    json.loads((await helpers.async_request("https://some-random-api.ml/animal/kangaroo")).text)['image'],
    animals["kangaroo"], 50)


async def refreshAnimalityWhale(): cycle(
    json.loads((await helpers.async_request("https://api.animality.xyz/img/whale")).text)['link'],
    animals["whale"], 50)


async def refreshAnimalityBunny(): cycle(
    json.loads((await helpers.async_request("https://api.animality.xyz/img/bunny")).text)['link'],
    animals["bunny"], 50)


async def refreshAnimalityLion(): cycle(
    json.loads((await helpers.async_request("https://api.animality.xyz/img/lion")).text)['link'],
    animals["lion"], 50)


async def refreshAnimalityBear(): cycle(
    json.loads((await helpers.async_request("https://api.animality.xyz/img/bear")).text)['link'],
    animals["bear"], 50)


async def refreshAnimalityFrog(): cycle(
    json.loads((await helpers.async_request("https://api.animality.xyz/img/frog")).text)['link'],
    animals["frog"], 50)


async def refreshAnimalityDuck(): cycle(
    json.loads((await helpers.async_request("https://api.animality.xyz/img/duck")).text)['link'],
    animals["duck"], 50)


async def refreshAnimalityPenguin(): cycle(
    json.loads((await helpers.async_request("https://api.animality.xyz/img/penguin")).text)['link'],
    animals["penguin"], 50)


async def refreshSomeRandomApiDotML() -> None:
    funcs = [refreshSRACat, refreshSRADog, refreshSRAPanda, refreshSRAFox, refreshSRARedPanda, refreshSRAKoala, refreshSRABird,
             refreshSRARaccoon, refreshSRAKangaroo]
    for func in funcs:
        try:
            await func()
        except Exception:
            helpers.warn(f"Failure with {func.__name__}")
            await asyncio.sleep(10)
        await asyncio.sleep(2)


async def refreshAnimality() -> None:
    funcs = [refreshAnimalityWhale, refreshAnimalityBunny, refreshAnimalityLion, refreshAnimalityBear, refreshAnimalityFrog, refreshAnimalityDuck, refreshAnimalityPenguin]
    for func in funcs:
        try:
            await func()
        except Exception:
            helpers.warn(f"Failure with {func.__name__}")
            await asyncio.sleep(10)
        await asyncio.sleep(2)


async def startRefreshCycle() -> None:
    scheduler = Scheduler()

    somerandomapidotml_job = CronJob(name="SomeRandomApi.ml").every(30).second.go(refreshSomeRandomApiDotML)
    animality_job = CronJob(name="Animality.xyz").every(30).second.go(refreshAnimality)
    scheduler.add_job(somerandomapidotml_job)
    scheduler.add_job(animality_job)

    loop = asyncio.get_event_loop()
    loop.create_task(scheduler.start())
