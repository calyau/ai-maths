---
concept: Casimir Operator
slug: casimir-operator
category: semisimple-theory
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Lie Algebras and Algebraic Groups"
chapter_number: 2
pdf_page: 288
section: "6c Representations of Lie algebras"
extraction_confidence: high
aliases:
  - "c_V"
prerequisites:
  - semisimple-lie-algebra
  - trace-form
extends: []
related:
  - weyls-theorem
  - universal-enveloping-algebra
contrasts_with: []
answers_questions:
  - "What is the Killing form?"
---

# Quick Definition

The Casimir operator c_V for a faithful representation g -> gl_V of a semisimple Lie algebra is c_V = sum e_{iV} o e'_{iV}, where {e_i} and {e'_i} are dual bases for g w.r.t. the trace form beta_V. It is a g-endomorphism of V with Tr_V(c_V) = dim(g).

# Core Definition

Let g be semisimple with faithful representation g -> gl_V. For any basis e_1,...,e_n of g and its dual basis e'_1,...,e'_n w.r.t. beta_V (so beta_V(e_i, e'_j) = delta_{ij}), the **Casimir operator** is c_V = sum_{i=1}^n e_{iV} o e'_{iV} (Milne, p. 288).

# Prerequisites

- **Semisimple Lie algebra** -- The Casimir operator requires a nondegenerate trace form
- **Trace form** -- Dual bases are defined w.r.t. beta_V

# Key Properties

1. c_V is independent of the choice of basis (Proposition 6.8a)
2. c_V is a g-module homomorphism V -> V (Proposition 6.8b)
3. Tr_V(c_V) = n = dim(g) (Proposition 6.8c)
4. The Casimir element c = sum e_i . e'_i in U(g) maps to c_V under every representation (Aside 6.9)
5. c lies in the centre of U(g)

# Context & Application

The Casimir operator is the key technical tool in the proof of Weyl's complete reducibility theorem. Its nontrivial trace ensures it acts nontrivially, which combined with Schur's lemma provides the complementary subspace in the inductive step.

# Examples

**Example 1** (p. 289): For a codimension-1 submodule W of V with W simple, c_V acts as a nonzero scalar on W (Schur) and as 0 on V/W (since g acts trivially there), so Ker(c_V) complements W.

# Relationships

## Builds Upon
- **Trace form** -- Uses dual bases w.r.t. beta_V

## Enables
- **Weyl's theorem** -- Casimir operator is the key tool in the proof

## Related
- **Universal enveloping algebra** -- The Casimir element lives in the centre of U(g)

# Source Reference

Chapter II: Lie Algebras and Algebraic Groups, Section 6c, pages 288-289.

# Verification Notes

- Definition source: Direct from p. 288
- Confidence rationale: Explicit definition with properties
- Uncertainties: None
- Cross-reference status: Verified
