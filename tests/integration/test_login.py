import re
from app import User
from reflex.testing import AppHarness
from playwright.sync_api import Page, expect


# Example: https://github.com/reflex-dev/reflex-examples/blob/main/form-designer/tests/test_login.py
# State test example: https://github.com/reflex-dev/reflex/blob/main/tests/integration/test_client_storage.py
def test_login(
        test_app: AppHarness,
        page: Page,
        test_user: User,
        test_user_email: str,
        test_user_password: str,
):
    assert test_app.frontend_url is not None

    def _url(url):
        return re.compile(test_app.frontend_url + url)

    page.goto(test_app.frontend_url + "/login")
    page.set_default_timeout(2500)
    expect(page).to_have_url(_url("/login"))

    page.get_by_placeholder("Username").fill(test_user_email)
    page.get_by_placeholder("Password").fill(test_user_password)
    page.get_by_role("button", name="Login").click()

    expect(page.get_by_text(test_user.first_name)).to_be_visible(timeout=5000)