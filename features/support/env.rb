require 'cucumber'
require 'fileutils'
require 'selenium-webdriver'
require 'watir'

# Let Selenium Manager use the driver version matching the installed browser
# instead of an older chromedriver that may be present in the system PATH.
ENV['SE_SKIP_DRIVER_IN_PATH'] = 'true'

require_relative 'configuration/browser_factory'
require_relative 'configuration/reporting'
require_relative '../libraries/test_data_loader'
require_relative '../libraries/module_object/mega_navigation'
require_relative '../libraries/module_object/module_page'
require_relative '../libraries/page_object/enterprise_page'
require_relative '../libraries/page_object/enterprise_contact_form_page'

Watir.logger.level = :warn
Selenium::WebDriver.logger.level = :warn

Before do
  @browser = BrowserFactory.build
  @enterprise_page = EnterprisePage.new(@browser)
end

After do |scenario|
  if @browser
    screenshot_directory = File.expand_path('../../reports/screenshots', __dir__)
    FileUtils.mkdir_p(screenshot_directory)

    status = scenario.failed? ? 'failed' : 'passed'
    scenario_name = scenario.name.downcase.gsub(/[^a-z0-9]+/, '_').gsub(/^_|_$/, '')
    screenshot_name = "#{status}_#{scenario_name}_line_#{scenario.location.line}.png"
    screenshot_path = File.join(screenshot_directory, screenshot_name)

    @browser.screenshot.save(screenshot_path)
    Allure.add_attachment(
      name: "#{scenario.name} screenshot",
      source: File.new(screenshot_path),
      type: Allure::ContentType::PNG
    )
    puts "Screenshot: #{screenshot_path}"
  end
ensure
  @browser&.close
end
