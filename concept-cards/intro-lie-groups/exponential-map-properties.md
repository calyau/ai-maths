---
# === CORE IDENTIFICATION ===
concept: Properties of the Exponential Map
slug: exponential-map-properties

# === CLASSIFICATION ===
category: lie-algebras
subcategory: exponential-map
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups and Lie Algebras"
chapter_number: 3
pdf_page: 21
section: "3.1"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Theorem 3.7"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - exponential-map
extends:
  - exponential-map
related:
  - adjoint-action-on-lie-algebra
  - lie-group-morphism
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I use the exponential map to go between Lie group and Lie algebra?"
  - "How does a Lie algebra relate to its Lie group?"
---

# Quick Definition

Theorem 3.7 collects the key properties of the exponential map: it is a local diffeomorphism, it commutes with morphisms, and it intertwines the adjoint actions.

# Core Definition

**Theorem 3.7** (Kirillov):
1. $\exp(x) = 1 + x + \ldots$ (i.e., $\exp(0) = 1$ and $\exp_*(0) = \mathrm{id}$).
2. $\exp$ is a diffeomorphism of some neighborhood of $0 \in \mathfrak{g}$ with a neighborhood of $1 \in G$.
3. $\exp((t+s)x) = \exp(tx)\exp(sx)$.
4. For any morphism $\varphi: G_1 \to G_2$: $\exp(\varphi_*(x)) = \varphi(\exp(x))$.
5. $X\exp(y)X^{-1} = \exp(\mathrm{Ad}\, X . y)$.

# Prerequisites

- **Exponential map** — the map whose properties are stated

# Key Properties

1. Property (2) gives local coordinates (logarithmic coordinates) near $1 \in G$.
2. Property (4) — naturality — is the single most useful property; it says exp commutes with any Lie group morphism.
3. Property (5) is a special case of (4) applied to conjugation.
4. Notable absence: no analog of $\exp(x)\exp(y) = \exp(x+y)$ when $[x,y] \neq 0$.

# Construction / Recognition

## To Construct/Create:
Not applicable (this is a theorem about properties).

## To Identify/Recognize:
1. These properties are used whenever one needs to move between group and algebra.

# Context & Application

These properties are the workhorse of the Lie group-Lie algebra correspondence. Property (4) is especially important: it says any commutative diagram at the algebra level lifts to the group level via exp.

# Examples

**Example** (p. 22): Proposition 3.9 uses property (4) to show that for connected $G_1$, a morphism $\varphi$ is uniquely determined by $\varphi_*$. Since $\varphi_*$ determines $\varphi$ on a neighborhood of $1$ (via exp), and neighborhoods generate connected groups, $\varphi$ is determined everywhere.

# Relationships

## Builds Upon
- **Exponential map** — the map being characterized

## Enables
- **Uniqueness of morphisms** — connected group morphisms are determined by their derivatives
- **Commutator bracket** — arises from higher-order terms of the group law in logarithmic coordinates

## Related
- **Adjoint action on Lie algebra** — property (5) connects Ad to exp

# Common Errors

- **Error**: Assuming property (4) holds for smooth maps that are not group morphisms.
  **Correction**: The naturality $\exp(\varphi_*(x)) = \varphi(\exp(x))$ requires $\varphi$ to be a Lie group morphism.

# Common Confusions

- **Confusion**: Whether "local diffeomorphism" means globally injective.
  **Clarification**: No. The exponential map is only locally injective near $0$. For example, $\exp: \mathfrak{u}(1) \to U(1)$ is $a \mapsto e^{2\pi i a}$, which is periodic.

# Source Reference

Chapter 3: Lie Groups and Lie Algebras, Section 3.1, Theorem 3.7, pages 21-22.

# Verification Notes

- Definition source: Direct from Theorem 3.7
- Confidence rationale: Central theorem stated explicitly
- Uncertainties: None
- Cross-reference status: Verified with Proposition 3.9, Example 3.10
