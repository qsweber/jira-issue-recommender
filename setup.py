from setuptools import find_packages, setup

setup(
    name='jira-issue-recommender',
    version='0.0.1',
    description='Find related issues',
    author='Quinn Weber',
    maintainer='Quinn Weber',
    maintainer_email='quinn@quinnweber.com',
    url='',
    packages=find_packages(exclude=('tests',)),
    install_requires=(
        'jira',
        'HTMLParser',
        'scikit-learn',
    ),
    entry_points={
        'console_scripts': (
            'jira-issue-recommender = jira_issue_recommender.main:main'
        )
    }
)
