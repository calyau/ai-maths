---
# === CORE IDENTIFICATION ===
concept: Correspondence Theorem
slug: correspondence-theorem

# === CLASSIFICATION ===
category: morphisms
subcategory: isomorphism-theorems
tier: intermediate

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Homomorphisms"
chapter_number: 11
pdf_page: 150
section: "The Isomorphism Theorems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "lattice isomorphism theorem"
  - "fourth isomorphism theorem"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - normal-subgroup
  - factor-group
  - canonical-homomorphism
extends: []
related:
  - first-isomorphism-theorem
  - third-isomorphism-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do subgroups of a factor group correspond to subgroups of the original group?"
---

# Quick Definition

The Correspondence Theorem establishes a one-to-one correspondence between subgroups of $G$ that contain a normal subgroup $N$ and subgroups of the factor group $G/N$, via the map $H \mapsto H/N$.

# Core Definition

**Theorem 11.13 (Correspondence Theorem)**: "Let $N$ be a normal subgroup of a group $G$. Then $H \mapsto H/N$ is a one-to-one correspondence between the set of subgroups $H$ containing $N$ and the set of subgroups of $G/N$. Furthermore, the normal subgroups of $G$ containing $N$ correspond to normal subgroups of $G/N$" (Judson, p. 150).

# Prerequisites

- **Normal subgroup** — $N$ must be normal in $G$
- **Factor group** — $G/N$ is the quotient
- **Canonical homomorphism** — The correspondence uses $\phi: G \to G/N$

# Key Properties

1. The map $H \mapsto H/N$ is a bijection between $\{H \leq G : N \subseteq H\}$ and $\{S \leq G/N\}$
2. Normal subgroups of $G$ containing $N$ correspond to normal subgroups of $G/N$
3. The inverse map sends $S \leq G/N$ to $\{g \in G : gN \in S\}$
4. The correspondence preserves containment (order-preserving)

# Context & Application

The Correspondence Theorem is essential for understanding the structure of factor groups. It tells us that the subgroup lattice of $G/N$ is isomorphic to the "upper portion" of the subgroup lattice of $G$ above $N$. This is used in the proof of the Third Isomorphism Theorem and in analyzing structure of groups via their quotients.

# Examples

**Example 1**: For $G = \mathbb{Z}$ and $N = 12\mathbb{Z}$, the subgroups of $\mathbb{Z}/12\mathbb{Z}$ correspond to the subgroups of $\mathbb{Z}$ containing $12\mathbb{Z}$: these are $\mathbb{Z}$, $2\mathbb{Z}$, $3\mathbb{Z}$, $4\mathbb{Z}$, $6\mathbb{Z}$, and $12\mathbb{Z}$.

# Relationships

## Builds Upon
- **Normal subgroup** and **Factor group** — Required for the correspondence

## Enables
- **Third isomorphism theorem** — Proved as a consequence
- **Analysis of factor groups** — Understanding subgroup structure of quotients

## Related
- **First isomorphism theorem** — Another fundamental structural theorem

# Common Confusions

- **Confusion**: Thinking all subgroups of $G$ correspond to subgroups of $G/N$
  **Clarification**: Only subgroups of $G$ that *contain* $N$ participate in the correspondence

# Source Reference

Chapter 11: Homomorphisms, Section 11.2, p. 150. Theorem 11.13.

# Verification Notes

- Definition source: Direct quote of Theorem 11.13
- Confidence: HIGH — explicitly stated theorem with proof
- Cross-reference status: Verified
