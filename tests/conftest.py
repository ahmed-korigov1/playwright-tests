import pytest
from playwright.sync_api import sync_playwright
from config.settings import ENVIRONMENTS


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="prod",
        help="Environment: prod, stage, dev",
    )


@pytest.fixture
def page(request):
    env = request.config.getoption("--env")
    env_config = ENVIRONMENTS[env]
    base_url = env_config["base_url"]

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.base_url = base_url
        page.env_config = env_config
        yield page
        browser.close()

