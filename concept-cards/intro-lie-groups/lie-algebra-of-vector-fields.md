---
# === CORE IDENTIFICATION ===
concept: Lie Algebra of Vector Fields
slug: lie-algebra-of-vector-fields

# === CLASSIFICATION ===
category: lie-algebras
subcategory: definitions
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups and Lie Algebras"
chapter_number: 3
pdf_page: 25
section: "3.5"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "$\\mathrm{Vect}(M)$"
  - "commutator of vector fields"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-algebra
  - group-action-on-manifold
extends: []
related:
  - left-invariant-vector-field
  - right-invariant-vector-field
  - derivation-of-lie-algebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Lie algebra?"
---

# Quick Definition

The space $\mathrm{Vect}(M)$ of smooth vector fields on a manifold $M$ is an infinite-dimensional Lie algebra, where the bracket is the commutator of vector fields. This is the "Lie algebra" of the group $\mathrm{Diff}(M)$.

# Core Definition

**Proposition 3.20** (Kirillov): The commutator of vector fields, defined by $\Phi_\xi^t \Phi_\eta^s \Phi_{-\xi}^t \Phi_{-\eta}^s = \Phi_{[\xi, \eta]}^{ts} + \ldots$, gives $\mathrm{Vect}(M)$ the structure of an (infinite-dimensional) Lie algebra.

Equivalently (equation 3.9): $\partial_{[\xi, \eta]} f = \partial_\eta(\partial_\xi f) - \partial_\xi(\partial_\eta f)$ for $f \in C^\infty(M)$.

In local coordinates (equation 3.10): $[\sum f_i \partial_i, \sum g_j \partial_j] = \sum_{i,j}(g_i \partial_i(f_j) - f_i \partial_i(g_j))\partial_j$.

# Prerequisites

- **Lie algebra** — Vect(M) is an example
- **Group action on a manifold** — actions induce Lie algebra morphisms to Vect(M)

# Key Properties

1. **Theorem 3.22**: Any action of $G$ on $M$ defines a Lie algebra morphism $\rho_*: \mathfrak{g} \to \mathrm{Vect}(M)$.
2. Right-invariant vector fields on $G$ form a Lie algebra isomorphic to $\mathfrak{g}$ (Corollary 3.25).
3. Left-invariant fields give the opposite bracket: $[\xi^x, \xi^y] = -\xi^{[x,y]}$ (Exercise 3.4).

# Construction / Recognition

## To Construct/Create:
1. Take smooth vector fields on $M$.
2. Define the bracket via the commutator formula (3.9) or (3.10).

## To Identify/Recognize:
1. The space of smooth sections of $TM$ with the Lie bracket.

# Context & Application

The Lie algebra of vector fields provides the infinitesimal version of diffeomorphisms. For finite-dimensional Lie groups acting on $M$, it gives a concrete realization of the Lie algebra as differential operators.

# Examples

**Example 3.23** (p. 26): For $\mathrm{GL}(n, \mathbb{R})$ acting on $\mathbb{R}^n$, each $a \in \mathfrak{gl}(n)$ gives the vector field $v_a(x) = \sum a_{ij} x_j \partial_i$.

**Remark 3.21** (p. 26): Warning: many books use the opposite sign convention for the commutator of vector fields.

# Relationships

## Builds Upon
- **Lie algebra** — Vect(M) is an infinite-dimensional Lie algebra

## Enables
- **Corollary 3.25** — identifies $\mathfrak{g}$ with right-invariant fields
- **Frobenius theorem application** — integrability via brackets of vector fields

## Related
- **Left-invariant vector field** — special vector fields on a Lie group
- **Derivation of Lie algebra** — vector fields act as derivations on $C^\infty(M)$

# Common Errors

- **Error**: Using the wrong sign convention for the commutator.
  **Correction**: Kirillov's convention matches the group multiplication; many differential geometry books use the opposite sign (Remark 3.21).

# Common Confusions

- **Confusion**: Whether $\mathrm{Diff}(M)$ is a Lie group.
  **Clarification**: It is not finite-dimensional, so it is not a Lie group in the strict sense. But $\mathrm{Vect}(M)$ plays the role of its "Lie algebra."

# Source Reference

Chapter 3: Lie Groups and Lie Algebras, Section 3.5, Proposition 3.20, Theorem 3.22, pages 25-27.

# Verification Notes

- Definition source: Direct from Proposition 3.20
- Confidence rationale: Explicit proposition with multiple equivalent formulas
- Uncertainties: None
- Cross-reference status: Verified with Theorem 3.22, Corollary 3.25, Example 3.23
