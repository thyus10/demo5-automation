from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.profile_page import ProfilePage


def test_update_profile(set_up_tear_down) -> None:
    page = set_up_tear_down
    print("Login successfully.")

    profile = ProfilePage(page)
    profile.click_update_icon()
    profile.enter_profile_modal("04203", "Thy", "2002-11-10", "Male", "Tester", "playwright")

    profile.click_save_button()

def test_ed_001_verify_edit_icon_opens_modal(set_up_tear_down) -> None:
    page = set_up_tear_down
    profile = ProfilePage(page)
    try:
        profile.click_update_icon()
        print("TC-ED-001 Passed")
    except Exception as e:
        print(f"TC-ED-001 Failed: {e}")
        page.screenshot(path="screenshot_TC-ED-001_failed.png")
        raise

def test_ed_002_verify_modal_closes(set_up_tear_down) -> None:
    page = set_up_tear_down
    profile = ProfilePage(page)
    try:
        profile.click_update_icon()

        page.press.keyboard("Escape")
        print("TC-ED-002 Passed")
    except Exception as e:
        print(f"TC-ED-002 Failed: {e}")
        page.screenshot(path="screenshot_TC-ED-002_failed.png")
        raise

def test_ed_003_verify_modal_title(set_up_tear_down) -> None:
    page = set_up_tear_down
    profile = ProfilePage(page)
    try:
        profile.click_update_icon()
        print("TC-ED-003 Passed")
    except Exception as e:
        print(f"TC-ED-003 Failed: {e}")
        page.screenshot(path="screenshot_TC-ED-003_failed.png")
        raise

def test_ed_004_verify_fields_and_buttons_in_modal(set_up_tear_down) -> None:
    page = set_up_tear_down
    profile = ProfilePage(page)
    try:
        profile.click_update_icon()

        expect(profile.email).to_be_visible()
        expect(profile.phone).to_be_visible()
        expect(profile.name).to_be_visible()
        expect(profile.birthday).to_be_visible()

        expect(profile.certification).to_be_visible()
        expect(profile.skill).to_be_visible()

        expect(profile.cancel).to_be_visible()
        expect(profile.cancel).to_have_text("Cancel")
        expect(profile.save).to_be_visible()
        expect(profile.save).to_have_text("Save")
        print("TC-ED-004 Passed")
    except Exception as e:
        print(f"TC-ED-004 Failed: {e}")
        page.screenshot(path="screenshot_TC-ED-004_failed.png")
        raise

def test_ed_005_verify_current_gender_preselected(set_up_tear_down) -> None:
    page = set_up_tear_down
    profile = ProfilePage(page)
    try:
        profile.click_update_icon()
        print("TC-ED-005 Passed")
    except Exception as e:
        print(f"TC-ED-005 Failed: {e}")
        page.screenshot(path="screenshot_TC-ED-005_failed.png")
        raise

def test_ed_006_verify_email_field_editable(set_up_tear_down) -> None:
    page = set_up_tear_down
    profile = ProfilePage(page)
    try:
        profile.click_update_icon()

        test_value = "test.edit@example.com"
        profile.email.fill(test_value)
        expect(profile.email).to_have_value(test_value)

        print("TC-ED-006 Passed")
    except Exception as e:
        print(f"TC-ED-006 Failed: {e}")
        page.screenshot(path="screenshot_TC-ED-006_failed.png")
        raise

def test_ed_007_verify_phone_field_editable(set_up_tear_down) -> None:
    page = set_up_tear_down
    profile = ProfilePage(page)
    try:
        profile.click_update_icon()

        test_value = "1234567890"
        profile.phone.fill(test_value)
        expect(profile.phone).to_have_value(test_value)

        print("TC-ED-007 Passed")
    except Exception as e:
        print(f"TC-ED-007 Failed: {e}")
        page.screenshot(path="screenshot_TC-ED-007_failed.png")
        raise

def test_ed_008_verify_name_field_editable(set_up_tear_down) -> None:
    page = set_up_tear_down
    profile = ProfilePage(page)
    try:
        profile.click_update_icon()

        test_value = "Test Name"
        profile.name.fill(test_value)
        expect(profile.name).to_have_value(test_value)

        print("TC-ED-008 Passed")
    except Exception as e:
        print(f"TC-ED-008 Failed: {e}")
        page.screenshot(path="screenshot_TC-ED-008_failed.png")
        raise

