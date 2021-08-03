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
    "kangaroo": ["https://i.some-random-api.ml/i9NUUXkJi1.jpg"]
}


def randomAnimal(animal: str) -> str:
    return random.sample(animals[animal], 1)[0] or "https://via.placeholder.com/666x666"


def cycle(item: any, array: list, amount: int) -> list:
    amount = 50  # Hard-coding cause I can't bother changing every line

    array += [item]
    array = array[max(len(array) - amount, 0):]
    return array


async def refreshCat(): cycle(
    json.loads((await helpers.async_request("https://some-random-api.ml/animal/cat")).text)['image'], animals["cat"],
    10)


async def refreshDog(): cycle(
    json.loads((await helpers.async_request("https://some-random-api.ml/animal/dog")).text)['image'], animals["dog"],
    10)


async def refreshPanda(): cycle(
    json.loads((await helpers.async_request("https://some-random-api.ml/animal/panda")).text)['image'],
    animals["panda"], 10)


async def refreshFox(): cycle(
    json.loads((await helpers.async_request("https://some-random-api.ml/animal/fox")).text)['image'], animals["fox"],
    10)


async def refreshRedPanda(): cycle(
    json.loads((await helpers.async_request("https://some-random-api.ml/animal/red_panda")).text)['image'],
    animals["red_panda"], 10)


async def refreshKoala(): cycle(
    json.loads((await helpers.async_request("https://some-random-api.ml/animal/koala")).text)['image'],
    animals["koala"], 10)


async def refreshBird(): cycle(
    json.loads((await helpers.async_request("https://some-random-api.ml/animal/bird")).text)['image'], animals["bird"],
    10)


async def refreshRaccoon(): cycle(
    json.loads((await helpers.async_request("https://some-random-api.ml/animal/raccoon")).text)['image'],
    animals["raccoon"], 10)


async def refreshKangaroo(): cycle(
    json.loads((await helpers.async_request("https://some-random-api.ml/animal/kangaroo")).text)['image'],
    animals["kangaroo"], 10)


async def refreshSomeRandomApiDotML() -> None:
    funcs = [refreshCat, refreshDog, refreshPanda, refreshFox, refreshRedPanda, refreshKoala, refreshBird,
             refreshRaccoon, refreshKangaroo]
    for func in funcs:
        await func()
        await asyncio.sleep(2)

async def startRefreshCycle() -> None:
    scheduler = Scheduler()

    somerandomapidotml_job = CronJob(name="SomeRandomApi.ml").every(30).second.go(refreshSomeRandomApiDotML)
    scheduler.add_job(somerandomapidotml_job)

    loop = asyncio.get_event_loop()
    loop.create_task(scheduler.start())
