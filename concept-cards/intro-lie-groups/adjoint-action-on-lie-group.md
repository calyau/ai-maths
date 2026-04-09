---
# === CORE IDENTIFICATION ===
concept: Adjoint Action on a Lie Group
slug: adjoint-action-on-lie-group

# === CLASSIFICATION ===
category: lie-groups
subcategory: group-actions
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups: Basic Definitions"
chapter_number: 2
pdf_page: 13
section: "2.4"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "conjugation action"
  - "$\\mathrm{Ad}_g$"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-group
  - left-action
  - right-action
extends: []
related:
  - adjoint-action-on-lie-algebra
  - ad-map
  - bi-invariant-vector-field
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the exponential map?"
  - "How does a Lie algebra relate to its Lie group?"
---

# Quick Definition

The adjoint action of $G$ on itself is conjugation: $\mathrm{Ad}_g(h) = ghg^{-1}$. Since it fixes the identity, it induces an action on $T_1G = \mathfrak{g}$, also denoted $\mathrm{Ad}_g: \mathfrak{g} \to \mathfrak{g}$.

# Core Definition

(Kirillov, p. 13-14): Adjoint action: $\mathrm{Ad}_g: G \to G$ is defined by $\mathrm{Ad}_g(h) = ghg^{-1}$. One has $\mathrm{Ad}_g = L_g R_g$.

Since the adjoint action preserves the identity $1 \in G$, it also defines an action on the tangent space:
$$\mathrm{Ad}\, g: T_1G \to T_1G.$$

# Prerequisites

- **Lie group** — the group acting on itself
- **Left action** — $\mathrm{Ad}_g = L_g \circ R_g$
- **Right action** — $\mathrm{Ad}_g = L_g \circ R_g$

# Key Properties

1. $\mathrm{Ad}: G \to \mathrm{GL}(\mathfrak{g})$ is a morphism of Lie groups (equation 3.4).
2. For matrix groups, $\mathrm{Ad}_g(v) = gvg^{-1}$ (Exercise 2.6).
3. $X \exp(y) X^{-1} = \exp(\mathrm{Ad}\, X . y)$ (Theorem 3.7 part 5).
4. $\mathrm{Ad}(\exp x) = \exp(\mathrm{ad}\, x)$ (Lemma 3.14).

# Construction / Recognition

## To Construct/Create:
1. For $g \in G$, define $\mathrm{Ad}_g: G \to G$ by $h \mapsto ghg^{-1}$.
2. Take the derivative at $h = 1$ to get $\mathrm{Ad}_g: \mathfrak{g} \to \mathfrak{g}$.

## To Identify/Recognize:
1. An action of $G$ on itself or on $\mathfrak{g}$ by conjugation.

# Context & Application

The adjoint action is central to the entire theory. It connects the group to its Lie algebra, gives rise to the adjoint representation, and its derivative yields the Lie bracket (ad map).

# Examples

**Example** (Exercise 2.12, p. 18): The adjoint action of $\mathrm{SU}(2)$ on $\mathfrak{su}(2) \cong \mathbb{R}^3$ gives a morphism $\mathrm{SU}(2) \to \mathrm{SO}(3, \mathbb{R})$.

# Relationships

## Builds Upon
- **Left action** and **Right action** — $\mathrm{Ad}_g = L_g R_g$

## Enables
- **Adjoint action on Lie algebra** — the derivative $\mathrm{Ad}_*$ at identity is the ad map
- **Bi-invariant vector field** — invariant under adjoint action (Theorem 2.26)
- **Center of Lie group** — $Z(G) = \mathrm{Ker}(\mathrm{Ad})$ (Theorem 3.32)

## Related
- **ad map** — the infinitesimal version of Ad

# Common Errors

- **Error**: Confusing $\mathrm{Ad}$ (the action on $\mathfrak{g}$) with $\mathrm{ad}$ (the derivative of $\mathrm{Ad}$).
  **Correction**: $\mathrm{Ad}: G \to \mathrm{GL}(\mathfrak{g})$ is a group representation; $\mathrm{ad} = \mathrm{Ad}_*: \mathfrak{g} \to \mathfrak{gl}(\mathfrak{g})$ is its derivative.

# Common Confusions

- **Confusion**: Whether the adjoint action on $G$ (by conjugation) and on $\mathfrak{g}$ (by $\mathrm{Ad}_g$) are the same thing.
  **Clarification**: They are related but different. The action on $\mathfrak{g}$ is obtained by differentiating the conjugation action at the identity.

# Source Reference

Chapter 2: Lie Groups: Basic Definitions, Section 2.4, pages 13-14. Equation (2.3).

# Verification Notes

- Definition source: Direct from source
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified with Theorem 3.7, Lemma 3.14, Theorem 3.32