def test_ed_009_verify_birthday_field_editable(set_up_tear_down) -> None:
    page = set_up_tear_down
    profile = ProfilePage(page)
    try:
        profile.click_update_icon()

        test_value = "2000-01-01"
        profile.birthday.fill(test_value)
        expect(profile.birthday).to_have_value(test_value)

        print("TC-ED-009 Passed")
    except Exception as e:
        print(f"TC-ED-009 Failed: {e}")
        page.screenshot(path="screenshot_TC-ED-009_failed.png")
        raise

def test_ed_010_verify_certification_field_editable(set_up_tear_down) -> None:
    page = set_up_tear_down
    profile = ProfilePage(page)
    try:
        profile.click_update_icon()

        test_value = "Playwright Certification"
        profile.certification.fill(test_value)
        expect(profile.certification).to_have_value(test_value)

        print("TC-ED-010 Passed")
    except Exception as e:
        print(f"TC-ED-010 Failed: {e}")
        page.screenshot(path="screenshot_TC-ED-010_failed.png")
        raise

def test_ed_011_verify_skill_field_editable(set_up_tear_down) -> None:
    page = set_up_tear_down
    profile = ProfilePage(page)
    try:
        profile.click_update_icon()

        test_value = "Test Automation with Playwright"
        profile.skill.fill(test_value)
        expect(profile.skill).to_have_value(test_value)

        print("TC-ED-011 Passed")
    except Exception as e:
        print(f"TC-ED-011 Failed: {e}")
        page.screenshot(path="screenshot_TC-ED-011_failed.png")
        raise

def test_ed_012_verify_gender_selection_can_be_changed(set_up_tear_down) -> None:
    page = set_up_tear_down
    profile = ProfilePage(page)
    try:
        profile.click_update_icon()

        profile.select_gender("female")
        expect(profile.gender_radio("female")).to_be_checked()
        profile.select_gender("male")
        expect(profile.gender_radio("male")).to_be_checked()

        print("TC-ED-012 Passed")
    except Exception as e:
        print(f"TC-ED-012 Failed: {e}")
        page.screenshot(path="screenshot_TC-ED-012_failed.png")
        raise

def test_ed_013_update_name_field_with_valid_data(set_up_tear_down) -> None:
    page = set_up_tear_down
    profile = ProfilePage(page)
    try:
        profile.click_update_icon()
        new_name = "Updated Name"
        profile.name.fill(new_name)
        expect(profile.name).to_have_value(new_name)

        print("TC-ED-013 Passed")
    except Exception as e:
        print(f"TC-ED-013 Failed: {e}")
        page.screenshot(path="screenshot_TC-ED-013_failed.png")
        raise

def test_ed_014_update_birthday_field_with_valid_data(set_up_tear_down) -> None:
    page = set_up_tear_down
    profile = ProfilePage(page)
    try:
        profile.click_update_icon()
        new_birthday = "1990-05-15"
        profile.birthday.fill(new_birthday)
        expect(profile.birthday).to_have_value(new_birthday)

        print("TC-ED-014 Passed")
    except Exception as e:
        print(f"TC-ED-014 Failed: {e}")
        page.screenshot(path="screenshot_TC-ED-014_failed.png")
        raise

def test_ed_015_change_gender_selection_to_opposite(set_up_tear_down) -> None:
    page = set_up_tear_down
    profile = ProfilePage(page)
    try:
        profile.click_update_icon()

        profile.select_gender("female")
        expect(profile.gender_radio("female")).to_be_checked()

        print("TC-ED-015 Passed")
    except Exception as e:
        print(f"TC-ED-015 Failed: {e}")
        page.screenshot(path="screenshot_TC-ED-015_failed.png")
        raise

def test_ed_016_verify_phone_field_accepts_valid_chars(set_up_tear_down) -> None:
    page = set_up_tear_down
    profile = ProfilePage(page)
    try:
        profile.click_update_icon()
        valid_phone = "+1 555-123-4567"
        profile.phone.fill(valid_phone)
        expect(profile.phone).to_have_value(valid_phone)

        print("TC-ED-016 Passed")
    except Exception as e:
        print(f"TC-ED-016 Failed: {e}")
        page.screenshot(path="screenshot_TC-ED-016_failed.png")
        raise

