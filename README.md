# Optus Enterprise navigation automation

Ruby/Cucumber automation for the Optus Enterprise mega navigation using Watir
with Selenium WebDriver, a Page Object Model, and a reusable page module.

## Run

```bash
bundle install
bundle exec cucumber
```

The default profile generates Cucumber HTML/JSON and Allure result files. To
generate the finished Allure HTML report as well, run:

```bash
bash scripts/generate_reports.sh
```

Reports are written under `reports/` and are intentionally excluded from Git.

Chrome runs visibly by default because the Optus CDN rejects headless sessions
in some environments. Run with:

```bash
bundle exec cucumber --format pretty
```

To request headless execution, use `HEADLESS=true bundle exec cucumber`.

You can select another supported browser with `BROWSER=edge`, `BROWSER=firefox`,
or `BROWSER=safari`. Safari does not support the `HEADLESS` option and requires
**Allow Remote Automation** to be enabled in Safari's Develop menu.

Each scenario captures a screenshot before the browser closes. Screenshots are
saved in `reports/screenshots` with the scenario status and feature line number.
The navigation scenario keeps one browser tab on the Enterprise page while it
opens all five mega-navigation categories and captures each menu separately.

## Structure

- `features/feature_files` contains the Gherkin feature files.
- `features/step_definitions/enterprise_navigation_steps.rb` maps Gherkin to page behavior.
- `features/libraries` contains reusable test-data loading, UI functions, page objects, and module objects.
- `features/libraries/page_object` contains the Enterprise page objects.
- `features/libraries/module_object` contains reusable form and navigation behavior and selectors.
- `features/test_data` contains YAML test data passed into the scenarios.
- `features/support/configuration/browser_factory.rb` configures Chrome, Edge, Firefox, and Safari.
- `features/support/env.rb` initializes and closes the configured browser for each scenario.
- `Jenkinsfile` defines the GitLab-backed Jenkins Pipeline.
- `docs/GITLAB_JENKINS_SETUP.md` provides the beginner GitLab and Jenkins setup guide.
