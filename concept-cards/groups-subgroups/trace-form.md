---
concept: Trace Form
slug: trace-form
category: semisimple-theory
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Lie Algebras and Algebraic Groups"
chapter_number: 2
pdf_page: 277
section: "5a Semisimple Lie algebras"
extraction_confidence: high
aliases:
  - "beta_V"
  - "associative form"
prerequisites:
  - lie-algebra
extends: []
related:
  - killing-form
  - cartans-criterion
contrasts_with: []
answers_questions:
  - "What is the Killing form?"
---

# Quick Definition

The trace form beta_V for a representation g -> gl_V is the bilinear form beta_V(x,y) = Tr_V(x_V o y_V). It is symmetric, bilinear, and associative. For a faithful representation of a semisimple Lie algebra, it is nondegenerate.

# Core Definition

Let rho: g -> gl_V be a representation. The **trace form** beta_V: g x g -> k is defined by beta_V(x,y) = Tr_V(x_V o y_V) (Milne, p. 277). A bilinear form B on g is **associative** if B([x,y],z) = B(x,[y,z]) for all x,y,z (p. 277).

# Prerequisites

- **Lie algebra** -- Trace forms are defined for representations of Lie algebras

# Key Properties

1. beta_V is symmetric: Tr(AB) = Tr(BA) (Lemma 5.8)
2. beta_V is associative: beta_V([x,y],z) = beta_V(x,[y,z]) (Lemma 5.8)
3. The orthogonal complement of an ideal (w.r.t. an associative form) is an ideal (Lemma 5.7)
4. For a faithful rep of a semisimple g, beta_V is nondegenerate (Proposition 5.9)
5. The Killing form is the trace form for the adjoint representation

# Examples

**Example 1**: For g = sl_n with the standard representation V = k^n, beta_V(A,B) = Tr(AB).

# Relationships

## Enables
- **Killing form** -- The Killing form is the trace form for the adjoint representation
- **Cartan's criterion** -- Uses trace forms to detect solvability

# Source Reference

Chapter II: Lie Algebras and Algebraic Groups, Section 5a, pages 277-278.

# Verification Notes

- Definition source: Direct from p. 277
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
