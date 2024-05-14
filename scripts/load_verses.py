""" Script to load Quran verses """

import json
from quran_api.chapters.models import Chapter
from quran_api.groups.models import Group
from quran_api.pages.models import Page
from quran_api.parts.models import Part
from quran_api.quarters.models import Quarter
from quran_api.verses.models import Verse


def run() -> None:
    """Run script"""

    print("Loading Quran verses")

    Verse.objects.bulk_create(
        [
            Verse(
                chapter=Chapter.objects.get(id=verse["chapter_id"]),
                part=Part.objects.get_or_create(id=verse["part_id"])[0],
                group=Group.objects.get_or_create(id=verse["group_id"])[0],
                quarter=Quarter.objects.get_or_create(id=verse["quarter_id"])[0],
                page=Page.objects.get_or_create(id=verse["page_id"])[0],
                text=verse["text"],
                number=verse["number"],
                transliteration=verse["transliteration"],
            )
            for verse in json.load(
                open(
                    "quran-db/json/verses/verses-trans.json",
                    "r",
                    encoding="utf-8",
                )
            )
        ]
    )

    print("Done")
