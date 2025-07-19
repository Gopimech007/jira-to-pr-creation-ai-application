from ai_code_gen import generate_code_from_jira
from bitbucket_automation import create_branch, commit_code, create_pull_request

def automate_code_flow(jira_id, title, description):
    branch = f"feature/{jira_id.lower().replace('-', '_')}"
    filename = f"{jira_id.lower().replace('-', '_')}.py"

    print(f"🔍 Jira Ticket: {jira_id} - {title}")
    print("🧠 Generating code...")
    code = generate_code_from_jira(title, description)

    print("🌿 Creating branch...")
    if create_branch(branch):
        print("✅ Branch created.")

    print("📦 Committing code...")
    if commit_code(branch, filename, code):
        print("✅ Code committed.")

    print("🚀 Creating Pull Request...")
    pr = create_pull_request(branch, f"[{jira_id}] {title}")
    print("🔗 PR Link:", pr['links']['html']['href'])

# Test run
automate_code_flow(
    jira_id="JIRA-1234",
    title="Add Login API",
    description="Create a secure login REST API endpoint that takes username and password and returns JWT."
)