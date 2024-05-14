""" Script to load Quran chapters """

import json
from quran_api.chapters.models import Chapter


def run() -> None:
    """Run script"""

    print("Loading Quran chapters")

    Chapter.objects.bulk_create(
        [
            Chapter(
                name=chapter["name"],
                order=chapter["order"],
                type=True if chapter["class"] == "Meccan" else False,
                verse_count=chapter["verses"],
                translation=chapter["translation"],
                transliteration=chapter["transliteration"],
            )
            for chapter in json.load(
                open(
                    "quran-db/json/chapters/chapters-trans.json",
                    "r",
                    encoding="utf-8",
                )
            )
        ]
    )

    print("Done")
