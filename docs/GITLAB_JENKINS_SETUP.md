# GitLab and Jenkins setup

This guide takes the project from a local VS Code folder to a GitLab repository
and then runs it from a Jenkins Pipeline.

## 1. Run and generate reports locally

Install the Ruby dependencies:

```bash
PATH="/opt/homebrew/opt/ruby/bin:/opt/homebrew/lib/ruby/gems/3.4.0/bin:$PATH" bundle install
```

Run the tests and generate both report types:

```bash
bash scripts/generate_reports.sh
```

Generated output:

- `reports/cucumber/cucumber.html`
- `reports/cucumber/cucumber.json`
- `reports/allure-results/`
- `reports/allure-report/index.html`

Open the reports on macOS:

```bash
open reports/cucumber/cucumber.html
JAVA_HOME=/opt/homebrew/opt/openjdk/libexec/openjdk.jdk/Contents/Home \
  allure open reports/allure-report
```

## 2. Create a GitLab project

1. Sign in to GitLab.
2. Select **New project**.
3. Select **Create blank project**.
4. Enter a project name, such as `bdd-framework-at`.
5. Do not initialize it with a README because this local folder already has one.
6. Select **Create project**.
7. Copy the SSH repository URL shown by GitLab.

## 3. Configure SSH access to GitLab

Create an SSH key if you do not already have one:

```bash
ssh-keygen -t ed25519 -C "your-email@example.com"
```

Press Enter to accept the suggested file location. Copy the public key:

```bash
pbcopy < ~/.ssh/id_ed25519.pub
```

In GitLab, open **Edit profile → Access → SSH keys**, paste the key, and save
it. Test the connection:

```bash
ssh -T git@gitlab.com
```

## 4. Commit and push the local repository

From the project folder in the VS Code terminal:

```bash
git status
git add .
git status
git commit -m "Set up Ruby Cucumber automation framework"
git remote add origin git@gitlab.com:YOUR_USERNAME/bdd-framework-at.git
git push --set-upstream origin main
```

Replace `YOUR_USERNAME` and the project path with the values from GitLab.

If Git asks for your identity, configure it once:

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

The project is already initialized locally with Git on the `main` branch. Do
not run `git init` again unless you create a fresh copy without its `.git`
directory.

## 5. Install Jenkins on macOS

Jenkins requires Java. With Homebrew:

```bash
brew install openjdk jenkins-lts
brew services start jenkins-lts
```

Open `http://localhost:8080` and complete the setup wizard.

Install these Jenkins plugins from **Manage Jenkins → Plugins**:

- Pipeline
- Git
- HTML Publisher
- Allure
- GitLab

Configure Allure from **Manage Jenkins → Tools → Allure Commandline
installations**. Add an installation named `allure` and choose automatic
installation.

## 6. Give Jenkins access to GitLab

For a private GitLab project:

1. In Jenkins, open **Manage Jenkins → Credentials**.
2. Add an **SSH Username with private key** credential.
3. Set the username to `git`.
4. Paste the private key that matches an SSH public key registered in GitLab.
5. Give the credential an ID such as `gitlab-ssh`.

Never commit private keys or access tokens to this repository.

## 7. Create the Jenkins job

1. From the Jenkins dashboard select **New Item**.
2. Enter `bdd-framework-at`.
3. Select **Pipeline**, then **OK**.
4. Under **Pipeline**, select **Pipeline script from SCM**.
5. Select **Git** as SCM.
6. Enter the GitLab repository URL.
7. Select the `gitlab-ssh` credential for a private repository.
8. Set **Branch Specifier** to `*/main`.
9. Set **Script Path** to `Jenkinsfile`.
10. Save, then select **Build with Parameters**.
11. Choose a browser and start the build.

After the build, Jenkins displays links to **Cucumber Report** and **Allure
Report**. It also archives the raw reports and screenshots.

## 8. Trigger Jenkins after a GitLab push

First make sure GitLab can reach the Jenkins URL. GitLab.com cannot call a
Jenkins server available only at `localhost`.

For an internet-accessible Jenkins instance:

1. Enable the GitLab trigger in the Jenkins job configuration.
2. Copy the generated Jenkins webhook URL and secret token.
3. In GitLab, open **Settings → Webhooks**.
4. Paste the Jenkins webhook URL and secret.
5. Enable **Push events**.
6. Add and test the webhook.

For a local learning installation, use **Build Now** until Jenkins has a secure,
reachable URL.
