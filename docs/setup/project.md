# Step 2: Create a New Project

This guide explains how to create a new REDCap project.

## Prerequisites

- [x] Active REDCap account ([Step 1](account.md))
- [x] Clear project name and description prepared

## Create the Project (Self-Service)

### 1. Log in to REDCap

Navigate to `https://redcapdev.uol.de` and log in.

### 2. Create New Project

1. Click **"New Project"** on your dashboard
2. Fill in the project details:

```
Project Title: Cognitive Assessment Study 2026
Purpose: Research
Project Notes: Data collection for stroke rehabilitation study
```

### 3. Select Project Template

Choose a starting point:

- **Empty project** - Start from scratch
- **Template** - Use a pre-built template
- **Copy existing** - Duplicate another project

!!! tip "Recommendation"
    For `rcol` projects, start with an **empty project** since you'll upload instruments via the API.

### 4. Confirm Creation

Click **"Create Project"** to finalize.

## Project Settings Checklist

After your project is created, verify these settings:

- [ ] Project title is correct
- [ ] Purpose is set appropriately
- [ ] Project is in **Development** mode (not Production)
- [ ] You have appropriate user rights

## What's Next?

Once your project is created, proceed to:

**[→ Step 3: Get API Access](api-key.md)**

## Troubleshooting

??? question "I don't see the 'New Project' button"
    - Your institution may require admin approval for new projects
    - Contact your REDCap administrator

??? question "I need to modify my project after creation"
    - Most settings can be changed in **Project Setup**
    - Some changes require administrator assistance
