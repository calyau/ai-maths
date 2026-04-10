---
concept: Coconnected Hopf Algebra
slug: coconnected-hopf-algebra
category: unipotent-groups
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 177
section: "15b Unipotent affine groups"
extraction_confidence: high
aliases: []
prerequisites:
  - hopf-algebra
extends: []
related:
  - unipotent-group
contrasts_with: []
answers_questions:
  - "What is a coconnected Hopf algebra?"
---

# Quick Definition

A Hopf algebra A is coconnected if it admits a filtration C_0 = k subset C_1 subset C_2 subset ... with union A and Delta(C_r) subset sum C_i tensor C_{r-i}. This is the algebraic characterization of unipotent groups: G is unipotent iff O(G) is coconnected.

# Core Definition

A Hopf algebra A is *coconnected* if there exists a filtration C_0 subset C_1 subset C_2 subset ... of A by subspaces such that C_0 = k, the union of all C_r is A, and Delta(C_r) subset sum_{0 <= i <= r} C_i tensor C_{r-i} (Definition 15.5). The key theorem (15.6) states: an algebraic group G is unipotent iff O(G) is coconnected (Milne, pp. 177-178).

# Prerequisites

- **Hopf algebra** -- Coconnected is a property of Hopf algebras

# Key Properties

1. Any quotient of a coconnected Hopf algebra is coconnected
2. O(U_n) is coconnected with the filtration given by weight (j-i for X_{ij})
3. If O(G) is coconnected, then every comodule has a nonzero fixed vector
4. Coconnected = "only one group-like element" (the identity)

# Context & Application

Coconnectedness provides the algebraic criterion for unipotence, avoiding the need to choose representations or embeddings.

# Examples

**Example 1** (p. 178): O(U_n) = k[X_{ij} | i < j]. Assign weight j-i to X_{ij}. Then C_r = span of monomials of weight <= r satisfies the coconnectedness axioms.

# Relationships

## Enables
- **Unipotent group** -- G unipotent iff O(G) coconnected

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 15b, pages 177-178. Definition 15.5, Theorem 15.6.

# Verification Notes

- Definition source: Direct from Definition 15.5
- Confidence rationale: Explicit definition with complete proof of equivalence
- Uncertainties: None
- Cross-reference status: Verified
