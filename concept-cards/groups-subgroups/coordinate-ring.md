---
# === CORE IDENTIFICATION ===
concept: Coordinate Ring
slug: coordinate-ring

# === CLASSIFICATION ===
category: algebraic-groups
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 22
section: "Definition of an affine (algebraic) group"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - coordinate algebra
  - "O(G)"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - affine-group
  - affine-algebraic-group
  - hopf-algebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I construct the Hopf algebra of an affine algebraic group?"
  - "What must I know before understanding Hopf algebras?"
---

# Quick Definition

The coordinate ring O(G) of an affine group G = (A, Delta) is the k-algebra A that represents the group functor. Its elements are natural families of functions f_R: G(R) -> R indexed by k-algebras R.

# Core Definition

Let G = (A, Delta) be an affine group. The ring A is called the **coordinate ring** (or **coordinate algebra**) of G, and is denoted O(G) (Definition 2.9, p. 22).

An element f of O(G) can be viewed in two equivalent ways (2.16, p. 25):
- As a natural family of maps f_R: G(R) -> R of sets, indexed by k-algebras R
- As a generator of the k-algebra A representing the functor G

These are related by the equation f_R(g) = g(f), where g in G(R) is regarded as a k-algebra homomorphism g: A -> R. Moreover, (Delta f)_R(g_1, g_2) = f_R(g_1 * g_2).

# Prerequisites

This is a foundational concept with no prerequisites within this source (beyond basic commutative algebra).

# Key Properties

1. O(G) carries a natural Hopf algebra structure (comultiplication, counit, and antipode)
2. O(G tensor G) = O(G) tensor O(G), so the comultiplication Delta: O(G) -> O(G) tensor O(G) encodes the group law
3. A homomorphism alpha: G -> H induces a Hopf algebra map alpha*: O(H) -> O(G)
4. When G is algebraic, O(G) is finitely presented as a k-algebra

# Examples

**Example 1** (p. 22): O(G_a) = k[X], with elements corresponding to polynomial functions on the additive group.

**Example 2** (p. 29): O(G_m) = k[X, X^{-1}], with elements corresponding to Laurent polynomial functions on the multiplicative group.

**Example 3** (p. 31): O(GL_n) = k[X_11,...,X_nn, det(X_ij)^{-1}], i.e., the localization of the polynomial ring at the determinant.

# Relationships

## Enables
- **Hopf algebra** — O(G) is the prototypical commutative Hopf algebra
- **Affine group scheme** — Spec(O(G)) is the underlying scheme

## Related
- **Affine algebraic group** — Defined by the condition that O(G) is finitely presented

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 2c, Definition 2.9, p. 22. Dual viewpoint at Summary 2.16, p. 25.

# Verification Notes

- Definition source: Direct from Definition 2.9 and Summary 2.16
- Confidence rationale: Explicit definition with extensive discussion
- Uncertainties: None
- Cross-reference status: Verified
