---
# === CORE IDENTIFICATION ===
concept: Adjoint Representation
slug: adjoint-representation-of-lie-group

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
  - "adjoint action on the Lie algebra"
  - "Ad representation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - representation-of-lie-group
  - lie-algebra
  - adjoint-action
extends:
  - adjoint-action
related:
  - casimir-operator
  - invariant-bilinear-form
contrasts_with:
  - trivial-representation

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes the adjoint representation from other representations?"
  - "How does a Lie group act on its own Lie algebra?"
---

# Quick Definition

The adjoint representation is the natural representation of a Lie group $G$ on its own Lie algebra $\mathfrak{g}$, where $g \in G$ acts by $\mathrm{Ad}\, g$, and equivalently $x \in \mathfrak{g}$ acts by $\mathrm{ad}\, x = [x, \cdot]$.

# Core Definition

**Example 4.8** (Kirillov, p. 39): Adjoint representation: $V = \mathfrak{g}$, $\rho(g) = \mathrm{Ad}\, g$ for the Lie group (respectively, $\rho(x) = \mathrm{ad}\, x$ for the Lie algebra). Here $\mathrm{Ad}$ and $\mathrm{ad}$ are defined in (2.3) and Lemma 3.14.

At the group level, $\mathrm{Ad}(g)(x) = gxg^{-1}$ (conjugation in matrix groups). At the Lie algebra level, $\mathrm{ad}(x)(y) = [x, y]$.

# Prerequisites

- **Representation of a Lie group** — The adjoint representation is an instance
- **Lie algebra** — The vector space on which the representation acts
- **Adjoint action** — The specific action $\mathrm{Ad}$/$\mathrm{ad}$ used

# Key Properties

1. The representation space is $\mathfrak{g}$ itself, so $\dim V = \dim \mathfrak{g}$
2. At the group level: $\rho(g) = \mathrm{Ad}(g)$, i.e., conjugation
3. At the algebra level: $\rho(x) = \mathrm{ad}(x) = [x, \cdot]$
4. Invariant elements under the adjoint action are central elements of $\mathfrak{g}$
5. Invariant bilinear forms on $\mathfrak{g}$ (e.g., the Killing form) are precisely those satisfying $B([x,y],z) + B(y,[x,z]) = 0$
6. For $\mathfrak{sl}(2,\mathbb{C})$, the adjoint representation is isomorphic to the symmetric square $S^2\mathbb{C}^2$ (Exercise 4.2)

# Construction / Recognition

## To Construct:
1. Take $V = \mathfrak{g}$
2. Define $\rho(g)(x) = gxg^{-1}$ for matrix groups
3. The corresponding Lie algebra action is $\rho(x)(y) = [x,y]$

## To Identify/Recognize:
1. Check that the representation space is the Lie algebra itself
2. Check that the action is by conjugation (group) or commutator (algebra)

# Context & Application

The adjoint representation is canonical: it exists for every Lie group without additional choices. It encodes the internal symmetry structure of the Lie algebra. The Killing form, defined via the adjoint representation, is the key tool for classifying semisimple Lie algebras. The Casimir element is constructed using the adjoint representation and an invariant bilinear form.

# Examples

**Example 4.8** (p. 39): For any Lie group $G$, $V = \mathfrak{g}$ with $\rho(g) = \mathrm{Ad}\, g$ is the adjoint representation.

**Exercise 4.2** (p. 55): The adjoint representation of $\mathfrak{sl}(2,\mathbb{C})$ (which is 3-dimensional) is isomorphic to $S^2\mathbb{C}^2$, the symmetric square of the standard representation.

# Relationships

## Builds Upon
- **Adjoint action** — The adjoint representation is this action viewed as a representation
- **Lie algebra** — The representation space

## Enables
- **Casimir operator** — Constructed via the adjoint representation and an invariant form
- **Killing form** — Defined as $B(x,y) = \mathrm{tr}(\mathrm{ad}\, x \circ \mathrm{ad}\, y)$

## Related
- **Invariant bilinear form** — G-invariant forms on $\mathfrak{g}$ relate to the adjoint representation

## Contrasts With
- **Trivial representation** — The adjoint representation is non-trivial for non-abelian groups

# Common Errors

- **Error**: Confusing the adjoint action $\mathrm{Ad}$ (group on algebra) with the coadjoint action (group on dual of algebra).
  **Correction**: The adjoint representation acts on $\mathfrak{g}$; the coadjoint acts on $\mathfrak{g}^*$.

# Common Confusions

- **Confusion**: Thinking the adjoint representation is always irreducible.
  **Clarification**: The adjoint representation is irreducible only for simple Lie algebras. For semisimple algebras with multiple simple factors, it decomposes.

# Source Reference

Chapter 4: Representations of Lie Groups and Lie Algebras, Section 4.1, Example 4.8, p. 39.

# Verification Notes

- Definition source: Direct from Example 4.8, p. 39
- Confidence rationale: Explicit example with clear references to earlier definitions
- Uncertainties: None
- Cross-reference status: Verified
