---
# === CORE IDENTIFICATION ===
concept: Adjoint Action on Universal Enveloping Algebra
slug: adjoint-action-on-enveloping-algebra

# === CLASSIFICATION ===
category: enveloping-algebras
subcategory: universal-enveloping-algebra
tier: advanced

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of Lie Groups and Lie Algebras"
chapter_number: 4
pdf_page: 52
section: "4.8 Universal enveloping algebra"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - universal-enveloping-algebra
  - adjoint-representation-of-lie-group
extends:
  - adjoint-representation-of-lie-group
related:
  - casimir-operator
  - center-of-enveloping-algebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the adjoint action extend to the universal enveloping algebra?"
---

# Quick Definition

The adjoint action of $\mathfrak{g}$ extends to $U\mathfrak{g}$ by $\mathrm{ad}\, x \cdot a = xa - ax$ and satisfies the Leibniz rule. The center of $U\mathfrak{g}$ consists precisely of the elements invariant under this adjoint action.

# Core Definition

**Proposition 4.56** (Kirillov, pp. 52-53):

1. The adjoint action of $\mathfrak{g}$ on $\mathfrak{g}$ extends uniquely to an action on $U\mathfrak{g}$ satisfying the Leibniz rule: $\mathrm{ad}\, x \cdot (ab) = (\mathrm{ad}\, x \cdot a)b + a(\mathrm{ad}\, x \cdot b)$. Moreover, $\mathrm{ad}\, x \cdot a = xa - ax$.
2. The center $Z\mathfrak{g} = Z(U\mathfrak{g})$ coincides with the space of invariants: $Z\mathfrak{g} = (U\mathfrak{g})^{\mathrm{ad}\,\mathfrak{g}}$.

# Prerequisites

- **Universal enveloping algebra** — The algebra on which the action is defined
- **Adjoint representation** — Being extended from $\mathfrak{g}$ to $U\mathfrak{g}$

# Key Properties

1. $\mathrm{ad}\, x \cdot a = xa - ax$ (commutator in $U\mathfrak{g}$)
2. Satisfies Leibniz rule: derivation of the algebra $U\mathfrak{g}$
3. $C$ is central iff $\mathrm{ad}\, x \cdot C = 0$ for all $x \in \mathfrak{g}$

# Context & Application

This provides the conceptual framework for understanding the Casimir operator: it is central because it is $\mathrm{ad}$-invariant. The center of $U\mathfrak{g}$ plays a crucial role in representation theory.

# Examples

**Example** (p. 52): The Casimir element $C = ef + fe + \frac{1}{2}h^2$ is invariant under $\mathrm{ad}\, e$, $\mathrm{ad}\, f$, $\mathrm{ad}\, h$, hence central.

# Relationships

## Builds Upon
- **Adjoint representation** — Extended from $\mathfrak{g}$ to $U\mathfrak{g}$

## Enables
- **Center of $U\mathfrak{g}$** — Characterized as $\mathrm{ad}$-invariant elements

# Source Reference

Chapter 4, Section 4.8, Proposition 4.56, pp. 52-53.

# Verification Notes

- Definition source: Direct from Proposition 4.56
- Confidence rationale: Explicit proposition with proof
- Uncertainties: None
- Cross-reference status: Verified
