from unittest import TestCase

from jira_issue_recommender.util import get_comment


class GetCommentTest(TestCase):
    def test_get_comment(self):
        expected = 'test preface\nABC-1 abc 1 title - 1.0 hours\nABC-2 abc 2 title - 2.0 hours'
        actual = get_comment('test preface', [
            ('ABC-1', {'title': 'abc 1 title', 'timespent': 3600}),
            ('ABC-2', {'title': 'abc 2 title', 'timespent': 7200}),
        ])

        self.assertEqual(expected, actual)
