---
concept: Nonabelian Galois Cohomology
slug: nonabelian-galois-cohomology
category: classical-groups
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 217
section: "19a Nonabelian cohomology"
extraction_confidence: high
aliases:
  - "H^1(Gamma, A)"
  - "Galois cohomology"
prerequisites:
  - galois-theory
extends: []
related:
  - forms-of-algebraic-group
  - classical-semisimple-groups
contrasts_with: []
answers_questions:
  - "What is a semisimple algebraic group?"
---

# Quick Definition

Nonabelian Galois cohomology H^1(Gamma, A) classifies equivalence classes of 1-cocycles from a group Gamma to a Gamma-group A. For algebraic groups, H^1(k, G) classifies the forms of G, i.e., algebraic groups becoming isomorphic to G over k^{al}.

# Core Definition

Let Gamma be a group acting on a group A. A **1-cocycle** is a map sigma -> a_sigma from Gamma to A satisfying a_{sigma*tau} = a_sigma * sigma(a_tau). Two cocycles are **equivalent** if there exists c in A with b_sigma = c^{-1} * a_sigma * sigma(c). The set **H^1(Gamma, A)** is the set of equivalence classes (Milne, p. 217). For algebraic groups, H^1(k, G) = H^1(Gal(k^{al}/k), G(k^{al})) classifies forms.

# Prerequisites

- **Galois theory** -- H^1 uses the Galois group action

# Key Properties

1. H^1(Gamma, A) is a pointed set, not generally a group (unless A is abelian)
2. An exact sequence 1 -> A' -> A -> A'' -> 1 gives an exact sequence of cohomology sets (Proposition 19.1)
3. H^1(k, GL_n) = 1 (Proposition 19.4, equivalent to Hilbert 90)
4. H^1(k, SL_n) = 1 (Proposition 19.5)
5. H^1(k, Sp_n) = 1 (Proposition 19.6)
6. H^1(k, O(phi)) classifies quadratic spaces of given dimension (Remark 19.7)

# Context & Application

Nonabelian cohomology is the primary tool for classifying forms of algebraic groups over non-algebraically closed fields. It connects the abstract theory of algebraic groups with concrete algebraic structures like central simple algebras and quadratic forms.

# Examples

**Example 1** (p. 220): H^1(k, GL_n) = 1 says all k-vector spaces of dimension n are isomorphic -- this is Hilbert's Theorem 90.

**Example 2** (p. 220): H^1(k, O(phi)) classifies nondegenerate quadratic spaces of the same dimension as (V, phi).

# Relationships

## Enables
- **Forms of algebraic group** -- H^1 classifies the forms
- **Classical semisimple groups** -- Classification uses H^1

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 19a, pages 217-220.

# Verification Notes

- Definition source: Direct from p. 217
- Confidence rationale: Explicit definitions and examples
- Uncertainties: None
- Cross-reference status: Verified
