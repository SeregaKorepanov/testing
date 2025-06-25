from BrowserInteraction import Navigation

def test_one_tensor(browser):
    one_browser = Navigation(browser)
    one_browser.start_site()
    one_browser.click_contact()
    one_browser.click_banner()
    assert one_browser.check_banner()
    one_browser.get_tensor()
    assert one_browser.check_title()
    assert one_browser.check_image()
