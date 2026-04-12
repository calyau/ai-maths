---
concept: Rank of a Free Module
slug: rank-of-free-module
category: module-theory
subcategory: module-types
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Linear Algebra in a Ring"
chapter_number: 14
pdf_page: 432
section: "14.2 Free Modules"
extraction_confidence: high
aliases:
  - "rank"
prerequisites:
  - free-module
extends:
  - dimension
related:
  - basis-of-module
contrasts_with: []
answers_questions:
  - "What is the rank of a free module?"
---

# Quick Definition

The rank of a free module V is the number of elements in any basis for V, analogous to the dimension of a vector space.

# Core Definition

The number of elements of a basis for a free module V is called the rank of V (Artin, p. 436). This is well-defined because any two bases of the same free module over a nonzero ring have the same cardinality (Proposition 14.2.6(b)). The rank is analogous to the dimension of a vector space.

# Prerequisites

- **Free module** -- Rank is defined only for free modules

# Key Properties

1. The rank is well-defined: all bases have the same cardinality (14.2.6(b))
2. The free module R^k has rank k
3. The rank of a free abelian group equals the number of generators in a Z-basis

# Context & Application

Rank provides a numerical invariant for classifying free modules, just as dimension classifies vector spaces. It appears in the structure theorem for finitely generated modules over a PID, where the free part has a well-defined rank.

# Examples

**Example 1** (p. 436): R^n has rank n. The standard basis has n elements.

# Relationships

## Builds Upon
- **Free module** -- Rank is defined for free modules

## Related
- **Dimension** -- Rank generalizes dimension from vector spaces to free modules

# Source Reference

Chapter 14: Linear Algebra in a Ring, Section 14.2, page 436.

# Verification Notes

- Definition source: Direct from Artin, p. 436
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
