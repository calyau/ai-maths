---
concept: Dual Numbers
slug: dual-numbers
category: lie-algebras
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Lie Algebras and Algebraic Groups"
chapter_number: 2
pdf_page: 241
section: "1c The Lie algebra of an algebraic group"
extraction_confidence: high
aliases:
  - "k[epsilon]"
prerequisites: []
extends: []
related:
  - lie-algebra-of-algebraic-group
contrasts_with: []
answers_questions:
  - "How does the Lie algebra functor connect algebraic groups to Lie algebras?"
---

# Quick Definition

The ring of dual numbers k[epsilon] = k[X]/(X^2) is a two-dimensional k-algebra with epsilon^2 = 0. It is the algebraic device used to define the Lie algebra of an algebraic group as Lie(G) = Ker(G(k[epsilon]) -> G(k)).

# Core Definition

The **ring of dual numbers** is k[epsilon] = k[X]/(X^2), so k[epsilon] = k + k*epsilon as a k-vector space with epsilon^2 = 0 (Milne, p. 241). There is a homomorphism pi: k[epsilon] -> k sending a + epsilon*b to a. The Lie algebra of G is Lie(G) = Ker(G(pi)).

# Prerequisites

This is a foundational algebraic concept.

# Key Properties

1. k[epsilon]^x = {a + b*epsilon | a != 0} (Remark 1.13)
2. Lie(G) depends only on the local ring O(G)_m (Remark 1.13)
3. For c in k, u_c: k[epsilon] -> k[epsilon] sends a + epsilon*b to a + c*epsilon*b, defining the k-vector space structure on Lie(G) (Remark 1.14)

# Context & Application

The dual numbers provide the algebraic analogue of tangent vectors: Lie(G) is the tangent space to G at the identity. The epsilon^2 = 0 condition means we are looking at "first-order infinitesimal" behavior.

# Examples

**Example 1** (p. 241): For GL_n, an element I_n + epsilon*A of M_n(k[epsilon]) is always invertible (with inverse I_n - epsilon*A), so Lie(GL_n) = M_n(k).

# Relationships

## Enables
- **Lie algebra of algebraic group** -- Lie(G) = Ker(G(k[epsilon]) -> G(k))

# Source Reference

Chapter II: Lie Algebras and Algebraic Groups, Section 1c, page 241.

# Verification Notes

- Definition source: Direct from p. 241
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
