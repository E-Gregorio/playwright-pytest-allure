import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def setup():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

# tests/e2e/test_e2e.py
def test_json_placeholder_navigation(setup):
    page = setup
    
    # Navegar a la página principal
    page.goto("https://jsonplaceholder.typicode.com/")
    page.wait_for_load_state("networkidle")
    
    # Verificar que estamos en la página correcta, eliminando espacios en blanco
    title_text = page.locator("header h1").text_content().strip()
    assert title_text == "JSONPlaceholder"