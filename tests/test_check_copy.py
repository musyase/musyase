import unittest

from scripts.check_copy import lint_text


class CopyCheckTests(unittest.TestCase):
    def test_profile_flags_dashes_emoji_cyrillic_and_stock_copy(self):
        issues = lint_text("# Hi 👋\nA — B\nПривет\nWe leverage powerful tools.", profile=True)
        messages = [message for _, message in issues]
        self.assertTrue(any("emoji" in message for message in messages))
        self.assertTrue(any("long dash" in message for message in messages))
        self.assertTrue(any("English" in message for message in messages))
        self.assertTrue(any("stock phrase" in message for message in messages))

    def test_link_targets_and_code_examples_do_not_trigger_language_rule(self):
        text = "[demo](https://example.com/#пример)\n```\n— Привет 👋\n```\nA concrete sentence."
        self.assertEqual(lint_text(text, profile=True), [])

    def test_russian_project_readme_can_pass_without_profile_mode(self):
        self.assertEqual(lint_text("Локальный инструмент для проверки файлов."), [])


if __name__ == "__main__":
    unittest.main()
