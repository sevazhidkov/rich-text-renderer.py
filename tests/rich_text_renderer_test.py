# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from unittest import TestCase
from rich_text_renderer import RichTextRenderer
from rich_text_renderer.base_node_renderer import BaseNodeRenderer


full_document = {
    "content": [
        {
            "data": {},
            "content": [
                {
                    "marks": [],
                    "value": "Some heading",
                    "nodeType": "text",
                    "nodeClass": "text",
                }
            ],
            "nodeType": "heading-1",
            "nodeClass": "block",
        },
        {
            "data": {},
            "content": [
                {"marks": [], "value": "", "nodeType": "text", "nodeClass": "text"}
            ],
            "nodeType": "paragraph",
            "nodeClass": "block",
        },
        {
            "data": {
                "target": {
                    "sys": {
                        "id": "49rofLvvxCOiIMIi6mk8ai",
                        "type": "Link",
                        "linkType": "Entry",
                    }
                }
            },
            "content": [
                {"marks": [], "value": "", "nodeType": "text", "nodeClass": "text"}
            ],
            "nodeType": "embedded-entry-block",
            "nodeClass": "block",
        },
        {
            "data": {},
            "content": [
                {
                    "marks": [],
                    "value": "Some subheading",
                    "nodeType": "text",
                    "nodeClass": "text",
                }
            ],
            "nodeType": "heading-2",
            "nodeClass": "block",
        },
        {
            "data": {},
            "content": [
                {
                    "marks": [{"data": {}, "type": "bold", "object": "mark"}],
                    "value": "Some bold",
                    "nodeType": "text",
                    "nodeClass": "text",
                }
            ],
            "nodeType": "paragraph",
            "nodeClass": "block",
        },
        {
            "data": {},
            "content": [
                {
                    "marks": [{"data": {}, "type": "italic", "object": "mark"}],
                    "value": "Some italics",
                    "nodeType": "text",
                    "nodeClass": "text",
                }
            ],
            "nodeType": "paragraph",
            "nodeClass": "block",
        },
        {
            "data": {},
            "content": [
                {
                    "marks": [{"data": {}, "type": "underline", "object": "mark"}],
                    "value": "Some underline",
                    "nodeType": "text",
                    "nodeClass": "text",
                }
            ],
            "nodeType": "paragraph",
            "nodeClass": "block",
        },
        {
            "data": {},
            "content": [
                {"marks": [], "value": "", "nodeType": "text", "nodeClass": "text"}
            ],
            "nodeType": "paragraph",
            "nodeClass": "block",
        },
        {
            "data": {},
            "content": [
                {"marks": [], "value": "", "nodeType": "text", "nodeClass": "text"}
            ],
            "nodeType": "paragraph",
            "nodeClass": "block",
        },
        {
            "data": {
                "target": {
                    "sys": {
                        "id": "5ZF9Q4K6iWSYIU2OUs0UaQ",
                        "type": "Link",
                        "linkType": "Entry",
                    }
                }
            },
            "content": [
                {"marks": [], "value": "", "nodeType": "text", "nodeClass": "text"}
            ],
            "nodeType": "embedded-entry-block",
            "nodeClass": "block",
        },
        {
            "data": {},
            "content": [
                {"marks": [], "value": "", "nodeType": "text", "nodeClass": "text"}
            ],
            "nodeType": "paragraph",
            "nodeClass": "block",
        },
        {
            "data": {},
            "content": [
                {
                    "marks": [],
                    "value": "Some raw content",
                    "nodeType": "text",
                    "nodeClass": "text",
                }
            ],
            "nodeType": "paragraph",
            "nodeClass": "block",
        },
        {
            "data": {},
            "content": [
                {"marks": [], "value": "", "nodeType": "text", "nodeClass": "text"}
            ],
            "nodeType": "paragraph",
            "nodeClass": "block",
        },
        {
            "data": {},
            "content": [
                {
                    "marks": [],
                    "value": "An unpublished embed:",
                    "nodeType": "text",
                    "nodeClass": "text",
                }
            ],
            "nodeType": "paragraph",
            "nodeClass": "block",
        },
        {
            "data": {},
            "content": [
                {"marks": [], "value": "", "nodeType": "text", "nodeClass": "text"}
            ],
            "nodeType": "paragraph",
            "nodeClass": "block",
        },
        {
            "data": {
                "target": {
                    "sys": {
                        "id": "q2hGXkd5tICym64AcgeKK",
                        "type": "Link",
                        "linkType": "Entry",
                    }
                }
            },
            "content": [
                {"marks": [], "value": "", "nodeType": "text", "nodeClass": "text"}
            ],
            "nodeType": "embedded-entry-block",
            "nodeClass": "block",
        },
        {
            "data": {},
            "content": [
                {
                    "marks": [],
                    "value": "Some more content",
                    "nodeType": "text",
                    "nodeClass": "text",
                }
            ],
            "nodeType": "paragraph",
            "nodeClass": "block",
        },
    ],
    "nodeType": "document",
    "nodeClass": "document",
}

