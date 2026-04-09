---
concept: Action on Cosets
slug: action-on-cosets
category: group-structure
subcategory: group-actions
tier: advanced
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Group Actions"
chapter_number: 14
pdf_page: 182
section: "Groups Acting on Sets"
extraction_confidence: high
aliases:
  - "left multiplication on cosets"
prerequisites:
  - group-action
  - coset
extends:
  - group-action
related:
  - orbit
  - stabilizer-subgroup
contrasts_with: []
answers_questions:
  - "How does a group act on the cosets of a subgroup?"
---

# Quick Definition

If $H$ is a subgroup of $G$, then $G$ acts on the set of left cosets $L_H = \{gH : g \in G\}$ by left multiplication: $(g, xH) \mapsto gxH$. This action is always transitive (single orbit).

# Core Definition

"Let $H$ be a subgroup of $G$ and $L_H$ the set of left cosets of $H$. The set $L_H$ is a $G$-set under the action $(g, xH) \mapsto gxH$" (Judson, p. 182, Example 14.5).

# Prerequisites

- **Group action** — This is a specific action
- **Coset** — The set being acted upon

# Key Properties

1. The action is well-defined: if $xH = yH$, then $gxH = gyH$
2. The action is transitive: for any $xH, yH$, take $g = yx^{-1}$
3. The stabilizer of $eH = H$ is $H$ itself

# Relationships

## Builds Upon
- **Group action** — A specific instance

## Enables
- **Cayley-type results** — $G$ embeds into $S_{[G:H]}$

# Source Reference

Chapter 14: Group Actions, Section 14.1, p. 182. Example 14.5.

# Verification Notes

- Definition source: Example 14.5
- Confidence: HIGH
