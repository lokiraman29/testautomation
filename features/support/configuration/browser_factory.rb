module BrowserFactory
  module_function

  def build
    browser_name = ENV.fetch('BROWSER', 'chrome').downcase.to_sym
    headless = ENV.fetch('HEADLESS', 'false').casecmp('true').zero?

    case browser_name
    when :chrome
      options = Selenium::WebDriver::Chrome::Options.new
      add_chromium_options(options, headless)
      Watir::Browser.new(:chrome, options: options)
    when :edge
      options = Selenium::WebDriver::Edge::Options.new
      add_chromium_options(options, headless)
      Watir::Browser.new(:edge, options: options)
    when :firefox
      options = Selenium::WebDriver::Firefox::Options.new
      options.add_argument('-headless') if headless
      Watir::Browser.new(:firefox, options: options)
    when :safari
      raise ArgumentError, 'Safari does not support HEADLESS=true.' if headless

      Watir::Browser.new(:safari)
    else
      raise ArgumentError,
            "Unsupported BROWSER '#{browser_name}'. Use chrome, edge, firefox, or safari."
    end
  end

  def add_chromium_options(options, headless)
    options.add_argument('--window-size=1440,1000')
    options.add_argument('--headless=new') if headless
  end
  private_class_method :add_chromium_options
end
