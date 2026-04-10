---
concept: Schreier Refinement Theorem for Algebraic Groups
slug: schreier-refinement-theorem
category: group-structure
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 125
section: "9f The Schreier refinement theorem"
extraction_confidence: high
aliases:
  - butterfly lemma
  - Zassenhaus lemma
prerequisites:
  - isomorphism-theorems-algebraic-groups
extends: []
related:
  - solvable-algebraic-group
contrasts_with: []
answers_questions:
  - "Do subnormal series of algebraic groups have equivalent refinements?"
---

# Quick Definition

The Schreier refinement theorem states that any two subnormal series in an algebraic group have equivalent refinements. This implies that composition series (when they exist) have the same length and the same quotients (up to order and isomorphism).

# Core Definition

*Theorem 9.18*: Any two subnormal series in an algebraic group have equivalent refinements. Two subnormal series G = G_0 > ... > G_s = 1 and G = H_0 > ... > H_t = 1 are equivalent if s = t and there is a permutation sigma such that G_i/G_{i+1} = H_{sigma(i)}/H_{sigma(i)+1}. The proof uses the butterfly lemma (Lemma 9.16). Consequence (Theorem 9.19): any two composition series have the same length and isomorphic quotients (Milne, pp. 125-127).

# Prerequisites

- **Isomorphism theorems** -- The butterfly lemma uses the isomorphism theorem

# Key Properties

1. Any two subnormal series have equivalent refinements
2. Composition series have unique length and quotients (up to permutation and isomorphism)
3. An algebraic group is *strongly connected* if it has no finite quotient
4. An algebraic group is *almost-simple* if dim G > 0 and every proper normal N has dim N < dim G

# Context & Application

The Schreier refinement theorem provides the foundation for Jordan-Holder-type decomposition of algebraic groups. It ensures that the "composition factors" of an algebraic group are well-defined.

# Examples

**Example 1** (p. 127): For GL_n, two different subnormal series (e.g., one using SL_n and one using the center) can always be refined to equivalent series.

# Relationships

## Builds Upon
- **Isomorphism theorems** -- The butterfly lemma is a consequence

## Enables
- **Solvable algebraic group** -- The derived series is a special subnormal series

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 9f, pages 125-127. Lemma 9.16, Theorems 9.18-9.20.

# Verification Notes

- Definition source: Direct from Theorem 9.18
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
