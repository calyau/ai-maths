---
# === CORE IDENTIFICATION ===
concept: Proving Non-Isomorphism
slug: isomorphism-not-isomorphism

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
  - "non-isomorphism techniques"
  - "proving groups are not isomorphic"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - isomorphism
  - isomorphism-preserves-commutativity
  - isomorphism-preserves-order
extends: []
related:
  - isomorphic-groups
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I determine whether two groups are isomorphic?"
  - "How do I show two groups are not isomorphic?"
---

# Quick Definition

To show two groups are not isomorphic, find a group-theoretic invariant that differs between them: group order, abelianness, element orders, or subgroup structure.

# Core Definition

Armstrong demonstrates several techniques for proving non-isomorphism in Chapter 7. Since an isomorphism preserves all group-theoretic properties, finding any property that differs between two groups proves they cannot be isomorphic. Armstrong uses three main invariants:

1. **Abelianness**: "$\mathbb{Z}_{12}$ is the only one which is abelian, so it cannot be isomorphic to either of the other two" ($D_6$ and $A_4$) (p. 42).
2. **Element orders**: "$D_6$, unlike $A_4$, contains an element of order six, so $D_6$ cannot be isomorphic to $A_4$" (p. 42).
3. **Algebraic structure**: $\mathbb{Q} \not\cong \mathbb{Q}^{pos}$ because an isomorphism would require $\sqrt{2} \in \mathbb{Q}$ (p. 41).

# Prerequisites

- **Isomorphism** — Understanding what is preserved
- **Isomorphism preserves commutativity** — Abelianness as invariant
- **Isomorphism preserves order** — Element orders as invariant

# Key Properties

1. If $|G| \ne |G'|$, then $G \not\cong G'$
2. If $G$ is abelian and $G'$ is not, then $G \not\cong G'$
3. If $G$ has an element of order $k$ but $G'$ does not, then $G \not\cong G'$
4. If $G$ has a subgroup of order $k$ but $G'$ does not, then $G \not\cong G'$
5. If $G$ is cyclic and $G'$ is not, then $G \not\cong G'$

# Construction / Recognition

## Strategy for Proving Non-Isomorphism:
1. Compare orders — quick and easy
2. Compare abelianness — next easiest check
3. Compare element orders — list the orders of all elements
4. Compare subgroup structure — count subgroups of each order
5. Use specific structural arguments (as for $\mathbb{Q} \not\cong \mathbb{Q}^{pos}$)

# Context & Application

Proving non-isomorphism is as important as proving isomorphism. Armstrong's Chapter 7 provides the toolkit: he distinguishes three groups of order 12 ($\mathbb{Z}_{12}$, $D_6$, $A_4$) that are pairwise non-isomorphic, using different invariants for each pair.

# Examples

**Example** (p. 42): Distinguishing $\mathbb{Z}_{12}$, $D_6$, $A_4$:
- $\mathbb{Z}_{12}$ is abelian; $D_6$ and $A_4$ are not. So $\mathbb{Z}_{12}$ differs from both.
- $D_6$ has an element of order 6; $A_4$ does not (max order 3). So $D_6 \ne A_4$.

**Example** (p. 41): $\mathbb{Q} \not\cong \mathbb{Q}^{pos}$ because $\varphi(x/2)$ must be $\sqrt{2} \notin \mathbb{Q}$.

# Relationships

## Builds Upon
- **Isomorphism** — Non-isomorphism is its negation
- **Isomorphism preserves commutativity** — Abelianness test
- **Isomorphism preserves order** — Element order test

## Related
- **Isomorphic groups** — The concept whose negation is studied

# Common Errors

- **Error**: Trying to prove non-isomorphism by failing to find an isomorphism.
  **Correction**: You must find an invariant that differs. Failing to construct an isomorphism does not prove one doesn't exist.

# Common Confusions

- **Confusion**: Thinking that matching element orders proves isomorphism.
  **Clarification**: Matching element orders is necessary but not sufficient. For example, groups can have the same multiset of element orders but different subgroup structures.

# Source Reference

Chapter 7: Isomorphisms, pages 41-42 (pdf pp. 41-42). Examples of non-isomorphism.

# Verification Notes

- Techniques: All from pp. 41-42
- Examples: Directly from source
- Confidence: HIGH — multiple worked examples
