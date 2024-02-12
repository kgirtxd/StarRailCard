import asyncio
import starrailcard.honkaicard as cardgen


async def main():
    art = {"Jingliu" : "url"}
    await cardgen.MiHoMoCard(
        characterImgs = art,
        template=2,
        characterName="Jingliu",
        save=True, lang='en'
    ).creat(uid)


asyncio.run(main())