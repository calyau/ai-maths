---
# === CORE IDENTIFICATION ===
concept: Isomorphism Preserves Subgroups
slug: isomorphism-preserves-subgroups

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
  - isomorphism-preserves-inverses
extends: []
related:
  - isomorphism-preserves-order
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What properties are preserved by isomorphisms?"
  - "Does an isomorphism send subgroups to subgroups?"
---

# Quick Definition

If $\varphi: G \to G'$ is an isomorphism and $H$ is a subgroup of $G$, then $\varphi(H)$ is a subgroup of $G'$.

# Core Definition

Armstrong proves: "If $\varphi: G \to G'$ is an isomorphism and if $H$ is a subgroup of $G$, then $\varphi(H)$ is a subgroup of $G'$" (p. 42). The proof uses the one-step subgroup test: if $x', y' \in \varphi(H)$, find $x, y \in H$ with $\varphi(x) = x'$, $\varphi(y) = y'$. Since $H$ is a subgroup, $xy^{-1} \in H$, and $\varphi(xy^{-1}) = x'(y')^{-1} \in \varphi(H)$.

# Prerequisites

- **Isomorphism** — This is a property of isomorphisms
- **Isomorphism preserves inverses** — Used in the proof to handle $y^{-1}$

# Key Properties

1. $\varphi(H) \le G'$ whenever $H \le G$
2. If $H$ is cyclic with generator $g$, then $\varphi(H)$ is cyclic with generator $\varphi(g)$
3. $H$ and $\varphi(H)$ have the same order
4. The subgroup lattices of isomorphic groups are isomorphic

# Construction / Recognition

Not applicable (this is a theorem).

# Context & Application

Subgroup preservation means that isomorphic groups have identical subgroup structures. This can be used to prove non-isomorphism: if $G$ has a subgroup of order $k$ but $G'$ does not, then $G \not\cong G'$.

# Examples

**Example** (p. 42): The rotational symmetry group of the tetrahedron ($\cong A_4$) has a subgroup isomorphic to $\{e, (12)(34), (13)(24), (14)(23)\}$ (Klein's group). Any group isomorphic to $A_4$ must also have such a subgroup.

# Relationships

## Builds Upon
- **Isomorphism** — Property of isomorphisms
- **Isomorphism preserves inverses** — Used in the proof

## Enables
- **Isomorphism preserves order** — Follows from cyclic subgroup preservation

# Common Errors

- **Error**: Assuming $\varphi(H)$ is a normal subgroup whenever $H$ is normal.
  **Correction**: This is actually true for isomorphisms (but would need separate verification for non-surjective homomorphisms).

# Common Confusions

- **Confusion**: Thinking preservation of subgroups means the subgroups are the same sets.
  **Clarification**: $H$ and $\varphi(H)$ are subgroups of different groups; they are isomorphic as groups but consist of different elements.

# Source Reference

Chapter 7: Isomorphisms, page 42 (pdf p. 42).

# Verification Notes

- Proof: Direct from p. 42
- Confidence: HIGH — explicit proof using one-step subgroup test
