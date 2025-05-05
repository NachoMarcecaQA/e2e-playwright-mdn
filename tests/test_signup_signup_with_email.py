from playwright.sync_api import Page, expect
from helpers.navigation import go_to_signup

def test_signup_happy_path (page: Page):
    go_to_signup(page)

    print("When the user fill email with valid email")
    page.get_by_role("textbox", name="Escribe tu correo electrónico").click()
    page.get_by_role("textbox", name="Escribe tu correo electrónico").fill("test@gmail.com")
    page.get_by_role("button", name="Regístrate o inicia sesión").click()

    print("And the user fill password with valid password")
    page.get_by_test_id("new-password-input-label").click()
    page.get_by_test_id("new-password-input-field").fill("P67jhjsdhhsd")
    page.get_by_test_id("age-input-label").click()

    print("And the user fill password with valid age")
    page.get_by_test_id("age-input-field").fill("33")

    print("And the user clicks on create account")
    page.get_by_role("button", name="Crear cuenta").click()

    print("Then the user should see verify message")
    expect(page.get_by_role("heading", name="Introduce el código de")).to_be_visible
    expect(page.get_by_role("button", name="Confirmar")).to_be_visible


def test_signup_invalid_email (page: Page):
    go_to_signup(page)

    print("When the user fill email with invalid email")
    page.get_by_role("textbox", name="Escribe tu correo electrónico").click()
    page.get_by_role("textbox", name="Escribe tu correo electrónico").fill("test_gmail_com")
    page.get_by_role("button", name="Regístrate o inicia sesión").click()

    print("Then the user should see an error message")
    expect(page.locator("#error-tooltip-1023")).to_contain_text("Introduce una dirección de correo válida")



def test_signup_invalid_password (page: Page):
    go_to_signup(page)

    print("When the user fill email with valid email")
    page.get_by_role("textbox", name="Escribe tu correo electrónico").click()
    page.get_by_role("textbox", name="Escribe tu correo electrónico").fill("test@gmail.com")
    page.get_by_role("button", name="Regístrate o inicia sesión").click()

    print("And the user fill password with valid password")
    page.get_by_test_id("new-password-input-label").click()
    page.get_by_test_id("new-password-input-field").fill("password")
    page.get_by_test_id("age-input-label").click()

    print("And the user fill password with valid age")
    page.get_by_test_id("age-input-field").fill("33")

    print("Then create account should be disabled")
    expect(page.get_by_role("button", name="Crear cuenta")).to_be_disabled()

