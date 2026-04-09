---
concept: Haven
slug: haven
category: graph-minors
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Minors, Trees and WQO"
chapter_number: 12
pdf_page: 332
section: "12.3 Tree-decompositions"
extraction_confidence: high
aliases: []
prerequisites: []
extends: []
related: []
contrasts_with: []
answers_questions:
  - "What is Haven?"
---

# Quick Definition
A haven of order k in G assigns to each set S of < k vertices a component of G - S, such that the chosen component for S contains the chosen component for any larger S' containing S.

# Core Definition
A *haven* of order k in G is a function beta that assigns to each set S of fewer than k vertices a component of G - S, such that if S subset S' then beta(S') subset beta(S). Havens of order k exist iff brambles of order k exist (Diestel, notes).

# Source Reference
Chapter 12, Section 12.3 Tree-decompositions, page 332.

# Verification Notes
- Extracted from source
- Confidence: HIGH
