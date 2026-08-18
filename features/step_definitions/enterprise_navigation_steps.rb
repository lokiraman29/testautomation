Given('I am on the Optus Enterprise page') do
  @enterprise_page.open
end

When('I open the Enterprise mega-navigation categories from the {string} test data') do |data_set|
  menu_items = TestDataLoader.fetch('enterprise_mega_navigation', data_set)
  @mega_navigation_results = menu_items.to_h do |menu_item|
    @enterprise_page.open_mega_navigation(menu_item)
    visible = @enterprise_page.mega_navigation_visible?(menu_item)
    capture_mega_navigation(menu_item)

    [menu_item, visible]
  end
end

Then('every requested mega-navigation panel should be visible') do
  hidden_menus = @mega_navigation_results.reject { |_menu_item, visible| visible }.keys
  next if hidden_menus.empty?

  raise "Expected these mega-navigation panels to be visible: #{hidden_menus.join(', ')}"
end

def capture_mega_navigation(menu_item)
  screenshot_directory = File.expand_path('../../reports/screenshots', __dir__)
  FileUtils.mkdir_p(screenshot_directory)
  screenshot_path = File.join(
    screenshot_directory,
    "mega_navigation_#{menu_item.downcase.gsub(/[^a-z0-9]+/, '_')}.png"
  )

  @browser.screenshot.save(screenshot_path)
  puts "Screenshot: #{screenshot_path}"
end
