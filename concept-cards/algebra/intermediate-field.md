---
concept: Intermediate Field
slug: intermediate-field
category: galois-theory
subcategory: core-definitions
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Galois Theory"
chapter_number: 16
pdf_page: 488
section: "16.6 Galois Extensions"
extraction_confidence: high
aliases: []
prerequisites:
  - field-extension
extends: []
related:
  - fundamental-theorem-galois-theory
  - galois-extension
contrasts_with: []
answers_questions:
  - "What is an intermediate field?"
---

# Quick Definition

An intermediate field L of an extension K/F is a field satisfying F in L in K. A proper intermediate field is one that is neither F nor K.

# Core Definition

If K is an extension field of F, an intermediate field L is a field such that F in L in K. An intermediate field is proper if it is neither F nor K (Artin, p. 497). The Fundamental Theorem of Galois Theory establishes a bijection between intermediate fields and subgroups of the Galois group.

# Prerequisites

- **Field extension** -- Intermediate fields sit between F and K

# Key Properties

1. A finite extension K/F has finitely many intermediate fields (16.7.3)
2. In a Galois extension, intermediate fields correspond bijectively to subgroups of G(K/F) (16.7.1)
3. L/F is Galois iff the corresponding subgroup is normal (16.7.5)
4. [L:F] = [G:H] where H is the subgroup corresponding to L (16.7.2(c))

# Context & Application

Intermediate fields are the objects classified by the Galois correspondence. Understanding them is essential for applying Galois theory to specific problems.

# Examples

**Example 1** (p. 501): K = Q(sqrt(3), sqrt(5)) over Q has exactly three proper intermediate fields: Q(sqrt(3)), Q(sqrt(5)), Q(sqrt(15)), corresponding to the three subgroups of order 2 in the Klein four group.

# Relationships

## Builds Upon
- **Field extension** -- Intermediate fields are between F and K

## Related
- **Fundamental theorem of Galois theory** -- Classifies intermediate fields via subgroups

# Source Reference

Chapter 16: Galois Theory, Section 16.6, page 497. Corollary 16.7.3.

# Verification Notes

- Definition source: Direct from Artin, p. 497
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
