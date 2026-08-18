Given('I have loaded the Optus Enterprise contact form') do
  @contact_form_page = EnterpriseContactFormPage.new(@browser).open
  @contact_form = ModuleObject::ModulePage.new(@browser).wait_until_visible
end

When('I submit the Enterprise contact form using the {string} test data') do |data_set|
  details = TestDataLoader.fetch('enterprise_contact_form', data_set)
  @contact_form.submit(details)
end

Then('the Enterprise contact form should be submitted successfully') do
  next if @contact_form.submitted_successfully?

  raise 'Expected the Enterprise contact form to be submitted successfully'
end
