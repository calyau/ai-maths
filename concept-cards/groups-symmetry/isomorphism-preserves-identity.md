---
# === CORE IDENTIFICATION ===
concept: Isomorphism Preserves Identity
slug: isomorphism-preserves-identity

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
extends: []
related:
  - isomorphism-preserves-inverses
  - isomorphism-preserves-order
  - isomorphism-preserves-subgroups
  - isomorphism-preserves-commutativity
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What properties are preserved by isomorphisms?"
  - "Does an isomorphism send the identity to the identity?"
---

# Quick Definition

An isomorphism $\varphi: G \to G'$ sends the identity element of $G$ to the identity element of $G'$: $\varphi(e_G) = e_{G'}$.

# Core Definition

Armstrong proves that an isomorphism sends the identity to the identity (p. 41). Two proofs are given. The first uses surjectivity: for any $x' \in G'$, $x'\varphi(e) = \varphi(x)\varphi(e) = \varphi(xe) = \varphi(x) = x'$, and similarly $\varphi(e)x' = x'$, so $\varphi(e)$ acts as the identity in $G'$.

The second, preferred proof uses only the homomorphism property: $\varphi(e)\varphi(e) = \varphi(ee) = \varphi(e)$, then multiply both sides by $\varphi(e)^{-1}$ to get $\varphi(e) = e'$ (p. 41).

# Prerequisites

- **Isomorphism** — This is a property of isomorphisms

# Key Properties

1. $\varphi(e_G) = e_{G'}$
2. This follows from the homomorphism property alone (bijectivity is not needed)
3. The proof is that $\varphi(e)\varphi(e) = \varphi(e)$ implies $\varphi(e) = e'$

# Construction / Recognition

Not applicable (this is a theorem, not a constructible object).

# Context & Application

This is the first of several properties showing that isomorphisms preserve group structure. Armstrong notes that the second proof is "preferable to the first one; it does not use the fact that $\varphi$ is a bijection" (p. 41), hinting that the result holds for homomorphisms more generally.

# Examples

**Example** (p. 39-40): In the isomorphism between the chessboard symmetry group and $\{1, 3, 5, 7\}$ mod 8, the identity $e$ maps to $1$ (the identity of the multiplicative group).

# Relationships

## Builds Upon
- **Isomorphism** — Property of isomorphisms

## Related
- **Isomorphism preserves inverses** — Companion result
- **Isomorphism preserves order** — Consequence
- **Isomorphism preserves commutativity** — Companion result

# Common Errors

- **Error**: Trying to prove this by checking all elements.
  **Correction**: The algebraic proof using $\varphi(e)\varphi(e) = \varphi(e)$ is clean and general.

# Common Confusions

- **Confusion**: Thinking bijectivity is needed for this result.
  **Clarification**: Armstrong explicitly notes that only the homomorphism property is needed, not bijectivity.

# Source Reference

Chapter 7: Isomorphisms, page 41 (pdf p. 41). Two proofs given.

# Verification Notes

- Proof: Both arguments direct from p. 41
- Confidence: HIGH — explicit proof in source
