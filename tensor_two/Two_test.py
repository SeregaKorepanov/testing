from BrowserChange import ChangeRegion

def test_two_tensor(browser):
    two_browser = ChangeRegion(browser)
    two_browser.start_site()
    two_browser.click_contact()
    assert two_browser.check_region()
    assert two_browser.check_partners_start()
    two_browser.set_region()
    assert two_browser.check_new_url()
    assert two_browser.check_new_title()
    assert two_browser.check_new_region()
    assert two_browser.check_new_partners()