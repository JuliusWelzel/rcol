# Step 3: Get API Access

This guide explains how to request and configure API access for your REDCap project.

## Prerequisites

- [x] Active REDCap account ([Step 1](account.md))
- [x] Created REDCap project ([Step 2](project.md))

## What is an API Token?

An API token is a unique key that allows programmatic access to your REDCap project. With it, you can:

- Upload instrument definitions
- Import/export data
- Manage project settings

!!! warning "Security Notice"
    Your API token grants full access to your project. **Never share it publicly** or commit it to version control.

## Request API Access

### 1. Navigate to API Settings

1. Log in to REDCap at `https://redcapdev.uol.de`
2. Open your project
3. Go to **Applications** → **API** (in the left sidebar)

### 2. Request API Token

Click the **"Request API token"** button.


### 3. Wait for Approval

- The administrator will review your request
- Approval typically takes **1-2 business days**
- You'll receive an email notification when approved

### 5. Copy Your API Token

Once approved:

1. Return to **Applications** → **API**
2. Your token will be displayed
3. Click **"Copy"** to copy the token

!!! danger "Important"
    Copy and store your token securely. You may not be able to view it again.

## Next: Store Your API Key

In the next step, you will store the API key locally (recommended: a `.env` file using the name `RC_API_KEY`) and upload instruments from `rcol`.

## API Permissions

Your API token may have different permission levels:

| Permission | Description |
|------------|-------------|
| **Import/Update** | Upload data and metadata |
| **Export** | Download data and metadata |
| **Delete** | Remove records |
| **Design** | Modify project structure |

!!! tip "Minimum Required"
    For `rcol`, you need at least **Import/Update** permission to upload instruments.

## What's Next?

Once you have API access, proceed to:

**[→ Step 4: Setup Python](python-setup.md)**

## Troubleshooting

??? question "My API request was denied"
    - Provide more detailed justification
    - Have your supervisor approve the request
    - Contact the REDCap administrator

??? question "I lost my API token"
    - Request a new token from the API page
    - The old token will be revoked

??? question "API calls return 403 Forbidden"
    - Verify your token is correct
    - Check your user rights in REDCap
    - Ensure the project is not in Production mode (or you have production rights)
