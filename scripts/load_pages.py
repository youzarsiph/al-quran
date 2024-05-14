""" Script to load Quran pages """

from quran_api.pages.models import Page


def run() -> None:
    """Run script"""

    print("Loading Quran Pages")

    Page.objects.bulk_create([Page() for verse in range(604)])

    print("Done")
