---
concept: Derivation of a Lie Algebra
slug: derivation-of-lie-algebra
category: lie-algebras
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Lie Algebras and Algebraic Groups"
chapter_number: 2
pdf_page: 239
section: "1a Lie algebras: basic definitions"
extraction_confidence: high
aliases:
  - "Der_k(g)"
  - "inner derivation"
prerequisites:
  - lie-algebra
extends: []
related:
  - adjoint-representation-of-lie-algebra
contrasts_with: []
answers_questions:
  - "What is a Lie algebra?"
---

# Quick Definition

A derivation of a k-algebra A is a k-linear map D: A -> A satisfying the Leibniz rule D(ab) = D(a)b + aD(b). The derivations of a Lie algebra g form a Lie algebra Der_k(g), and the inner derivations ad(x) form an ideal.

# Core Definition

A **derivation** of a k-algebra A is a k-linear map D: A -> A such that D(ab) = D(a)b + aD(b) (Milne, Example 1.3). The set Der_k(A) of k-derivations is a Lie subalgebra of gl_A with bracket [D,E] = D o E - E o D. For a Lie algebra g, the derivations ad(x) for x in g are called **inner derivations**.

# Prerequisites

- **Lie algebra** -- Derivations are defined on Lie algebras

# Key Properties

1. Der_k(A) is a Lie subalgebra of gl_A
2. The inner derivations ad(g) form an ideal in Der(g) (Lemma 5.20)
3. For semisimple g, ad: g -> Der(g) is an isomorphism (Theorem 5.21)

# Examples

**Example 1** (p. 239): For an associative algebra A, [D,E] = D o E - E o D is again a derivation.

# Relationships

## Builds Upon
- **Lie algebra** -- Derivations of g form a Lie algebra

## Enables
- **Adjoint representation of Lie algebra** -- ad(x) is the inner derivation y -> [x,y]

# Source Reference

Chapter II: Lie Algebras and Algebraic Groups, Section 1a, page 239.

# Verification Notes

- Definition source: Direct from Example 1.3
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
