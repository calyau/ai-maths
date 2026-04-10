---
concept: Lie's Theorem
slug: lies-theorem
category: semisimple-theory
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Lie Algebras and Algebraic Groups"
chapter_number: 2
pdf_page: 267
section: "3c Solvable Lie algebras: Lie's theorem"
extraction_confidence: high
aliases:
  - "Lie-Kolchin theorem for Lie algebras"
prerequisites:
  - solvable-lie-algebra
extends: []
related:
  - engels-theorem
  - cartans-criterion
contrasts_with: []
answers_questions:
  - "What distinguishes a nilpotent Lie algebra from a solvable Lie algebra?"
---

# Quick Definition

Lie's theorem states that over an algebraically closed field of characteristic zero, any solvable subalgebra of gl_V can be simultaneously put in upper triangular form. In particular, [g,g] consists of nilpotent endomorphisms.

# Core Definition

Let V be a finite-dimensional vector space over an algebraically closed field k of characteristic zero, and let g be a solvable subalgebra of gl_V. Then there exists a basis of V for which g is contained in b_{dim V} (upper triangular matrices) (Milne, Theorem 3.14). A corollary: if g is solvable (char 0), then [g,g] is nilpotent (Corollary 3.15).

# Prerequisites

- **Solvable Lie algebra** -- The theorem applies to solvable algebras

# Key Properties

1. Requires k algebraically closed and char(k) = 0
2. Fails in characteristic p (Examples 3.16, 3.17)
3. The key lemma is the Invariance Lemma (3.19): eigenspaces V_lambda of an ideal are stable under g
4. Works for dim V < p in characteristic p (Aside 3.21)

# Context & Application

Lie's theorem is the Lie algebra analogue of the Lie-Kolchin theorem for solvable algebraic groups. Together with Engel's theorem, it provides the key tools for analyzing the structure of solvable Lie algebras and for proving Cartan's solvability criterion.

# Examples

**Example 1** (p. 267): In characteristic 2, sl_2 is solvable but cannot be put in upper triangular form.

**Example 2** (p. 268): In characteristic p, there exist solvable subalgebras of gl_p with no simultaneous eigenvector.

# Relationships

## Builds Upon
- **Solvable Lie algebra** -- The theorem characterizes solvable subalgebras of gl_V

## Enables
- **Cartan's criterion** -- Uses Lie's theorem in its proof

## Related
- **Engel's theorem** -- The nilpotent analogue

# Source Reference

Chapter II: Lie Algebras and Algebraic Groups, Section 3c, pages 267-270.

# Verification Notes

- Definition source: Direct from Theorem 3.14
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
