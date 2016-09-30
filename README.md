# JIRA Issue Recommender

Adds a comment to new tickets with links to related tickets.

## Installation

    pip3 install jira_issue_recommender

## Usage

    jira-issue-recommender \
        --jira-server-url 'https://jira.example.com/' \
        --username quinn \
        --password **** \
        --finished-issues-query 'status = Done and timespent > 0' \
        --new-issues-query 'status = "To Do" and timeestimate is null' \
        --comment-preface 'Consider looking at:'
