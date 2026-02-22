#!/usr/bin/env python3
"""Generates README.md as a table of contents for all recipe markdown files."""

import os
import re

REPO_ROOT = os.path.join(os.path.dirname(__file__), "..")
README_PATH = os.path.join(REPO_ROOT, "README.md")


def slug_to_title(slug: str) -> str:
    """Convert a hyphenated filename slug to a human-readable title."""
    name = slug.replace("-", " ")
    # Title-case but keep short words lowercase unless they're first
    minor_words = {"a", "an", "the", "and", "but", "or", "for", "nor",
                   "on", "at", "to", "by", "in", "of", "up", "as", "with"}
    words = name.split()
    titled = []
    for i, word in enumerate(words):
        if i == 0 or word not in minor_words:
            titled.append(word.capitalize())
        else:
            titled.append(word)
    return " ".join(titled)


def get_recipes():
    """Return sorted list of (title, filename) tuples for all recipes."""
    recipes = []
    for entry in sorted(os.listdir(REPO_ROOT)):
        if not entry.endswith(".md"):
            continue
        if entry.lower() == "readme.md":
            continue
        slug = entry[:-3]  # strip .md
        title = slug_to_title(slug)
        recipes.append((title, entry))
    return recipes


def generate_readme(recipes):
    lines = [
        "# Recipe Index\n",
        "A collection of recipes. Click any title to open the full recipe.\n",
        f"*{len(recipes)} recipes total.*\n",
        "\n",
        "| Recipe |\n",
        "| --- |\n",
    ]
    for title, filename in recipes:
        lines.append(f"| [{title}]({filename}) |\n")
    return "".join(lines)


def main():
    recipes = get_recipes()
    content = generate_readme(recipes)
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"README.md updated with {len(recipes)} recipes.")


if __name__ == "__main__":
    main()
