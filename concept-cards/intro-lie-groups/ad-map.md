---
# === CORE IDENTIFICATION ===
concept: ad Map
slug: ad-map

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
aliases:
  - "adjoint representation of Lie algebra"
  - "$\\mathrm{ad}: \\mathfrak{g} \\to \\mathfrak{gl}(\\mathfrak{g})$"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - adjoint-action-on-lie-algebra
  - commutator-bracket
extends:
  - adjoint-action-on-lie-algebra
related:
  - jacobi-identity
  - lie-algebra
contrasts_with:
  - adjoint-action-on-lie-algebra

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Lie algebra?"
  - "How does a Lie algebra relate to its Lie group?"
---

# Quick Definition

The ad map $\mathrm{ad}: \mathfrak{g} \to \mathfrak{gl}(\mathfrak{g})$ is the derivative of the adjoint representation $\mathrm{Ad}$, satisfying $\mathrm{ad}\, x . y = [x, y]$.

# Core Definition

**Lemma 3.14** (Kirillov): Denote by $\mathrm{ad} = \mathrm{Ad}_*: \mathfrak{g} \to \mathfrak{gl}(\mathfrak{g})$ the map of Lie algebras corresponding to $\mathrm{Ad}: G \to \mathrm{GL}(\mathfrak{g})$. Then:
1. $\mathrm{ad}\, x . y = [x, y]$
2. $\mathrm{Ad}(\exp x) = \exp(\mathrm{ad}\, x)$ as operators $\mathfrak{g} \to \mathfrak{g}$.

# Prerequisites

- **Adjoint representation (Ad)** — the ad map is its derivative
- **Commutator bracket** — $\mathrm{ad}\, x . y = [x, y]$

# Key Properties

1. $\mathrm{ad}\, x$ is a derivation of $\mathfrak{g}$: $\mathrm{ad}\, x . [y, z] = [\mathrm{ad}\, x . y, z] + [y, \mathrm{ad}\, x . z]$ (Jacobi identity).
2. $\mathrm{ad}[x, y] = \mathrm{ad}\, x \circ \mathrm{ad}\, y - \mathrm{ad}\, y \circ \mathrm{ad}\, x$ (i.e., ad is a Lie algebra morphism).
3. $\mathrm{Ker}(\mathrm{ad}) = \mathfrak{z}(\mathfrak{g})$ (center of the Lie algebra).
4. If $\mathfrak{g}$ has trivial center, $\mathrm{ad}$ is injective, giving an embedding $\mathfrak{g} \hookrightarrow \mathfrak{gl}(\mathfrak{g})$.

# Construction / Recognition

## To Construct/Create:
1. For each $x \in \mathfrak{g}$, define $\mathrm{ad}\, x: \mathfrak{g} \to \mathfrak{g}$ by $\mathrm{ad}\, x . y = [x, y]$.

## To Identify/Recognize:
1. The linear map sending $x$ to the operator "bracket with $x$."

# Context & Application

The ad map is used to prove the Jacobi identity, to define the Killing form (later chapters), and to provide the connection between the Lie bracket and the group adjoint action.

# Examples

**Example** (p. 24): The Jacobi identity $[x, [y, z]] = [[x,y], z] + [y, [x,z]]$ is equivalent to $\mathrm{ad}[x, y] = [\mathrm{ad}\, x, \mathrm{ad}\, y]$ (where the bracket on the right is the commutator in $\mathfrak{gl}(\mathfrak{g})$).

**Example** (p. 33): If $\mathfrak{g}$ has no center, then $x \mapsto \mathrm{ad}\, x$ embeds $\mathfrak{g}$ into $\mathfrak{gl}(\mathfrak{g})$ (used in the proof of Lie's third theorem).

# Relationships

## Builds Upon
- **Adjoint representation (Ad)** — $\mathrm{ad} = \mathrm{Ad}_*$
- **Commutator bracket** — $\mathrm{ad}\, x . y = [x, y]$

## Enables
- **Jacobi identity** — equivalent to $\mathrm{ad}$ being a Lie algebra morphism
- **Killing form** — defined using ad (later chapters)
- **Lie's third theorem** — for centerless algebras, ad embeds $\mathfrak{g}$ in $\mathfrak{gl}(\mathfrak{g})$

## Related
- **Derivation of a Lie algebra** — $\mathrm{ad}\, x$ is an inner derivation

## Contrasts With
- **Adjoint representation (Ad)** — Ad is a group homomorphism; ad is an algebra homomorphism

# Common Errors

- **Error**: Writing $\mathrm{ad}(x)(y) = yx - xy$ (wrong sign for non-matrix algebras).
  **Correction**: $\mathrm{ad}\, x . y = [x, y]$. For matrices, this is $xy - yx$ (not $yx - xy$).

# Common Confusions

- **Confusion**: Whether ad and Ad carry the same information.
  **Clarification**: Ad determines ad (by differentiation). For connected groups, ad determines Ad locally (via $\mathrm{Ad}(\exp x) = \exp(\mathrm{ad}\, x)$).

# Source Reference

Chapter 3: Lie Groups and Lie Algebras, Section 3.3, Lemma 3.14, pages 23-24.

# Verification Notes

- Definition source: Direct from Lemma 3.14
- Confidence rationale: Explicit lemma with proof
- Uncertainties: None
- Cross-reference status: Verified with Theorem 3.15, Definition 3.16