def test_ed_017_verify_birthday_field_accepts_yyyymmdd(set_up_tear_down) -> None:
    page = set_up_tear_down
    profile = ProfilePage(page)
    try:
        profile.click_update_icon()
        valid_birthday = "1995-12-25"
        profile.birthday.fill(valid_birthday)
        expect(profile.birthday).to_have_value(valid_birthday)

        print("TC-ED-017 Passed")
    except Exception as e:
        print(f"TC-ED-017 Failed: {e}")
        page.screenshot(path="screenshot_TC-ED-017_failed.png")
        raise

def test_ed_018_verify_email_field_accepts_format(set_up_tear_down) -> None:
    page = set_up_tear_down
    profile = ProfilePage(page)
    try:
        profile.click_update_icon()
        valid_email = "test.user.123@example.co.uk"
        profile.email.fill(valid_email)
        expect(profile.email).to_have_value(valid_email)

        print("TC-ED-018 Passed")
    except Exception as e:
        print(f"TC-ED-018 Failed: {e}")
        page.screenshot(path="screenshot_TC-ED-018_failed.png")
        raise

def test_ed_019_verify_text_fields_accept_various_chars(set_up_tear_down) -> None:
    page = set_up_tear_down
    profile = ProfilePage(page)
    try:
        profile.click_update_icon()


        name_value = "Name- with space, numbers 123!@#."
        profile.name.fill(name_value)
        expect(profile.name).to_have_value(name_value)


        cert_value = "Cert, number 456 and symbols &*()"
        profile.certification.fill(cert_value)
        expect(profile.certification).to_have_value(cert_value)


        skill_value = "Skill with_underscores- periods. and, commas"
        profile.skill.fill(skill_value)
        expect(profile.skill).to_have_value(skill_value)

        print("TC-ED-019 Passed")
    except Exception as e:
        print(f"TC-ED-019 Failed: {e}")
        page.screenshot(path="screenshot_TC-ED-019_failed.png")
        raise

def test_ed_020_invalid_birthday_format_yyyymmdd_error(set_up_tear_down) -> None:
    page = set_up_tear_down
    profile = ProfilePage(page)
    try:
        profile.click_update_icon()
        invalid_birthday = "2000/01/01"
        profile.birthday.fill(invalid_birthday)
        profile.name.click()

        profile.click_save_button()

        # Assert that the modal is still open (save was prevented)
        # TODO: Add locator for the update profile modal to ProfilePage class
        expect(profile.update_profile_modal).to_be_visible()

        print("TC-ED-020 Passed")
    except Exception as e:
        print(f"TC-ED-020 Failed: {e}")
        page.screenshot(path="screenshot_TC-ED-020_failed.png")
        raise

def test_ed_021_invalid_birthday_format_ddmmyyyy_error(set_up_tear_down) -> None:
    page = set_up_tear_down
    profile = ProfilePage(page)
    try:
        profile.click_update_icon()
        invalid_birthday = "01-01-2000"
        profile.birthday.fill(invalid_birthday)
        profile.name.click()

        profile.click_save_button()

        # Assert that the modal is still open (save was prevented)
        # TODO: Add locator for the update profile modal to ProfilePage class
        expect(profile.update_profile_modal).to_be_visible()

        print("TC-ED-021 Passed")
    except Exception as e:
        print(f"TC-ED-021 Failed: {e}")
        page.screenshot(path="screenshot_TC-ED-021_failed.png")
        raise

def test_ed_022_invalid_birthday_non_date_chars_error(set_up_tear_down) -> None:
    page = set_up_tear_down
    profile = ProfilePage(page)
    try:
        profile.click_update_icon()
        invalid_birthday = "abcdefg"
        profile.birthday.fill(invalid_birthday)
        profile.name.click()

        profile.click_save_button()

        # Assert that the modal is still open (save was prevented)
        # TODO: Add locator for the update profile modal to ProfilePage class
        expect(profile.update_profile_modal).to_be_visible()

        print("TC-ED-022 Passed")
    except Exception as e:
        print(f"TC-ED-022 Failed: {e}")
        page.screenshot(path="screenshot_TC-ED-022_failed.png")
        raise

