---
# === CORE IDENTIFICATION ===
concept: Isomorphism Preserves Inverses
slug: isomorphism-preserves-inverses

# === CLASSIFICATION ===
category: fundamentals
subcategory: isomorphism-properties
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Isomorphisms"
chapter_number: 7
pdf_page: 39
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - isomorphism
  - isomorphism-preserves-identity
extends: []
related:
  - isomorphism-preserves-order
  - isomorphism-preserves-subgroups
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What properties are preserved by isomorphisms?"
  - "Does an isomorphism send inverses to inverses?"
---

# Quick Definition

An isomorphism sends inverses to inverses: $\varphi(x^{-1}) = \varphi(x)^{-1}$ for all $x \in G$.

# Core Definition

Armstrong states: "The isomorphism $\varphi$ sends inverses to inverses in the sense that $\varphi(x)^{-1} = \varphi(x^{-1})$ for all $x \in G$" (p. 42). The proof is direct: $\varphi(x^{-1})\varphi(x) = \varphi(x^{-1}x) = \varphi(e) = e'$, and similarly $\varphi(x)\varphi(x^{-1}) = e'$, so $\varphi(x^{-1})$ is the inverse of $\varphi(x)$ in $G'$.

# Prerequisites

- **Isomorphism** — This is a property of isomorphisms
- **Isomorphism preserves identity** — Uses the fact that $\varphi(e) = e'$

# Key Properties

1. $\varphi(x^{-1}) = \varphi(x)^{-1}$ for all $x \in G$
2. This follows from the homomorphism property and identity preservation
3. Combined with identity preservation, this means $\varphi$ respects the full group structure

# Construction / Recognition

Not applicable (this is a theorem).

# Context & Application

Together with preservation of identity, this result shows that isomorphisms respect all the group operations. This is essential for establishing that isomorphic groups are truly "the same" algebraically.

# Examples

**Example**: In the isomorphism $\varphi: \mathbb{R} \to \mathbb{R}^{pos}$ via $\varphi(x) = e^x$, the inverse of $x$ in $\mathbb{R}$ is $-x$, and $\varphi(-x) = e^{-x} = (e^x)^{-1} = \varphi(x)^{-1}$.

# Relationships

## Builds Upon
- **Isomorphism** — Property of isomorphisms
- **Isomorphism preserves identity** — Used in the proof

## Related
- **Isomorphism preserves order** — Follows from inverse preservation
- **Isomorphism preserves subgroups** — Uses inverse preservation

# Common Errors

- **Error**: Writing the inverse preservation as $\varphi(x^{-1}) = \varphi^{-1}(x)$.
  **Correction**: $\varphi(x^{-1}) = \varphi(x)^{-1}$; the inverse on the left is the group inverse, while on the right it is the group inverse in $G'$, not the inverse function.

# Common Confusions

- **Confusion**: Confusing $\varphi(x)^{-1}$ (inverse of $\varphi(x)$ in $G'$) with $\varphi^{-1}(x)$ (inverse function applied to $x$).
  **Clarification**: These are different operations. The theorem is about group inverses, not function inverses.

# Source Reference

Chapter 7: Isomorphisms, page 42 (pdf p. 42).

# Verification Notes

- Proof: Direct from p. 42
- Confidence: HIGH — explicit proof in source
