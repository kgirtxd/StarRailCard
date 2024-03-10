"A Fixed, typed, and streamlined version of the original"
from honkairail import starrailapi
import asyncio,re,os,datetime

from .src.tools import translation, pill, modal, openFile
from .src.generators import one, two, tree,four,five, author, profile, relicts,two_new
from starrailcard.src.tools import translation
import honkaicard


class StarRailGraphics:
    def __init__(
            self,
            lang:str = 'en',
            img_dict:dict = None,
            character_name:str = None,
            hide_uid:bool = False,
            disable_alt_img:bool = False,
            use_seeleland:bool = False,
        ):
        if lang not in translation.supportLang:
            self.lang = translation.Translator("en")
        else:
            self.lang = translation.Translator(lang)

        self.img_dict = img_dict
        self.character_name = character_name
        self.hide_uid = hide_uid
        self.disable_alt_img = disable_alt_img
        self.use_seeleland = use_seeleland

        self.api = starrailapi.StarRailApi(lang, v = 2)

    async def get_profile(self, uid:str, banner = None,):
        data = await self.api.get_full_data(uid)
        banner = await pill.get_user_image(banner)
        return await profile.Creat(
            data,
            self.lang,
            self.img_dict,
            self.hide_uid
        ).start()