---
# === CORE IDENTIFICATION ===
concept: Torsion-Free Arithmetic Group
slug: torsion-free-arithmetic-group

# === CLASSIFICATION ===
category: arithmetic-groups
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Arithmetic Subgroups"
chapter_number: 7
pdf_page: 402
section: "Torsion-free arithmetic groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - arithmetic-subgroup
  - principal-congruence-subgroup
extends:
  - arithmetic-subgroup
related:
  - discrete-subgroup-of-lie-group
  - connected-shimura-variety
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do arithmetic subgroups relate to discrete subgroups of Lie groups?"
---

# Quick Definition

Every arithmetic group contains a torsion-free subgroup of finite index. Specifically, the principal congruence subgroup $\Gamma(p)$ of $\mathrm{GL}_n(\mathbb{Z})$ is torsion-free for any prime $p \geq 3$.

# Core Definition

"Every arithmetic group contains a torsion-free subgroup of finite index." (Theorem 8.1, Milne, p. 402)

The key ingredient is Lemma 8.2: "For any prime $p \geq 3$, the subgroup $\Gamma(p)$ of $\mathrm{GL}_n(\mathbb{Z})$ is torsion-free." The proof shows that $(I + p^m A)^\ell = I$ leads to a contradiction by comparing $p$-adic valuations.

# Prerequisites

- **Arithmetic subgroup** — torsion-freeness is a property of arithmetic subgroups
- **Principal congruence subgroup** — $\Gamma(p)$ provides the torsion-free subgroup

# Key Properties

1. $\Gamma(p)$ is torsion-free for primes $p \geq 3$ (Lemma 8.2)
2. $\Gamma(2)$ is *not* torsion-free: $-I \in \Gamma(2)$ has order 2
3. Every arithmetic group has a torsion-free subgroup of finite index
4. Torsion-free arithmetic subgroups act freely on symmetric spaces

# Construction / Recognition

## To Construct a Torsion-Free Arithmetic Group:
1. Start with any arithmetic subgroup $\Gamma$
2. Choose a prime $p \geq 3$
3. Take $\Gamma' = \Gamma \cap \Gamma(p)$, which is torsion-free and of finite index in $\Gamma$

## To Recognize:
1. Check that no element of $\Gamma$ (other than the identity) has finite order

# Context & Application

Torsion-free arithmetic groups are needed to construct smooth locally symmetric manifolds. If $\Gamma$ has torsion, the quotient $\Gamma \backslash G(\mathbb{R})/K$ may have singularities (orbifold points). Passing to a torsion-free subgroup of finite index resolves these singularities.

# Examples

**Example 1** (p. 402): $\mathrm{SL}_2(\mathbb{Z})$ is *not* torsion-free: $\begin{pmatrix} 0 & -1 \\ 1 & 0\end{pmatrix}$ has order 4, and $\begin{pmatrix} 0 & -1 \\ 1 & 1\end{pmatrix}$ has order 6.

**Example 2** (p. 402): $\Gamma(3) = \ker(\mathrm{GL}_n(\mathbb{Z}) \to \mathrm{GL}_n(\mathbb{Z}/3\mathbb{Z}))$ is torsion-free.

# Relationships

## Builds Upon
- **Arithmetic subgroup** — torsion-free arithmetic groups are a subclass
- **Principal congruence subgroup** — $\Gamma(p)$ provides examples

## Enables
- **Connected Shimura variety** — requires torsion-free $\Gamma$ for smooth quotients
- **Discrete subgroup of Lie group** — torsion-free ensures free action

# Common Errors

- **Error**: Taking $\Gamma(2)$ as a torsion-free subgroup
  **Correction**: $\Gamma(2)$ contains $-I$ which has order 2; use $p \geq 3$

# Common Confusions

- **Confusion**: Thinking $\mathrm{SL}_2(\mathbb{Z})$ is torsion-free because it is infinite
  **Clarification**: Infinite groups can have elements of finite order; $\mathrm{SL}_2(\mathbb{Z})$ has elements of orders 2, 4, and 6

# Source Reference

Chapter VII: Arithmetic Subgroups, Section 8, pages 402-403. Theorem 8.1, Lemma 8.2.

# Verification Notes

- Definition source: Theorem 8.1 directly stated on p. 402
- Confidence: HIGH — explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
