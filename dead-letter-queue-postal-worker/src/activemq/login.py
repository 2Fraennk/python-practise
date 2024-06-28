from playwright.sync_api import Page, expect
import time
from properties import Props

now = time.time()

stage = Props.stage
title = Props.title
url = Props.AMQ_URL



def run_login(page: Page) -> None:
    """ Login """
    page.goto(url)
    page.wait_for_url(f"{url}/**")
    expect(page).to_have_title(str(title))


if url is None:
    print("PLEASE SET *_STAGE VARIABLE")
    exit(1)
