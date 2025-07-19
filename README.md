# Jira to PR Automation

This project automates the process of generating code based on Jira ticket descriptions and integrating it into a Bitbucket repository via automated branch creation, code commitment, and pull request generation.

## Features

- **Jira Integration**: Fetches ticket details (title and description) directly from Jira.
- **AI Code Generation**: Utilizes OpenAI's GPT-4 to generate Python code based on the Jira ticket's requirements.
- **Bitbucket Automation**:
    - Creates new feature branches for each Jira ticket.
    - Commits the AI-generated code to the new branch.
    - Creates a pull request to merge the new code into the main branch (e.g., `master`).
- **Secure Credential Handling**: Uses environment variables to manage API keys and sensitive information.

## How it Works

The `main.py` script orchestrates the entire workflow:

1.  **Fetch Jira Details**: It calls `jira_reader.py` to retrieve the title and description of a specified Jira ticket.
2.  **Generate Code**: The `ai_code_gen.py` module then uses these details to prompt OpenAI's GPT-4 model to generate relevant Python code.
3.  **Bitbucket Operations**: Finally, `bitbucket_automation.py` handles the version control aspects by:
    *   Creating a new branch (e.g., `feature/JIRA-XXXX_ticket_title`).
    *   Committing the generated code to this new branch.
    *   Creating a pull request from the new branch to the `master` branch.

## Setup and Installation

### Prerequisites

*   Python 3.x
*   Access to Jira API
*   Access to Bitbucket API
*   OpenAI API Key

### Environment Variables

Create a `.env` file in the root directory of the project and populate it with your credentials:

```
JIRA_DOMAIN=your-jira-domain.atlassian.net
JIRA_EMAIL=your-jira-email@example.com
JIRA_API_TOKEN=your-jira-api-token

BITBUCKET_USERNAME=your-bitbucket-username
BITBUCKET_APP_PASSWORD=your-bitbucket-app-password
BITBUCKET_WORKSPACE_ID=your-bitbucket-workspace-id
BITBUCKET_REPO_SLUG=your-bitbucket-repository-slug

OPENAI_API_KEY=your-openai-api-key
```

### Installation

1.  Clone the repository:
    ```bash
    git clone https://your-repository-url.git
    cd jira-to-pr
    ```
2.  Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the automation, execute the `main.py` script. You will need to provide the Jira ID, title, and description.

```python
# Example usage in main.py
from main import automate_code_flow

automate_code_flow(
    jira_id="JIRA-1234",
    title="Add Login API",
    description="Create a secure login REST API endpoint that takes username and password and returns JWT."
)
```

Modify the `automate_code_flow` call in `main.py` with your desired Jira ticket details.

## Project Structure

```
.
├── .env                  # Environment variables for API keys
├── ai_code_gen.py        # Handles AI code generation via OpenAI
├── bitbucket_automation.py # Manages Bitbucket API interactions
├── jira_reader.py        # Fetches Jira ticket details
├── main.py               # Orchestrates the automation workflow
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies
