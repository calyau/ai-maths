---
# === CORE IDENTIFICATION ===
concept: Intertwining Operator
slug: intertwining-operator

# === CLASSIFICATION ===
category: representations
subcategory: basic-definitions
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of Lie Groups and Lie Algebras"
chapter_number: 4
pdf_page: 38
section: "4.1 Basic definitions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "morphism of representations"
  - "G-morphism"
  - "equivariant map"
  - "G-map"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - representation-of-lie-group
  - representation-of-lie-algebra
extends: []
related:
  - schur-lemma
  - invariant-vectors
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a morphism between two representations?"
  - "What is an intertwining operator?"
---

# Quick Definition

An intertwining operator between two representations $V$ and $W$ of a Lie group $G$ (or Lie algebra $\mathfrak{g}$) is a linear map $f: V \to W$ that commutes with the group (or algebra) action.

# Core Definition

**Definition 4.1 / Remark 4.2** (Kirillov, p. 38): A morphism between two representations $V, W$ of the same group $G$ is a linear map $f: V \to W$ which commutes with the action of $G$: $f \circ \rho(g) = \rho(g) \circ f$ for all $g \in G$. Similarly for Lie algebra representations. The space of all $G$-morphisms is denoted $\mathrm{Hom}_G(V, W)$ (respectively $\mathrm{Hom}_{\mathfrak{g}}(V, W)$).

Morphisms between representations are also frequently called intertwining operators because they "intertwine" the action of $G$ in $V$ and $W$ (Remark 4.2).

# Prerequisites

- **Representation of a Lie group** — The objects between which the morphism is defined
- **Representation of a Lie algebra** — Same concept at the algebra level

# Key Properties

1. The kernel $\ker f$ is a subrepresentation of $V$
2. The image $\mathrm{Im}\, f$ is a subrepresentation of $W$
3. If $G$ is connected, $\mathrm{Hom}_G(V, W) = \mathrm{Hom}_{\mathfrak{g}}(V, W)$ (Theorem 4.3)
4. Intertwining operators form a vector space $\mathrm{Hom}_G(V, W)$
5. Composition of intertwining operators is an intertwining operator

# Construction / Recognition

## To Construct:
1. Define a linear map $f: V \to W$
2. Verify $f(\rho_V(g)v) = \rho_W(g)f(v)$ for all $g \in G$, $v \in V$
3. For Lie algebras: verify $f(\rho_V(x)v) = \rho_W(x)f(v)$ for all $x \in \mathfrak{g}$

## To Identify/Recognize:
1. Check that the map is linear
2. Check that it commutes with the action of each group element (or each Lie algebra element)

# Context & Application

Intertwining operators arise naturally in physics, e.g., as Hamiltonians in quantum mechanics that commute with a symmetry group. The baby example in the Introduction and the hydrogen atom (Section 5.2) are key motivating examples. Understanding intertwining operators is essential for decomposing representations and applying Schur's lemma.

# Examples

**Example** (p. 42-43): In quantum mechanics, a Hamiltonian $H: V \to V$ that is invariant under a symmetry group $G$ (meaning $gHg^{-1} = H$ for all $g \in G$) is precisely an intertwining operator.

**Example 4.13** (p. 41): The space $(\mathrm{Hom}(V, W))^G = \mathrm{Hom}_G(V, W)$ of invariant elements in $\mathrm{Hom}(V, W)$ coincides with the space of intertwining operators.

# Relationships

## Builds Upon
- **Representation of a Lie group** — The objects between which intertwiners act

## Enables
- **Schur's lemma** — Characterizes intertwiners between irreducible representations
- **Decomposition of representations** — Intertwiners relate to projection operators

## Related
- **Invariant vectors** — Invariants in $\mathrm{Hom}(V, W)$ are intertwiners

# Common Errors

- **Error**: Checking the intertwining condition only for generators of $G$ and assuming it holds for all elements.
  **Correction**: For Lie group representations, it suffices to check on Lie algebra generators (by connectedness), but for discrete groups one must check all elements.

# Common Confusions

- **Confusion**: Believing an intertwining operator must be an isomorphism.
  **Clarification**: An intertwining operator is any linear map commuting with the action. It can be zero, injective, surjective, or bijective.

# Source Reference

Chapter 4: Representations of Lie Groups and Lie Algebras, Section 4.1 "Basic definitions," p. 38; Section 4.4, pp. 42-44.

# Verification Notes

- Definition source: Direct from Definition 4.1 and Remark 4.2, p. 38
- Confidence rationale: Explicit definition with clear terminology
- Uncertainties: None
- Cross-reference status: Verified
