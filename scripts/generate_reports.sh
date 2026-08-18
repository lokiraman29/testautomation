#!/usr/bin/env bash

set -u

project_directory="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$project_directory" || exit 1

export PATH="/opt/homebrew/opt/ruby/bin:/opt/homebrew/lib/ruby/gems/3.4.0/bin:/opt/homebrew/opt/openjdk/bin:/opt/homebrew/bin:$PATH"
export JAVA_HOME="${JAVA_HOME:-/opt/homebrew/opt/openjdk/libexec/openjdk.jdk/Contents/Home}"

bundle exec cucumber --profile reports
test_status=$?

if command -v allure >/dev/null 2>&1; then
  allure generate reports/allure-results --clean --output reports/allure-report
else
  echo "Allure CLI was not found. Raw results remain in reports/allure-results."
fi

echo "Cucumber HTML: reports/cucumber/cucumber.html"
echo "Cucumber JSON: reports/cucumber/cucumber.json"
echo "Allure HTML: reports/allure-report/index.html"

exit "$test_status"
