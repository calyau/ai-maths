---
concept: Refinement of a Series
slug: refinement-of-series
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
extends: []
related:
  - composition-series
  - jordan-holder-theorem
contrasts_with: []
answers_questions:
  - "What is a refinement of a subnormal series?"
---

# Quick Definition

A subnormal (normal) series $\{K_j\}$ is a refinement of a series $\{H_i\}$ if $\{H_i\} \subset \{K_j\}$, meaning every term of the original series appears in the refinement.

# Core Definition

"A subnormal (normal) series $\{K_j\}$ is a **refinement of a subnormal (normal) series** $\{H_i\}$ if $\{H_i\} \subset \{K_j\}$. That is, each $H_i$ is one of the $K_j$" (Judson, p. 176).

# Prerequisites

- **Subnormal series** — Refinements apply to subnormal (or normal) series

# Key Properties

1. Every term of the original series appears in the refinement
2. A refinement inserts additional subgroups between existing ones
3. Any two subnormal series have isomorphic refinements (Schreier's Theorem)

# Examples

**Example 1** (p. 176): $\mathbb{Z} \supset 3\mathbb{Z} \supset 9\mathbb{Z} \supset 45\mathbb{Z} \supset 90\mathbb{Z} \supset 180\mathbb{Z} \supset \{0\}$ refines $\mathbb{Z} \supset 9\mathbb{Z} \supset 45\mathbb{Z} \supset 180\mathbb{Z} \supset \{0\}$.

# Relationships

## Builds Upon
- **Subnormal series** — Refinements modify these series

## Enables
- **Jordan-Holder theorem** — Uses refinements in the proof

# Source Reference

Chapter 13: The Structure of Groups, Section 13.2, p. 176.

# Verification Notes

- Definition source: Direct from p. 176
- Confidence: HIGH
