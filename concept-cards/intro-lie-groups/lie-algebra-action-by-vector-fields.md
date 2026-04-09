---
# === CORE IDENTIFICATION ===
concept: Lie Algebra Action by Vector Fields
slug: lie-algebra-action-by-vector-fields

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
pdf_page: 26
section: "3.5"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "$\\rho_*: \\mathfrak{g} \\to \\mathrm{Vect}(M)$"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-algebra
  - group-action-on-manifold
  - lie-algebra-of-vector-fields
extends: []
related:
  - stabilizer-lie-algebra
  - right-invariant-vector-field
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a Lie algebra relate to its Lie group?"
---

# Quick Definition

Any action of a Lie group $G$ on a manifold $M$ induces a Lie algebra morphism $\rho_*: \mathfrak{g} \to \mathrm{Vect}(M)$, mapping each $x \in \mathfrak{g}$ to a vector field on $M$.

# Core Definition

**Theorem 3.22** (Kirillov): Let $G$ act on $M$.
1. This action defines a linear map $\rho_*: \mathfrak{g} \to \mathrm{Vect}(M)$.
2. $\rho_*$ is a morphism of Lie algebras: $\rho_*[x, y] = [\rho_*(x), \rho_*(y)]$.

# Prerequisites

- **Lie algebra** — the source of the map
- **Group action on a manifold** — the group action inducing the algebra action
- **Lie algebra of vector fields** — the target of the map

# Key Properties

1. For $x \in \mathfrak{g}$, $\rho_*(x)(m) = \frac{d}{dt}|_{t=0} \exp(tx).m$.
2. The map preserves brackets.
3. The kernel of $\rho_*|_m$ (evaluation at $m$) gives the stabilizer Lie algebra.
4. The flow of $\rho_*(x)$ is $\Phi^t(m) = \exp(tx).m$.

# Construction / Recognition

## To Construct/Create:
1. Given an action $\rho: G \to \mathrm{Diff}(M)$, differentiate at $g = 1$.
2. $\rho_*(x)(m) = \frac{d}{dt}|_{t=0} \rho(\exp(tx))(m)$.

## To Identify/Recognize:
1. A Lie algebra morphism from $\mathfrak{g}$ to vector fields on $M$.

# Context & Application

This is the infinitesimal version of a group action. It converts group-level symmetries into differential equations (vector fields), which are often easier to work with.

# Examples

**Example 3.23** (p. 26): $\mathrm{GL}(n)$ acts on $\mathbb{R}^n$; each $a \in \mathfrak{gl}(n)$ gives $v_a(x) = \sum a_{ij}x_j\partial_i$.

**Proposition 3.24** (p. 27): Left multiplication $L(g).h = gh$ gives right-invariant vector fields.

# Relationships

## Builds Upon
- **Group action on a manifold** — the group action being differentiated
- **Lie algebra of vector fields** — the target

## Enables
- **Stabilizer Lie algebra** — kernel of $\rho_*$ at a point
- **Frobenius-based proofs** — via generated distributions

## Related
- **Right-invariant vector field** — left multiplication action gives these

# Common Errors

- **Error**: Confusing the action of $\mathfrak{g}$ with the action of $G$.
  **Correction**: $G$ acts by diffeomorphisms; $\mathfrak{g}$ acts by vector fields. They are related by the exponential map.

# Common Confusions

- **Confusion**: Why the left multiplication action gives right-invariant (not left-invariant) fields.
  **Clarification**: $L_*(x)(g) = \frac{d}{dt}\exp(tx)g = xg$, which defines a right-invariant field (Proposition 3.24).

# Source Reference

Chapter 3: Lie Groups and Lie Algebras, Section 3.5, Theorem 3.22, Proposition 3.24, pages 26-27.

# Verification Notes

- Definition source: Direct from Theorem 3.22
- Confidence rationale: Explicit theorem
- Uncertainties: None
- Cross-reference status: Verified with Example 3.23, Proposition 3.24
