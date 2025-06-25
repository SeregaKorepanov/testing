from BrowserDownload import Loading

def test_one_tensor(browser):
    three_browser = Loading(browser)
    three_browser.start_site()
    three_browser.click_local_load()
    three_browser.click_desktop()
    three_browser.loading_file()
    assert three_browser.check_file()
    assert three_browser.check_size_file()