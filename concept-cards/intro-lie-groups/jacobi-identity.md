---
# === CORE IDENTIFICATION ===
concept: Jacobi Identity
slug: jacobi-identity

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
pdf_page: 24
section: "3.3"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - commutator-bracket
  - ad-map
extends: []
related:
  - lie-algebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Lie algebra?"
---

# Quick Definition

The Jacobi identity is the fundamental identity satisfied by the Lie bracket: $[x, [y, z]] + [y, [z, x]] + [z, [x, y]] = 0$. Together with skew-symmetry, it defines a Lie algebra.

# Core Definition

**Theorem 3.15** (Kirillov): The commutator satisfies the Jacobi identity, which has the following equivalent forms:

$$[x, [y, z]] = [[x, y], z] + [y, [x, z]]$$
$$[x, [y, z]] + [y, [z, x]] + [z, [x, y]] = 0$$
$$\mathrm{ad}\, x . [y, z] = [\mathrm{ad}\, x . y, z] + [y, \mathrm{ad}\, x . z]$$
$$\mathrm{ad}[x, y] = \mathrm{ad}\, x \circ \mathrm{ad}\, y - \mathrm{ad}\, y \circ \mathrm{ad}\, x$$

# Prerequisites

- **Commutator bracket** — the operation satisfying the identity
- **ad map** — provides the most illuminating form of the identity

# Key Properties

1. The Jacobi identity follows from associativity of the group multiplication via the ad map.
2. The first form says $\mathrm{ad}\, x$ is a derivation of the bracket.
3. The last form says $\mathrm{ad}: \mathfrak{g} \to \mathfrak{gl}(\mathfrak{g})$ is a Lie algebra morphism.
4. Equivalently: associativity of the group $\Rightarrow$ Ad is a group morphism $\Rightarrow$ ad preserves brackets $\Rightarrow$ Jacobi identity.

# Construction / Recognition

## To Construct/Create:
Not applicable (an identity).

## To Identify/Recognize:
1. Check that a proposed bracket satisfies $[x, [y, z]] + [y, [z, x]] + [z, [x, y]] = 0$.

# Context & Application

The Jacobi identity is one of the two axioms defining a Lie algebra (the other being skew-symmetry). It replaces associativity — Lie algebras are generally not associative.

# Examples

**Example** (p. 24): The proof uses that $\mathrm{Ad}: G \to \mathrm{GL}(\mathfrak{g})$ is a morphism, so $\mathrm{ad} = \mathrm{Ad}_*$ preserves brackets. But the bracket in $\mathfrak{gl}(\mathfrak{g})$ is $[A, B] = AB - BA$, giving $\mathrm{ad}[x, y] = \mathrm{ad}\, x \circ \mathrm{ad}\, y - \mathrm{ad}\, y \circ \mathrm{ad}\, x$.

**Example**: For $\mathfrak{gl}(n)$ with $[x, y] = xy - yx$, the Jacobi identity can be verified directly by expanding.

# Relationships

## Builds Upon
- **Commutator bracket** — the bracket satisfying the identity
- **ad map** — gives the cleanest proof

## Enables
- **Lie algebra** — one of the defining axioms

## Related
- **Associativity** — the Jacobi identity is the "shadow" of group associativity at the algebra level

# Common Errors

- **Error**: Thinking the Jacobi identity means the bracket is associative.
  **Correction**: In general, $[[x,y],z] \neq [x,[y,z]]$. The Jacobi identity relates these but does not equate them.

# Common Confusions

- **Confusion**: Whether the cyclic form or the derivation form is more fundamental.
  **Clarification**: They are equivalent. The derivation form ($\mathrm{ad}\, x$ is a derivation) is often more useful in practice.

# Source Reference

Chapter 3: Lie Groups and Lie Algebras, Section 3.3, Theorem 3.15, page 24.

# Verification Notes

- Definition source: Direct from Theorem 3.15
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
