---
# === CORE IDENTIFICATION ===
concept: Equivalence of Group and Algebra Representations
slug: equivalence-of-group-and-algebra-representations

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
pdf_page: 39
section: "4.1 Basic definitions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Lie correspondence for representations"
  - "lifting representations"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - representation-of-lie-group
  - representation-of-lie-algebra
  - lie-group
extends:
  - exponential-map
related:
  - complexification-of-lie-algebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do representations of a Lie group relate to representations of its Lie algebra?"
  - "When can a Lie algebra representation be lifted to a group representation?"
---

# Quick Definition

For a connected, simply-connected Lie group $G$ with Lie algebra $\mathfrak{g}$, the categories of finite-dimensional representations of $G$ and $\mathfrak{g}$ are equivalent: every representation of $\mathfrak{g}$ lifts uniquely to a representation of $G$.

# Core Definition

**Theorem 4.3** (Kirillov, p. 39): Let $G$ be a Lie group with Lie algebra $\mathfrak{g}$.

1. Every representation $\rho: G \to GL(V)$ defines a representation $\rho_*: \mathfrak{g} \to \mathfrak{gl}(V)$, and every morphism of representations of $G$ is automatically a morphism of representations of $\mathfrak{g}$.
2. If $G$ is connected, simply-connected, then $\rho \mapsto \rho_*$ gives an equivalence of categories of representations of $G$ and representations of $\mathfrak{g}$. In particular, every representation of $\mathfrak{g}$ can be uniquely lifted to a representation of $G$, and $\mathrm{Hom}_G(V, W) = \mathrm{Hom}_{\mathfrak{g}}(V, W)$.

For a connected but not simply-connected group $G = \tilde{G}/Z$, representations of $G$ correspond to representations of $\tilde{G}$ satisfying $\rho(Z) = \mathrm{id}$.

# Prerequisites

- **Representation of a Lie group** — One side of the equivalence
- **Representation of a Lie algebra** — The other side
- **Lie group** — Must understand simply-connected vs. non-simply-connected

# Key Properties

1. Differentiation $\rho \mapsto \rho_*$ always works (group to algebra)
2. Lifting $\rho_* \mapsto \rho$ requires $G$ to be connected and simply connected
3. For non-simply-connected $G = \tilde{G}/Z$: reps of $G$ = reps of $\tilde{G}$ with $\rho(Z) = \mathrm{id}$
4. Complex representations of a real Lie algebra $\mathfrak{g}$ are equivalent to those of $\mathfrak{g}^{\mathbb{C}}$ (Lemma 4.4)

# Construction / Recognition

## To Lift a Lie Algebra Representation to a Group:
1. Verify $G$ is connected and simply connected
2. Use the exponential map: $\rho(\exp(x)) = e^{\rho_*(x)}$
3. Extend to all of $G$ by the group law

## For Non-Simply-Connected Groups:
1. Write $G = \tilde{G}/Z$ where $\tilde{G}$ is the universal cover
2. Lift the desired representation to $\tilde{G}$
3. Check whether $\rho(Z) = \mathrm{id}$; if so, it descends to $G$

# Context & Application

This theorem is the reason representation theory can often be done at the Lie algebra level, which is simpler since Lie algebras are vector spaces. It is particularly powerful for compact groups: one can study the representations of the compact group $SU(2)$ via the simpler Lie algebra $\mathfrak{sl}(2,\mathbb{C})$.

# Examples

**Example 4.5** (p. 39): The categories of representations of $SL(2, \mathbb{C})$, $SU(2)$, $\mathfrak{sl}(2, \mathbb{C})$, and $\mathfrak{su}(2)$ are all equivalent.

**Example** (p. 39): Representations of $SO(3, \mathbb{R})$ correspond to representations of $SU(2)$ (its double cover) satisfying $\rho(-I) = \mathrm{id}$. See Exercise 4.1.

# Relationships

## Builds Upon
- **Exponential map** — The mechanism for lifting algebra representations to group representations

## Enables
- **Classification of sl(2,C) representations** — Can work at algebra level and lift to group
- **Complete reducibility** — Can transfer between group and algebra settings

## Related
- **Complexification of Lie algebra** — Extends the equivalence: reps of $\mathfrak{g}$ = reps of $\mathfrak{g}^{\mathbb{C}}$

# Common Errors

- **Error**: Attempting to lift a Lie algebra representation to a non-simply-connected group without checking the kernel condition.
  **Correction**: For $G = \tilde{G}/Z$, verify $\rho(z) = \mathrm{id}$ for all $z \in Z$.

# Common Confusions

- **Confusion**: Believing the equivalence holds for infinite-dimensional representations.
  **Clarification**: This only works for finite-dimensional representations (Remark 4.6). The theory of infinite-dimensional representations of $SL(2, \mathbb{C})$ is very different from that of $SU(2)$.

# Source Reference

Chapter 4: Representations of Lie Groups and Lie Algebras, Section 4.1, Theorem 4.3, Lemma 4.4, Example 4.5, pp. 39-40.

# Verification Notes

- Definition source: Direct from Theorem 4.3, p. 39
- Confidence rationale: Explicit theorem statement with proof references
- Uncertainties: None
- Cross-reference status: Verified
