require 'allure-cucumber'
require 'fileutils'
require 'rbconfig'

REPORTS_DIRECTORY = File.expand_path('../../../reports', __dir__).freeze
CUCUMBER_REPORT_DIRECTORY = File.join(REPORTS_DIRECTORY, 'cucumber').freeze

FileUtils.mkdir_p(CUCUMBER_REPORT_DIRECTORY)

AllureCucumber.configure do |config|
  config.results_directory = File.join(REPORTS_DIRECTORY, 'allure-results')
  config.clean_results_directory = true
  config.environment_properties = {
    browser: ENV.fetch('BROWSER', 'chrome'),
    headless: ENV.fetch('HEADLESS', 'false'),
    operating_system: RbConfig::CONFIG['host_os'],
    ruby_version: RUBY_VERSION
  }
end
