---
# === CORE IDENTIFICATION ===
concept: Adjoint Representation (Ad)
slug: adjoint-action-on-lie-algebra

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
pdf_page: 23
section: "3.3"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Ad map"
  - "adjoint representation of Lie group"
  - "$\\mathrm{Ad}: G \\to \\mathrm{GL}(\\mathfrak{g})$"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - adjoint-action-on-lie-group
  - exponential-map
extends:
  - adjoint-action-on-lie-group
related:
  - ad-map
  - commutator-bracket
contrasts_with:
  - ad-map

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a Lie algebra relate to its Lie group?"
  - "What is the exponential map?"
---

# Quick Definition

The adjoint representation $\mathrm{Ad}: G \to \mathrm{GL}(\mathfrak{g})$ is the morphism of Lie groups obtained by taking the derivative of the conjugation action at the identity. For matrix groups, $\mathrm{Ad}_g(x) = gxg^{-1}$.

# Core Definition

**Equation (3.4)** (Kirillov): $\mathrm{Ad}: G \to \mathrm{GL}(\mathfrak{g})$ is the morphism of Lie groups defined by $\mathrm{Ad}_g = (d/dt)|_{t=0} g \exp(tx) g^{-1}$.

Key relations:
- $\mathrm{Ad}(\exp x) = \exp(\mathrm{ad}\, x)$ (Lemma 3.14 part 2).
- The adjoint preserves the commutator: $\mathrm{Ad}\, g([x, y]) = [\mathrm{Ad}\, g . x, \mathrm{Ad}\, g . y]$ (Proposition 3.12).

# Prerequisites

- **Adjoint action on Lie group** — the action of $G$ on itself by conjugation
- **Exponential map** — connects $\mathrm{Ad}$ and $\mathrm{ad}$

# Key Properties

1. $\mathrm{Ad}: G \to \mathrm{GL}(\mathfrak{g})$ is a Lie group morphism (homomorphism).
2. $\mathrm{Ad}$ preserves the Lie bracket.
3. $\mathrm{Ad}(\exp x) = \exp(\mathrm{ad}\, x)$ as linear operators on $\mathfrak{g}$.
4. $X \exp(y) X^{-1} = \exp(\mathrm{Ad}\, X . y)$ (Theorem 3.7 part 5).
5. $\mathrm{Ker}(\mathrm{Ad}) = Z(G)$ for connected $G$ (Theorem 3.32).

# Construction / Recognition

## To Construct/Create:
1. For each $g \in G$, define $\mathrm{Ad}_g: \mathfrak{g} \to \mathfrak{g}$ as the derivative at $h = 1$ of $h \mapsto ghg^{-1}$.
2. For matrix groups: $\mathrm{Ad}_g(x) = gxg^{-1}$.

## To Identify/Recognize:
1. The action of $G$ on its own Lie algebra by the derivative of conjugation.

# Context & Application

The adjoint representation is the canonical representation of any Lie group. Its derivative yields the ad map and hence the Lie bracket. The kernel of Ad is the center of $G$.

# Examples

**Example** (Exercise 2.12): $\mathrm{Ad}: \mathrm{SU}(2) \to \mathrm{GL}(\mathfrak{su}(2)) \cong \mathrm{GL}(3, \mathbb{R})$ gives a morphism $\mathrm{SU}(2) \to \mathrm{SO}(3, \mathbb{R})$.

# Relationships

## Builds Upon
- **Adjoint action on Lie group** — $\mathrm{Ad}_g$ is the derivative of conjugation

## Enables
- **ad map** — $\mathrm{ad} = \mathrm{Ad}_*: \mathfrak{g} \to \mathfrak{gl}(\mathfrak{g})$
- **Center of Lie group** — $Z(G) = \mathrm{Ker}(\mathrm{Ad})$

## Related
- **Commutator bracket** — $\mathrm{Ad}$ preserves the bracket

## Contrasts With
- **ad map** — $\mathrm{Ad}$ is a group representation; $\mathrm{ad}$ is its infinitesimal (algebra) version

# Common Errors

- **Error**: Confusing $\mathrm{Ad}$ and $\mathrm{ad}$.
  **Correction**: $\mathrm{Ad}: G \to \mathrm{GL}(\mathfrak{g})$ acts by group elements; $\mathrm{ad}: \mathfrak{g} \to \mathfrak{gl}(\mathfrak{g})$ acts by algebra elements. They are related by $\mathrm{Ad}(\exp x) = \exp(\mathrm{ad}\, x)$.

# Common Confusions

- **Confusion**: Whether $\mathrm{Ad}$ is always faithful (injective).
  **Clarification**: No. $\mathrm{Ker}(\mathrm{Ad}) = Z(G)$. For example, $\mathrm{Ad}: \mathrm{SU}(2) \to \mathrm{SO}(3)$ has kernel $\{\pm I\} = Z(\mathrm{SU}(2))$.

# Source Reference

Chapter 3: Lie Groups and Lie Algebras, Section 3.3, equation (3.4), Lemma 3.14, pages 23-24.

# Verification Notes

- Definition source: Direct from equation (3.4)
- Confidence rationale: Explicit definition with key lemma
- Uncertainties: None
- Cross-reference status: Verified with Proposition 3.12, Theorem 3.32
