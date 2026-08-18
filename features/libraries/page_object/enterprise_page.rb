class EnterprisePage
  include ModuleObject::MegaNavigation

  URL = 'https://www.optus.com.au/enterprise'.freeze

  attr_reader :browser

  def initialize(browser)
    @browser = browser
  end

  def open
    browser.goto(URL)
    dismiss_cookie_banner
    wait_until_loaded
    self
  end

  def loaded?
    browser.url.include?('/enterprise') &&
      browser.ready_state == 'complete' &&
      !body_text.match?(/This site can.t be reached|ERR_[A-Z_]+/i)
  end

  private

  def wait_until_loaded
    Watir::Wait.until(timeout: 20) do
      page_text = body_text
      if page_text.match?(/This site can.t be reached|ERR_[A-Z_]+/i)
        raise "Optus Enterprise could not be loaded by the browser: #{page_text.lines.first&.strip}"
      end

      loaded?
    end
  end

  def dismiss_cookie_banner
    accept_button = browser.button(text: /^(accept all|accept all cookies|allow all)$/i)
    accept_button.click if accept_button.present?
  end

  def body_text
    browser.body.text
  end
end
