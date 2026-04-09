---
concept: Isomorphic Series
slug: isomorphic-series
category: group-structure
subcategory: series-of-subgroups
tier: advanced
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "The Structure of Groups"
chapter_number: 13
pdf_page: 176
section: "Solvable Groups"
extraction_confidence: high
aliases: []
prerequisites:
  - subnormal-series
  - factor-group
extends: []
related:
  - jordan-holder-theorem
  - composition-series
contrasts_with: []
answers_questions:
  - "When are two subnormal series isomorphic?"
---

# Quick Definition

Two subnormal (normal) series $\{H_i\}$ and $\{K_j\}$ of a group $G$ are isomorphic if there is a one-to-one correspondence between their factor groups $\{H_{i+1}/H_i\}$ and $\{K_{j+1}/K_j\}$ such that corresponding factor groups are isomorphic.

# Core Definition

"We say that two subnormal (normal) series $\{H_i\}$ and $\{K_j\}$ of a group $G$ are **isomorphic** if there is a one-to-one correspondence between the collections of factor groups $\{H_{i+1}/H_i\}$ and $\{K_{j+1}/K_j\}$" (Judson, p. 176).

# Prerequisites

- **Subnormal series** — The series being compared
- **Factor group** — Isomorphism is between factor groups

# Key Properties

1. The factor groups are the same (up to isomorphism and reordering)
2. Isomorphic series have the same length
3. The Jordan-Holder Theorem: any two composition series are isomorphic

# Examples

**Example 1** (p. 176): The normal series $\mathbb{Z}_{60} \supset \langle 3 \rangle \supset \langle 15 \rangle \supset \{0\}$ and $\mathbb{Z}_{60} \supset \langle 4 \rangle \supset \langle 20 \rangle \supset \{0\}$ are isomorphic with factors $\mathbb{Z}_3, \mathbb{Z}_5, \mathbb{Z}_4$ (in different orders).

# Relationships

## Enables
- **Jordan-Holder theorem** — Composition series are always isomorphic

# Source Reference

Chapter 13: The Structure of Groups, Section 13.2, p. 176.

# Verification Notes

- Definition source: Direct from p. 176
- Confidence: HIGH
