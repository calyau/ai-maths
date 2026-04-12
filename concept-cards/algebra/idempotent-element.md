---
concept: Idempotent Element
slug: idempotent-element
category: ring-theory
subcategory: basic-structures
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Rings"
chapter_number: 11
pdf_page: 339
section: "Product Rings"
extraction_confidence: high
aliases: []
prerequisites:
  - ring
extends: []
related:
  - product-ring
contrasts_with: []
answers_questions:
  - "What is an idempotent element?"
---

# Quick Definition

An idempotent element e of a ring S is one satisfying e^2 = e. If e is idempotent, so is e' = 1 - e, and S is isomorphic to the product ring eS x e'S.

# Core Definition

An idempotent element e of a ring S is an element such that e^2 = e (Artin, p. 359). The element e' = 1 - e is also idempotent, e + e' = 1, and ee' = 0. The ring S is isomorphic to the product ring eS x e'S (Proposition 11.6.2).

# Prerequisites

- **Ring** -- Idempotents are elements of a ring

# Key Properties

1. e^2 = e
2. e' = 1 - e is also idempotent
3. ee' = 0 and e + e' = 1
4. S ~ eS x e'S

# Examples

**Example 1** (p. 359): In F_11[delta]/(delta^2 - 3), the elements e = delta - 5 and e' = -delta - 5 are idempotents, giving R' ~ F_11 x F_11.

# Relationships

## Builds Upon
- **Ring** -- Defined in any ring

## Enables
- **Product ring** -- Idempotents detect product decompositions

# Source Reference

Chapter 11: Rings, Section 11.6, Proposition 11.6.2, page 359.

# Verification Notes

- Definition source: Direct from text and Proposition 11.6.2
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
