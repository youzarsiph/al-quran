""" Script to load Quran data """

import json
from quran_api.chapters.models import Chapter
from quran_api.groups.models import Group
from quran_api.pages.models import Page
from quran_api.parts.models import Part
from quran_api.quarters.models import Quarter
from quran_api.verses.models import Verse


def load_chapters() -> None:
    """Loads chapter data"""

    print("\tLoading Quran chapters")

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


def load_pages() -> None:
    """Loads page data"""

    print("\tLoading Quran Pages")

    Page.objects.bulk_create([Page() for page in range(604)])


def load_verses() -> None:
    """Loads verse data"""

    print("\tLoading Quran verses")

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


def update_pages() -> None:
    """Update pages to add missing fields like chapter"""

    # The problem in verses data, the range is 134-141
    for page in Page.objects.all():
        data = Verse.objects.filter(page=page)[0]
        page.chapter = data.chapter
        page.part = data.part
        page.group = data.group
        page.quarter = data.quarter
        page.save()


def run():
    """Run script"""

    print("Loading Quran")
    load_chapters()
    load_pages()
    load_verses()
    update_pages()
    print("Done")
