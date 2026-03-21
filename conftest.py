from playwright.sync_api import sync_playwright, Playwright
import pytest


@pytest.fixture(scope="session")
def api_context(playwright: Playwright):
    request_context = playwright.request.new_context()
    yield request_context
    request_context.dispose()




