---
concept: Engel's Theorem
slug: engels-theorem
category: semisimple-theory
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Lie Algebras and Algebraic Groups"
chapter_number: 2
pdf_page: 265
section: "3b Nilpotent Lie algebras: Engel's theorems"
extraction_confidence: high
aliases:
  - "Engel's theorems"
prerequisites:
  - nilpotent-lie-algebra
  - adjoint-representation-of-lie-algebra
extends: []
related:
  - lies-theorem
contrasts_with: []
answers_questions:
  - "What distinguishes a nilpotent Lie algebra from a solvable Lie algebra?"
---

# Quick Definition

Engel's theorem states that a Lie algebra g is nilpotent if and only if ad(x) is a nilpotent endomorphism for every x in g. A stronger form says: if a subalgebra of gl_V consists entirely of nilpotent endomorphisms, then there is a basis putting it in strictly upper triangular form.

# Core Definition

**Engel's theorem** has three equivalent forms (Milne, Theorems 3.9-3.11): (1) g is nilpotent iff ad(x) is nilpotent for every x; (2) if g is a subalgebra of gl_V consisting of nilpotent endomorphisms, there exists a basis for which g is in n_n; (3) if alpha: g -> gl_V is a representation with alpha(x) nilpotent for all x, then there exists a nonzero v with gv = 0.

# Prerequisites

- **Nilpotent Lie algebra** -- The theorem characterizes nilpotency
- **Adjoint representation of Lie algebra** -- Uses nilpotency of ad(x)

# Key Properties

1. If x is nilpotent in End(V), then ad(x) is nilpotent in End(End(V)): if x^n = 0 then (ad x)^{2n} = 0 (Lemma 3.13)
2. The theorem gives a common eigenvector (the analogue of a common fixed point for nilpotent groups)

# Context & Application

Engel's theorem is the Lie algebra analogue of the fact that a finite nilpotent group has a nontrivial centre. It provides the key inductive step for proving structural results about nilpotent Lie algebras.

# Examples

**Example 1** (p. 266): For n_n (strictly upper triangular matrices), every element x satisfies x^n = 0, confirming nilpotency.

# Relationships

## Builds Upon
- **Nilpotent Lie algebra** -- Characterizes nilpotency

## Related
- **Lie's theorem** -- The solvable analogue of Engel's theorem

# Source Reference

Chapter II: Lie Algebras and Algebraic Groups, Section 3b, pages 265-267.

# Verification Notes

- Definition source: Direct from Theorems 3.9-3.11
- Confidence rationale: Explicit theorem statements with proofs
- Uncertainties: None
- Cross-reference status: Verified