mock_unknown_node = {"content": [], "nodeType": "unknown"}

mock_document_with_unicode = {
    "content": [
        {"content": [{"value": "😇", "nodeType": "text"}], "nodeType": "paragraph"}
    ],
    "nodeType": "document",
}


class HeadingOneMarkdownRenderer(BaseNodeRenderer):
    def render(self, node):
        return "\n".join(
            "# {0}".format(self._find_renderer(c).render(c)) for c in node["content"]
        )


class HeadingTwoMarkdownRenderer(BaseNodeRenderer):
    def render(self, node):
        return "\n".join(
            "## {0}".format(self._find_renderer(c).render(c)) for c in node["content"]
        )


class ParagraphMarkdownRenderer(BaseNodeRenderer):
    def render(self, node):
        return "\n{0}\n".format(
            "\n".join(self._find_renderer(c).render(c) for c in node["content"])
        )


class EntryBlockMarkdownRenderer(BaseNodeRenderer):
    def render(self, node):
        return "\n```\n{0}\n```\n".format(node["data"]["target"])


class BoldMarkdownRenderer(BaseNodeRenderer):
    def render(self, node):
        return "**{0}**".format(node["value"])


class ItalicMarkdownRenderer(BaseNodeRenderer):
    def render(self, node):
        return "*{0}*".format(node["value"])


class UnderlineMarkdownRenderer(BaseNodeRenderer):
    def render(self, node):
        return "__{0}__".format(node["value"])


class RichTextRendererTest(TestCase):
    def test_render_with_defaults(self):
        renderer = RichTextRenderer()

        self.assertEqual(
            renderer.render(full_document),
            "\n".join(
                [
                    "<h1>Some heading</h1>",
                    "<p></p>",
                    "<div>{0}</div>".format(
                        {
                            "sys": {
                                "id": "49rofLvvxCOiIMIi6mk8ai",
                                "type": "Link",
                                "linkType": "Entry",
                            }
                        }
                    ),
                    "<h2>Some subheading</h2>",
                    "<p><b>Some bold</b></p>",
                    "<p><i>Some italics</i></p>",
                    "<p><u>Some underline</u></p>",
                    "<p></p>",
                    "<p></p>",
                    "<div>{0}</div>".format(
                        {
                            "sys": {
                                "id": "5ZF9Q4K6iWSYIU2OUs0UaQ",
                                "type": "Link",
                                "linkType": "Entry",
                            }
                        }
                    ),
                    "<p></p>",
                    "<p>Some raw content</p>",
                    "<p></p>",
                    "<p>An unpublished embed:</p>",
                    "<p></p>",
                    "<div>{0}</div>".format(
                        {
                            "sys": {
                                "id": "q2hGXkd5tICym64AcgeKK",
                                "type": "Link",
                                "linkType": "Entry",
                            }
                        }
                    ),
                    "<p>Some more content</p>",
                ]
            ),
        )

    def test_null_renderer_will_raise_an_error_if_unknown_node_type_is_not_mapped(self):
        renderer = RichTextRenderer()

        with self.assertRaises(Exception):
            renderer.render(mock_unknown_node)

    def test_render_with_emojis(self):
        renderer = RichTextRenderer()

        self.assertEqual(
            renderer.render(mock_document_with_unicode), "\n".join(["<p>😇</p>"])
        )

    def test_render_with_all_renderers_overridden_for_markdown(self):
        self.maxDiff = None
        renderer = RichTextRenderer(
            {
                "heading-1": HeadingOneMarkdownRenderer,
                "heading-2": HeadingTwoMarkdownRenderer,
                "paragraph": ParagraphMarkdownRenderer,
                "embedded-entry-block": EntryBlockMarkdownRenderer,
                "bold": BoldMarkdownRenderer,
                "italic": ItalicMarkdownRenderer,
                "underline": UnderlineMarkdownRenderer,
            }
        )

        self.assertEqual(
            renderer.render(full_document),
            "\n".join(
                [
                    "# Some heading",
                    "",
                    "",
                    "",
                    "",
                    "```",
                    "{0}".format(
                        {
                            "sys": {
                                "id": "49rofLvvxCOiIMIi6mk8ai",
                                "type": "Link",
                                "linkType": "Entry",
                            }
                        }
                    ),
                    "```",
                    "",
                    "## Some subheading",
                    "",
                    "**Some bold**",
                    "",
                    "",
                    "*Some italics*",
                    "",
                    "",
                    "__Some underline__",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "```",
                    "{0}".format(
                        {
                            "sys": {
                                "id": "5ZF9Q4K6iWSYIU2OUs0UaQ",
                                "type": "Link",
                                "linkType": "Entry",
                            }
                        }
                    ),
                    "```",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "Some raw content",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "An unpublished embed:",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "```",
                    "{0}".format(
                        {
                            "sys": {
                                "id": "q2hGXkd5tICym64AcgeKK",
                                "type": "Link",
                                "linkType": "Entry",
                            }
                        }
                    ),
                    "```",
                    "",
                    "",
                    "Some more content",
                    "",
                ]
            ),
        )