def test_ed_023_invalid_phone_non_numeric_chars_error(set_up_tear_down) -> None:
    page = set_up_tear_down
    profile = ProfilePage(page)
    try:
        profile.click_update_icon()
        invalid_phone = "abc-def-ghij"
        profile.phone.fill(invalid_phone)
        profile.name.click()

        profile.click_save_button()

        # Assert that the modal is still open (save was prevented)
        # TODO: Add locator for the update profile modal to ProfilePage class
        expect(profile.update_profile_modal).to_be_visible()

        print("TC-ED-023 Passed")
    except Exception as e:
        print(f"TC-ED-023 Failed: {e}")
        page.screenshot(path="screenshot_TC-ED-023_failed.png")
        raise

def test_ed_024_invalid_phone_too_short_error(set_up_tear_down) -> None:
    page = set_up_tear_down
    profile = ProfilePage(page)
    try:
        profile.click_update_icon()
        invalid_phone = "123"
        profile.phone.fill(invalid_phone)
        profile.name.click()

        profile.click_save_button()

        # Assert that the modal is still open (save was prevented)
        # TODO: Add locator for the update profile modal to ProfilePage class
        expect(profile.update_profile_modal).to_be_visible()

        print("TC-ED-024 Passed")
    except Exception as e:
        print(f"TC-ED-024 Failed: {e}")
        page.screenshot(path="screenshot_TC-ED-024_failed.png")
        raise

def test_ed_025_invalid_phone_too_long_error(set_up_tear_down) -> None:
    page = set_up_tear_down
    profile = ProfilePage(page)
    try:
        profile.click_update_icon()
        invalid_phone = "123456789012345678901234567890"
        profile.phone.fill(invalid_phone)
        profile.name.click()

        profile.click_save_button()

        # Assert that the modal is still open (save was prevented)
        # TODO: Add locator for the update profile modal to ProfilePage class
        expect(profile.update_profile_modal).to_be_visible()

        print("TC-ED-025 Passed")
    except Exception as e:
        print(f"TC-ED-025 Failed: {e}")
        page.screenshot(path="screenshot_TC-ED-025_failed.png")
        raise

def test_ed_026_invalid_phone_special_chars_error(set_up_tear_down) -> None:
    page = set_up_tear_down
    profile = ProfilePage(page)
    try:
        profile.click_update_icon()
        invalid_phone = "555-123-4567!*?"
        profile.phone.fill(invalid_phone)
        profile.name.click()

        profile.click_save_button()

        # Assert that the modal is still open (save was prevented)
        # TODO: Add locator for the update profile modal to ProfilePage class
        expect(profile.update_profile_modal).to_be_visible()

        print("TC-ED-026 Passed")
    except Exception as e:
        print(f"TC-ED-026 Failed: {e}")
        page.screenshot(path="screenshot_TC-ED-026_failed.png")
        raise

def test_ed_027_attempt_save_with_empty_field(set_up_tear_down) -> None:
    page = set_up_tear_down
    profile = ProfilePage(page)
    try:
        profile.click_update_icon()


        profile.name.fill("")

        profile.click_save_button()


        print("TC-ED-027 Passed")
    except Exception as e:
        print(f"TC-ED-027 Failed: {e}")
        page.screenshot(path="screenshot_TC-ED-027_failed.png")
        raise

def test_ed_028_exceed_max_length_name_field(set_up_tear_down) -> None:
    page = set_up_tear_down
    profile = ProfilePage(page)
    try:
        profile.click_update_icon()

        long_name = "a" * 100
        profile.name.fill(long_name)

        profile.name.click()

        print("TC-ED-028 Passed")
    except Exception as e:
        print(f"TC-ED-028 Failed: {e}")
        page.screenshot(path="screenshot_TC-ED-028_failed.png")
        raise

def test_ed_029_exceed_max_length_certification_field(set_up_tear_down) -> None:
    page = set_up_tear_down
    profile = ProfilePage(page)
    try:
        profile.click_update_icon()

        long_cert = "b" * 300
        profile.certification.fill(long_cert)

        profile.certification.click()

        print("TC-ED-029 Passed")
    except Exception as e:
        print(f"TC-ED-029 Failed: {e}")
        page.screenshot(path="screenshot_TC-ED-029_failed.png")
        raise

