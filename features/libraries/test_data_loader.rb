require 'yaml'

module TestDataLoader
  TEST_DATA_DIRECTORY = File.expand_path('../test_data', __dir__).freeze
  SAFE_NAME = /\A[a-z0-9_]+\z/.freeze

  module_function

  def fetch(file_name, data_set)
    validate_name!(file_name, 'file')
    validate_name!(data_set, 'data set')

    path = File.join(TEST_DATA_DIRECTORY, "#{file_name}.yml")
    data = YAML.safe_load_file(path, aliases: false)
    data.fetch(data_set)
  rescue Errno::ENOENT
    raise ArgumentError, "Test data file was not found: #{path}"
  rescue KeyError
    raise ArgumentError, "Test data set '#{data_set}' was not found in #{path}"
  end

  def validate_name!(name, type)
    return if name.match?(SAFE_NAME)

    raise ArgumentError, "Invalid test data #{type}: #{name}"
  end
  private_class_method :validate_name!
end
