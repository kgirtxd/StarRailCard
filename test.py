import asyncio
import random
from os import getenv, system
import starrailcard.honkaicard as cardgen
from starrailcard.src.generators import two_new
from honkairail import starrailapi
from PIL import Image
from starrailcard.src.tools import translation




async def main():
    system("cls")
    lang = 'en'
    uid = getenv('UID')
    print(uid)

    # art = {"Jingliu" : "url"}
    # stuff = await cardgen.MiHoMoCard(
    #     # characterImgs = art,
    #     template=2,
    #     # characterName="Sparkle",
    #     save=True,
    #     lang='en'
    # ).get_profile(uid)

    async with cardgen.MiHoMoCard(
        # characterImgs = art,
        template=2,
        # characterName="Sparkle",
        # save=True,
        lang='en'
    ) as generator:
        stuff = await generator.get_profile(uid)
    stuff.card.save("RailCard/test.png")

    # for card in stuff.card:
    #     card.card.save(f"RailCard/{card.name}.png")


    # r = starrailapi.StarRailApi(lang, v = 2)
    # data = await r.get_full_data(uid)

    # gen = await two_new.Creat(
    #     data.characters[random.randint(0, len(data.characters))],
    #     uid=uid,
    # ).start()

    # gen.card.save("RailCard/test.png")



asyncio.run(main())
