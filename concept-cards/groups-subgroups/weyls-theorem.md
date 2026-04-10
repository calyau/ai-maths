---
concept: Weyl's Complete Reducibility Theorem
slug: weyls-theorem
category: semisimple-theory
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Lie Algebras and Algebraic Groups"
chapter_number: 2
pdf_page: 289
section: "6c Representations of Lie algebras"
extraction_confidence: high
aliases:
  - "Weyl's theorem"
  - "complete reducibility"
prerequisites:
  - semisimple-lie-algebra
  - killing-form
  - casimir-operator
extends: []
related:
  - semisimple-representation-of-reductive-group
contrasts_with: []
answers_questions:
  - "What is the Killing form?"
---

# Quick Definition

Weyl's theorem states that a Lie algebra g (over a field of characteristic zero) is semisimple if and only if every finite-dimensional representation of g is semisimple (completely reducible).

# Core Definition

A Lie algebra g is semisimple if and only if every finite-dimensional representation of g is semisimple (Milne, Theorem 6.10). The proof uses the Casimir operator: for a semisimple g with faithful representation g -> gl_V, the Casimir element c_V = sum e_{iV} o e'_{iV} (dual basis w.r.t. beta_V) is a g-module endomorphism with Tr_V(c_V) = dim g (Proposition 6.8).

# Prerequisites

- **Semisimple Lie algebra** -- The theorem characterizes semisimplicity
- **Killing form** -- Used in constructing the Casimir operator
- **Casimir operator** -- Key tool in the proof

# Key Properties

1. Forward direction: if all representations are semisimple, then the adjoint representation is semisimple, which forces g to be semisimple
2. Reverse direction uses the Casimir operator and induction on codimension
3. The theorem extends to algebraic groups: Rep(G) semisimple iff G^0 reductive (Theorems 6.14, 6.17)
4. Fails for infinite-dimensional representations even of sl_2 (Aside 6.11)
5. The result requires characteristic zero

# Context & Application

Weyl's theorem is the foundation for representation theory of semisimple Lie algebras and reductive groups. It establishes that the representation category of a semisimple Lie algebra is semisimple, which extends to reductive algebraic groups via the Lie functor.

# Examples

**Example 1** (p. 289): For the codimension-1 case with simple W: the Casimir operator c_V acts as a nonzero scalar on W (Schur's lemma) and trivially on V/W, so Ker(c_V) is the complement.

# Relationships

## Builds Upon
- **Semisimple Lie algebra** -- Characterizes semisimplicity via representations
- **Casimir operator** -- Key tool in the proof

## Enables
- **Semisimple representation of reductive group** -- Extends to algebraic groups in char 0

# Source Reference

Chapter II: Lie Algebras and Algebraic Groups, Section 6c, pages 289-291.

# Verification Notes

- Definition source: Direct from Theorem 6.10
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
