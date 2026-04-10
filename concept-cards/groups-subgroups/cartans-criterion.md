---
concept: Cartan's Solvability Criterion
slug: cartans-criterion
category: semisimple-theory
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Lie Algebras and Algebraic Groups"
chapter_number: 2
pdf_page: 271
section: "3e Cartan's first criterion"
extraction_confidence: high
aliases:
  - "Cartan's criterion"
prerequisites:
  - solvable-lie-algebra
  - jordan-decomposition
extends: []
related:
  - killing-form
  - cartan-killing-criterion
contrasts_with: []
answers_questions:
  - "What is the Killing form?"
---

# Quick Definition

Cartan's criterion states that a subalgebra g of gl_V (char 0) is solvable if Tr_V(x o y) = 0 for all x, y in g. In its refined form: g is solvable iff Tr_V(x o y) = 0 for all x in g and y in [g,g].

# Core Definition

Let g be a subalgebra of gl_V, where V is a finite-dimensional vector space over a field k of characteristic zero. Then g is solvable if Tr_V(x o y) = 0 for all x, y in g (Milne, Theorem 3.25). Conversely, if g is solvable, then Tr_V(x o y) = 0 for all x in g and y in [g,g]; and the latter condition on [g,g] alone suffices for solvability (Corollary 3.26).

# Prerequisites

- **Solvable Lie algebra** -- The criterion detects solvability
- **Jordan decomposition** -- Used in the proof

# Key Properties

1. The proof reduces to k = C using the Jordan decomposition and complex conjugation
2. The criterion implies [g,g] consists of nilpotent endomorphisms, then uses Engel's theorem
3. This criterion leads to the Cartan-Killing criterion for semisimplicity

# Context & Application

Cartan's criterion provides a computational test for solvability using trace forms. It is the key ingredient in proving the Cartan-Killing criterion: a Lie algebra is semisimple iff its Killing form is nondegenerate.

# Examples

**Example 1**: For g = b_n (upper triangular), [g,g] = n_n (strictly upper triangular). Then Tr(x o y) = 0 for x in g, y in n_n because the product of an upper triangular and a strictly upper triangular matrix is strictly upper triangular.

# Relationships

## Builds Upon
- **Solvable Lie algebra** -- Detects solvability

## Enables
- **Cartan-Killing criterion** -- The semisimplicity criterion follows from Cartan's criterion

## Related
- **Killing form** -- The Killing form is a special trace form

# Source Reference

Chapter II: Lie Algebras and Algebraic Groups, Section 3e, pages 271-272.

# Verification Notes

- Definition source: Direct from Theorem 3.25
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
