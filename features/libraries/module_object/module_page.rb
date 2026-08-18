module ModuleObject
  class ModulePage
    FORM_ID = 'mktoForm_2858'.freeze
    FIELD_IDS = {
      'first_name' => 'FirstName',
      'last_name' => 'LastName',
      'work_email' => 'Email',
      'contact_number' => 'MobilePhone',
      'company_name' => 'Company',
      'job_title' => 'Title'
    }.freeze
    SUCCESS_TEXT = /thank you|thanks for (?:contacting|getting in touch)|we(?:'|’)ll be in touch|request has been (?:sent|submitted|received)/i

    attr_reader :browser

    def initialize(browser)
      @browser = browser
    end

    def wait_until_visible
      contact_form.scroll.to(:center)
      Watir::Wait.until(timeout: 20) { contact_form.present? }
      self
    end

    def submit(details)
      validate_details!(details)

      FIELD_IDS.each do |field_name, field_id|
        contact_form.text_field(id: field_id).set(details.fetch(field_name))
      end

      @url_before_submission = browser.url
      contact_form.button(type: 'submit').click
    end

    def submitted_successfully?
      Watir::Wait.until(timeout: 30) do
        raise validation_error_message unless validation_errors.empty?

        success_message_visible? ||
          browser.url != @url_before_submission ||
          !contact_form.present?
      end
    rescue Watir::Wait::TimeoutError
      false
    end

    private

    def contact_form
      browser.form(id: FORM_ID)
    end

    def success_message_visible?
      browser.body.text.match?(SUCCESS_TEXT)
    end

    def validation_errors
      browser.elements(css: '.mktoErrorMsg, [role="alert"], .error-message')
             .select(&:present?)
             .map(&:text)
             .reject(&:empty?)
    end

    def validation_error_message
      "Contact form validation failed: #{validation_errors.join('; ')}"
    end

    def validate_details!(details)
      missing_fields = FIELD_IDS.keys - details.keys
      return if missing_fields.empty?

      raise ArgumentError, "Missing contact form values: #{missing_fields.join(', ')}"
    end
  end
end
