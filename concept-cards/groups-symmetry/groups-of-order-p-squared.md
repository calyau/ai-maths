---
# === CORE IDENTIFICATION ===
concept: Groups of Order p-Squared
slug: groups-of-order-p-squared

# === CLASSIFICATION ===
category: group-actions
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Actions, Orbits, and Stabilizers"
chapter_number: 17
pdf_page: 98
section: "Theorem 17.5"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "classification of groups of order p^2"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - centre-of-p-group
  - direct-product
extends: []
related:
  - sylow-p-subgroup
  - classification-of-groups-of-order-12
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the groups of order p^2 for a prime p?"
---

# Quick Definition

If $p$ is prime, a group of order $p^2$ is either cyclic ($\mathbb{Z}_{p^2}$) or isomorphic to $\mathbb{Z}_p \times \mathbb{Z}_p$. There are exactly two isomorphism classes.

# Core Definition

**(17.5) Theorem.** If $p$ is prime, a group of order $p^2$ is either cyclic or isomorphic to $\mathbb{Z}_p \times \mathbb{Z}_p$ (Armstrong, p. 101).

# Prerequisites

- **Centre of p-group** -- Theorem 17.4 guarantees a non-trivial centre
- **Direct product** -- the non-cyclic case is identified as $\mathbb{Z}_p \times \mathbb{Z}_p$

# Key Properties

1. There are exactly two groups of order $p^2$ up to isomorphism
2. Both are abelian
3. The cyclic group $\mathbb{Z}_{p^2}$ has elements of order $p^2$
4. $\mathbb{Z}_p \times \mathbb{Z}_p$ has no element of order $p^2$; all non-identity elements have order $p$

# Construction / Recognition

## Proof Sketch (p. 101):
1. If $G$ has an element of order $p^2$, then $G$ is cyclic.
2. Otherwise, all non-identity elements have order $p$.
3. By Theorem 17.4, $Z(G)$ is non-trivial; choose $x \ne e$ from $Z(G)$.
4. Choose $y \notin \langle x \rangle$. The $p^2$ products $x^iy^j$ ($1 \le i, j \le p$) are distinct.
5. Since $x \in Z(G)$, $\langle x \rangle$ and $\langle y \rangle$ commute element-wise.
6. By (10.2), $G \cong \langle x \rangle \times \langle y \rangle \cong \mathbb{Z}_p \times \mathbb{Z}_p$.

# Context & Application

This classification is a first taste of the general theory of abelian groups. It shows that small prime-power order forces strong structural constraints.

# Examples

For $p = 2$: the two groups of order 4 are $\mathbb{Z}_4$ and $\mathbb{Z}_2 \times \mathbb{Z}_2$ (Klein's four-group).

For $p = 3$: the two groups of order 9 are $\mathbb{Z}_9$ and $\mathbb{Z}_3 \times \mathbb{Z}_3$.

# Relationships

## Builds Upon
- **Centre of p-group** -- the proof requires $Z(G) \ne \{e\}$

## Enables
- **Sylow theorems** -- understanding $p$-group structure is foundational

## Related
- **Classification of groups of order 12** -- a more complex classification in Chapter 20

# Common Errors

- **Error**: Forgetting to check that $\langle x \rangle \cap \langle y \rangle = \{e\}$.
  **Correction**: Since $y \notin \langle x \rangle$ and both $\langle x \rangle, \langle y \rangle$ have prime order $p$, their intersection is trivial.

# Common Confusions

- **Confusion**: Thinking there might be non-abelian groups of order $p^2$.
  **Clarification**: Both groups of order $p^2$ are abelian. The non-trivial centre forces commutativity in this case.

# Source Reference

Chapter 17: Actions, Orbits, and Stabilizers, Theorem 17.5, page 101.

# Verification Notes

- Theorem and proof: Direct from p. 101
- Confidence: HIGH -- explicitly stated theorem with complete proof