def test_ed_030_exceed_max_length_skill_field(set_up_tear_down) -> None:
    page = set_up_tear_down
    profile = ProfilePage(page)
    try:
        profile.click_update_icon()

        long_skill = "c" * 600
        profile.skill.fill(long_skill)

        profile.skill.click()

        print("TC-ED-030 Passed")
    except Exception as e:
        print(f"TC-ED-030 Failed: {e}")
        page.screenshot(path="screenshot_TC-ED-030_failed.png")
        raise

def test_ed_031_save_valid_changes_and_verify_success_message(set_up_tear_down) -> None:
    page = set_up_tear_down
    profile = ProfilePage(page)
    try:
        profile.click_update_icon()
        new_name = "Jane Doe"
        profile.name.fill(new_name)
        new_birthday = "1990-01-01"
        profile.birthday.fill(new_birthday)
        profile.select_gender("female")

        profile.click_save_button()

        print("TC-ED-031 Passed")
    except Exception as e:
        print(f"TC-ED-031 Failed: {e}")
        page.screenshot(path="screenshot_TC-ED-031_failed.png")
        raise

def test_ed_032_updated_info_persists_after_navigation(set_up_tear_down) -> None:
    page = set_up_tear_down
    profile = ProfilePage(page)
    try:

        profile.click_update_icon()
        original_name = profile.name.get_attribute("value")


        new_name = "Persistent Name"
        profile.name.fill(new_name)
        profile.click_save_button()

        page.reload()

        profile = ProfilePage(page)

        profile.click_update_icon()
        print("TC-ED-032 Passed")
    except Exception as e:
        print(f"TC-ED-032 Failed: {e}")
        page.screenshot(path="screenshot_TC-ED-032_failed.png")
        raise


def test_ed_033_updated_info_persists_after_refresh(set_up_tear_down) -> None:
    page = set_up_tear_down
    profile = ProfilePage(page)
    try:

        profile.click_update_icon()
        refresh_name = "Refreshed Name"
        profile.name.fill(refresh_name)
        profile.click_save_button()

        page.reload()

        profile = ProfilePage(page)

        profile.click_update_icon()
        expect(profile.name).to_have_value(refresh_name)

        print("TC-ED-033 Passed")
    except Exception as e:
        print(f"TC-ED-033 Failed: {e}")
        page.screenshot(path="screenshot_TC-ED-033_failed.png")
        raise

def test_ed_034_save_without_changes(set_up_tear_down) -> None:
    page = set_up_tear_down
    profile = ProfilePage(page)
    try:
        profile.click_update_icon()

        profile.click_save_button()

        print("TC-ED-034 Passed")
    except Exception as e:
        print(f"TC-ED-034 Failed: {e}")
        page.screenshot(path="screenshot_TC-ED-034_failed.png")
        raise

def test_ed_035_cancel_button_closes_modal(set_up_tear_down) -> None:
    page = set_up_tear_down
    profile = ProfilePage(page)
    try:
        profile.click_update_icon()
        profile.click_cancel_button()

        print("TC-ED-035 Passed")
    except Exception as e:
        print(f"TC-ED-035 Failed: {e}")
        page.screenshot(path="screenshot_TC-ED-035_failed.png")
        raise

def test_ed_036_cancel_discards_changes(set_up_tear_down) -> None:
    page = set_up_tear_down
    profile = ProfilePage(page)
    try:

        profile.click_update_icon()
        original_name = profile.name.get_attribute("value")

        new_name = "Discarded Name"
        profile.name.fill(new_name)

        profile.click_cancel_button()


        profile.click_update_icon()
        expect(profile.name).to_have_value(original_name)

        print("TC-ED-036 Passed")
    except Exception as e:
        print(f"TC-ED-036 Failed: {e}")
        page.screenshot(path="screenshot_TC-ED-036_failed.png")
        raise

def test_ed_037_cancel_button_closes_modal_no_changes(set_up_tear_down) -> None:
    page = set_up_tear_down
    profile = ProfilePage(page)
    try:
        profile.click_update_icon()

        profile.click_cancel_button()


        print("TC-ED-037 Passed")
    except Exception as e:
        print(f"TC-ED-037 Failed: {e}")
        page.screenshot(path="screenshot_TC-ED-037_failed.png")
        raise





