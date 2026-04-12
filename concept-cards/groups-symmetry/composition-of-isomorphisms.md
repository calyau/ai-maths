---
# === CORE IDENTIFICATION ===
concept: Composition of Isomorphisms
slug: composition-of-isomorphisms

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
aliases:
  - "transitivity of isomorphism"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - isomorphism
extends: []
related:
  - isomorphic-groups
  - cayleys-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Is isomorphism transitive?"
  - "Is the composition of two isomorphisms an isomorphism?"
---

# Quick Definition

If $\varphi: G \to G'$ and $\psi: G' \to G''$ are both isomorphisms, then the composition $\psi\varphi: G \to G''$ is also an isomorphism.

# Core Definition

Armstrong states: "if $\varphi: G \to G'$ and $\psi: G' \to G''$ are both isomorphisms, then the composition $\psi\varphi: G \to G''$ is also an isomorphism" (p. 42). This establishes transitivity of the isomorphism relation.

# Prerequisites

- **Isomorphism** — The concept being composed

# Key Properties

1. The composition of two bijections is a bijection
2. $\psi\varphi(xy) = \psi(\varphi(xy)) = \psi(\varphi(x)\varphi(y)) = \psi(\varphi(x))\psi(\varphi(y))$
3. This makes isomorphism an equivalence relation (with reflexivity from the identity map and symmetry from inverse maps)

# Construction / Recognition

Not applicable (this is a theorem).

# Context & Application

This property is used in the proof of Theorem 8.2, where Cayley's theorem is strengthened: $G$ is isomorphic to $G'$ (a subgroup of $S_G$), and $S_G \cong S_n$, so composing these isomorphisms gives $G$ isomorphic to a subgroup of $S_n$.

# Examples

**Example** (p. 49): In Theorem 8.2, $G \cong G' \le S_G$ and $S_G \cong S_n$, so $G \cong G'' \le S_n$ by composition.

# Relationships

## Builds Upon
- **Isomorphism** — Composition of isomorphisms

## Related
- **Cayley's theorem** — Uses composition of isomorphisms in the proof

# Common Errors

- **Error**: Forgetting that the codomain of $\varphi$ must equal the domain of $\psi$.
  **Correction**: $\psi\varphi$ only makes sense when $\varphi: G \to G'$ and $\psi: G' \to G''$.

# Common Confusions

- **Confusion**: Thinking isomorphism is only a pairwise relation.
  **Clarification**: Because isomorphism is transitive, if $G \cong G'$ and $G' \cong G''$, then $G \cong G''$ without needing to construct a direct isomorphism.

# Source Reference

Chapter 7: Isomorphisms, page 42 (pdf p. 42). Used in Chapter 8, Theorem 8.2.

# Verification Notes

- Statement: Direct from p. 42
- Application: Theorem 8.2 on p. 49
- Confidence: HIGH — explicit statement
