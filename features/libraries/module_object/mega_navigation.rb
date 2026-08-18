module ModuleObject
  module MegaNavigation
    MENU_ITEMS = %w[Industries Solutions Services Satellite Resources].freeze
    EXPECTED_MENU_CONTENT = {
      'Industries' => ['Construction', 'Government']
    }.freeze
    WAIT_TIME = 15

    def open_mega_navigation(menu_item)
      validate_menu_item!(menu_item)

      trigger = mega_navigation_trigger(menu_item)
      trigger.scroll.to(:center)
      trigger.click
      @last_opened_menu_item = menu_item
    end

    def mega_navigation_visible?(menu_item)
      validate_menu_item!(menu_item)
      return false unless @last_opened_menu_item == menu_item

      Watir::Wait.until(timeout: WAIT_TIME) do
        panel = mega_navigation_panel
        panel.present? &&
          panel.links.any?(&:present?) &&
          expected_menu_content_visible?(panel, menu_item)
      end
    rescue Watir::Wait::TimeoutError
      false
    end

    private

    def mega_navigation_trigger(menu_item)
      text = /^\s*#{Regexp.escape(menu_item)}\s*$/i
      candidates = [
        browser.button(aria_label: text),
        browser.button(text: text),
        browser.link(aria_label: text),
        browser.link(text: text),
        browser.element(xpath: header_navigation_xpath(menu_item)),
        browser.element(xpath: role_navigation_xpath(menu_item))
      ]

      Watir::Wait.until(timeout: WAIT_TIME) do
        candidates.any? { |candidate| candidate.exists? && candidate.present? }
      end

      candidates.find { |candidate| candidate.exists? && candidate.present? }
    end

    def header_navigation_xpath(menu_item)
      "//header//*[self::a or self::button or @role='button' or @aria-expanded]" \
        "[normalize-space(.)='#{menu_item}' or @aria-label='#{menu_item}']"
    end

    def role_navigation_xpath(menu_item)
      "//*[@role='navigation']//*[normalize-space(.)='#{menu_item}' or @aria-label='#{menu_item}']"
    end

    def mega_navigation_panel
      browser.nav(css: 'nav.header__level-3')
    end

    def expected_menu_content_visible?(panel, menu_item)
      expected_labels = EXPECTED_MENU_CONTENT.fetch(menu_item, [])
      expected_labels.all? { |label| panel.text.include?(label) }
    end

    def validate_menu_item!(menu_item)
      return if MENU_ITEMS.include?(menu_item)

      raise ArgumentError,
            "Unknown mega-navigation item '#{menu_item}'. Expected one of: #{MENU_ITEMS.join(', ')}"
    end
  end
end
