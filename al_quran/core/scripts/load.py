"""A script to load Quran data"""

import json
from pathlib import Path

from al_quran.comp.collections.models import Collection
from al_quran.comp.items.models import Item
from al_quran.comp.languages.models import Language
from al_quran.core.chapters.models import Chapter
from al_quran.core.groups.models import Group
from al_quran.core.pages.models import Page
from al_quran.core.parts.models import Part
from al_quran.core.quarters.models import Quarter
from al_quran.core.verses.models import Verse


def load_chapters(src: Path) -> None:
    """Load chapter data to chapters table."""

    Chapter.objects.bulk_create(
        [
            Chapter(
                name=c["name"],
                order=c["order"],
                type=bool(c["type"]),
                verse_count=c["verse_count"],
                page_count=c["page_count"],
            )
            for c in json.load(
                open(src.joinpath("chapters.json"), "r", encoding="utf-8")
            )
        ]
    )


def load_parts(src: Path) -> None:
    """Load part data to parts table."""

    Part.objects.bulk_create(
        [
            Part(
                name=p["name"], verse_count=p["verse_count"], page_count=p["page_count"]
            )
            for p in json.load(open(src.joinpath("parts.json"), "r", encoding="utf-8"))
        ]
    )


def load_groups(src: Path) -> None:
    """Load group data to groups table."""

    Group.objects.bulk_create(
        [
            Group(
                name=g["name"],
                verse_count=g["verse_count"],
                page_count=g["page_count"],
                part_id=g["part_id"],
            )
            for g in json.load(open(src.joinpath("groups.json"), "r", encoding="utf-8"))
        ]
    )


def load_quarters(src: Path) -> None:
    """Load quarter data to quarters table."""

    Quarter.objects.bulk_create(
        [
            Quarter(
                name=q["name"],
                verse_count=q["verse_count"],
                page_count=q["page_count"],
                part_id=q["part_id"],
                group_id=q["group_id"],
            )
            for q in json.load(
                open(src.joinpath("quarters.json"), "r", encoding="utf-8")
            )
        ]
    )


def load_pages(src: Path) -> None:
    """Load page data to pages table."""

    Page.objects.bulk_create(
        [
            Page(
                name=p["name"],
                verse_count=p["verse_count"],
                chapter_id=p["chapter_id"],
                part_id=p["part_id"],
                group_id=p["group_id"],
                quarter_id=p["quarter_id"],
            )
            for p in json.load(open(src.joinpath("pages.json"), "r", encoding="utf-8"))
        ]
    )


def load_verses(src: Path) -> None:
    """Load verse data to verses table."""

    Verse.objects.bulk_create(
        [
            Verse(
                number=v["number"],
                content=v["content"],
                chapter_id=v["chapter_id"],
                part_id=v["part_id"],
                group_id=v["group_id"],
                quarter_id=v["quarter_id"],
                page_id=v["page_id"],
            )
            for v in json.load(open(src.joinpath("verses.json"), "r", encoding="utf-8"))
        ]
    )


def load_languages(src: Path) -> None:
    """Load language data to languages table."""

    Language.objects.bulk_create(
        [
            Language(name=lang["name"], code=lang["code"])
            for lang in json.load(
                open(src.joinpath("languages.json"), "r", encoding="utf-8")
            )
        ]
    )


def load_collections(src: Path) -> None:
    """Load collection data to collections table."""

    Collection.objects.bulk_create(
        [
            Collection(
                language_id=c["language_id"],
                type=c["type"],
                name=c["name"],
                description=c["description"] if c["description"] else "N/A",
            )
            for c in json.load(
                open(src.joinpath("collections.json"), "r", encoding="utf-8")
            )
        ]
    )


def load_items(src: Path) -> None:
    """Load item data to items table."""

    Item.objects.bulk_create(
        [
            Item(
                collection_id=i["collection_id"],
                chapter_id=i["chapter_id"],
                verse_id=i["verse_id"],
                content=i["content"],
            )
            for i in json.load(open(src.joinpath("items.json"), "r", encoding="utf-8"))
        ]
    )


def load_quran(src: Path) -> None:
    """Load Quran data"""

    load_chapters(src)
    load_parts(src)
    load_groups(src)
    load_quarters(src)
    load_pages(src)
    load_verses(src)


def load_comp(src: Path) -> None:
    """Load complementary data"""

    load_languages(src)
    load_collections(src)
    load_items(src)


def run(src: str = "quran-db/json", with_comp: bool = True) -> None:
    """
    Load quran data

    Args:
        src (str): Path to data
        with_comp (bool): Weather to include complementary data
    """

    src_path = Path(src)
    if not src_path.exists():
        print(
            f"Error: Given src path '{src}' not exists.\n"
            "To get started: https://github.com/youzarsiph/quran-db. "
            "Also you can use Quran CLI for more info: https://github.com/youzarsiph/quran-cli."
        )
        return

    print("Loading Quran data")
    load_quran(src_path)
    print("Done")

    if with_comp:
        print("Loading complementary data")
        load_comp(src_path)
        print("Done")
