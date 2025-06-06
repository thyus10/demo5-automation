from playwright.sync_api import Page
import re

class ProfilePage:
    def __init__(self, page: Page):
        self.page = page
        self.update_icon = page.locator("(//button[contains(@class, 'edit')])[2]")
        self.email = page.locator("//input[@id='email']")
        self.phone = page.locator("//input[@name='phone']")
        self.name = page.locator("//input[@id='name']")
        self.birthday = page.locator("//input[@name='birthday']")

        # Placeholder locators for error messages (replace with actual locators)
        self.birthday_invalid_format_error = page.locator("#birthday-error-message") # Example locator
        self.birthday_invalid_chars_error = page.locator("#birthday-error-message") # Example locator
        self.phone_invalid_chars_error = page.locator("#phone-error-message") # Example locator
        self.phone_too_short_error = page.locator("#phone-error-message") # Example locator
        self.phone_too_long_error = page.locator("#phone-error-message") # Example locator

        # self.male_radio = page.locator("//input[@value='male']")
        # self.female_radio = page.locator("//input[@value='female']")
        self.gender_radio = lambda value: page.locator(f"input[name='gender'][value='{value.lower()}']")

        self.certification = page.locator("//input[@id='certification']")
        self.skill = page.locator("//input[@id='skill']")
        self.save = page.locator("//button[normalize-space()='Save']")
        self.cancel = page.locator("//button[normalize-space()='Cancel']")

    @property
    def edit_icon(self):
        return self.update_icon

    def click_update_icon(self):
        self.edit_icon.wait_for(state='visible')
        self.edit_icon.click()

    def enter_email(self, mail):
        self.email.fill(mail)
        return self

    def enter_phone(self, phone):
        self.phone.fill(phone)
        return self

    def enter_name(self, name):
        self.name.fill(name)
        return self

    def enter_birthday(self, birthday):
        self.birthday.fill(birthday)
        return self

    def select_gender(self, gender):  # gender: "male", "female", "n/a"
        self.gender_radio(gender).check()
        return self

    def enter_certification(self, certification):
        self.certification.fill(certification)
        return self

    def enter_skill(self, skill):
        self.skill.fill(skill)
        self.skill.press("Enter")
        return self

    def enter_profile_modal(self, phone, name, birthday, gender, certification, skill):
        self.enter_phone(phone)\
            .enter_name(name)\
            .enter_birthday(birthday)\
            .select_gender(gender)\
            .enter_certification(certification)\
            .enter_skill(skill)

    @property
    def save_button(self):
        return self.save

    def click_save_button(self):
        self.save_button.click()

    @property
    def cancel_button(self):
        return self.cancel

    def click_cancel_button(self):
        self.cancel_button.click()




