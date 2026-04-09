---
# === CORE IDENTIFICATION ===
concept: Quotient Group
slug: quotient-group

# === CLASSIFICATION ===
category: subgroup-theory
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Basic Definitions and Results"
chapter_number: 1
pdf_page: 20
section: "Kernels and quotients"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - factor group

# === TYPED RELATIONSHIPS ===
prerequisites:
  - normal-subgroup
  - left-coset
extends: []
related:
  - kernel
  - canonical-homomorphism
  - universal-property-of-quotients
  - correspondence-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a quotient group?"
  - "How do I construct a quotient group G/N?"
---

# Quick Definition

If $N \trianglelefteq G$, the quotient group $G/N$ is the set of cosets $\{aN \mid a \in G\}$ with multiplication $(aN)(bN) = (ab)N$. The natural map $a \mapsto aN$ is a surjective homomorphism with kernel $N$.

# Core Definition

"If $N$ is a normal subgroup of $G$, then there is a unique group structure on the set $G/N$ of cosets of $N$ in $G$ for which the natural map $a \mapsto [a]: G \to G/N$ is a homomorphism." (Milne, Proposition 1.42, p. 20)

"The group $G/N$ is called the **quotient** of $G$ by $N$." (p. 21)

# Prerequisites

- **Normal subgroup** — $N$ must be normal for the quotient to be well-defined
- **Left coset** — elements of $G/N$ are cosets

# Key Properties

1. Elements of $G/N$ are cosets $aN$
2. Multiplication: $(aN)(bN) = (ab)N$ (well-defined because $N$ is normal)
3. Identity: $N$ (the coset $eN$)
4. Inverse: $(aN)^{-1} = a^{-1}N$
5. $|G/N| = (G : N) = |G|/|N|$ when $G$ is finite
6. The map $g \mapsto gN$ is a surjective homomorphism with kernel $N$

# Construction / Recognition

## To Construct $G/N$:
1. Verify $N \trianglelefteq G$
2. Form the set of cosets $\{aN \mid a \in G\}$
3. Define $(aN)(bN) = (ab)N$
4. Well-definedness: if $aN = a'N$ and $bN = b'N$, then $abN = a'b'N$ (uses normality)

## Well-Definedness Check (from proof):
$abN = a(bN) = a(b'N) \stackrel{1.34}{=} aNb' = a'Nb' \stackrel{1.34}{=} a'b'N$

# Context & Application

Quotient groups are one of the most important constructions in algebra. They "collapse" a normal subgroup to the identity, simplifying the group. Every surjective homomorphism is essentially a quotient map.

# Examples

**Example 1** (p. 21): $\mathbb{Z}/m\mathbb{Z}$ is a cyclic group of order $m$.

**Example 2** (p. 21): For a line $L$ through the origin in $\mathbb{R}^2$, the quotient $\mathbb{R}^2/L \cong \mathbb{R}$.

**Example 3** (p. 21): $D_n/\langle r \rangle = \{\bar{e}, \bar{s}\}$ (cyclic group of order 2).

# Relationships

## Builds Upon
- **normal-subgroup** — quotients require normal subgroups
- **left-coset** — elements of the quotient are cosets

## Enables
- **factorization-theorem** — every homomorphism factors through a quotient
- **correspondence-theorem** — subgroups of quotients correspond to subgroups above the kernel
- **isomorphism-theorem** — relates quotients of quotients

## Related
- **canonical-homomorphism** — the natural map $G \to G/N$
- **kernel** — the kernel of the canonical map is $N$

# Common Errors

- **Error**: Trying to form $G/H$ when $H$ is not normal
  **Correction**: The coset multiplication $(aH)(bH) = (ab)H$ is well-defined only when $H \trianglelefteq G$

# Common Confusions

- **Confusion**: Thinking elements of $G/N$ are elements of $G$
  **Clarification**: Elements of $G/N$ are *cosets* (subsets of $G$), not individual elements. The coset $aN$ represents the equivalence class of $a$

- **Confusion**: "Factor group" vs "quotient group"
  **Clarification**: Milne notes "some authors say 'factor' instead of 'quotient', but this can be confused with 'direct factor'" (footnote 7, p. 21)

# Source Reference

Chapter 1, Proposition 1.42, Examples 1.44, pages 20-21.

# Verification Notes

- Definition source: Direct from Proposition 1.42
- Confidence: HIGH — explicit definition with full proof
- Cross-reference status: Verified
- Uncertainties: None
