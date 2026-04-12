---
concept: Product Ring
slug: product-ring
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
aliases:
  - "direct product of rings"
prerequisites:
  - ring
extends:
  - ring
related:
  - idempotent-element
  - chinese-remainder-theorem
contrasts_with: []
answers_questions:
  - "What is a product ring?"
---

# Quick Definition

The product ring R x R' has componentwise addition and multiplication: (x,x') + (y,y') = (x+y, x'+y') and (x,x')(y,y') = (xy, x'y'). Its identity is (1,1).

# Core Definition

Let R and R' be rings. The product set R x R' is a ring called the product ring, with componentwise operations (Artin, Proposition 11.6.1, p. 358). The projections pi: R x R' -> R and pi': R x R' -> R' are ring homomorphisms. The elements (1,0) and (0,1) are idempotents.

# Prerequisites

- **Ring** -- Components are rings

# Key Properties

1. Componentwise addition and multiplication
2. Identity is (1,1), zero is (0,0)
3. Projections are ring homomorphisms
4. The product ring is never an integral domain (when both factors are nonzero)
5. A ring S with an idempotent e is isomorphic to eS x (1-e)S

# Examples

**Example 1** (p. 359): Adjoining an abstract square root of 3 to F_11 gives F_11 x F_11, since F_11 already contains square roots of 3.

**Example 2** (p. 359): C[x,y]/(xy) is isomorphic to a subring of C[x] x C[y].

# Relationships

## Builds Upon
- **Ring** -- Products of rings

## Related
- **Idempotent element** -- Detects product decompositions
- **Chinese Remainder Theorem** -- Produces product ring decompositions

# Source Reference

Chapter 11: Rings, Section 11.6 "Product Rings," Proposition 11.6.1, pages 358-360.

# Verification Notes

- Definition source: Direct from Proposition 11.6.1
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
