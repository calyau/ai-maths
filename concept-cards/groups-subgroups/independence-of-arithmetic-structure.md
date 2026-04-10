---
# === CORE IDENTIFICATION ===
concept: Independence of Arithmetic Structure
slug: independence-of-arithmetic-structure

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
pdf_page: 399
section: "Independence of ρ and L"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - arithmetic-subgroup
  - principal-congruence-subgroup
extends: []
related:
  - congruence-subgroup
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an arithmetic subgroup?"
---

# Quick Definition

The notions of arithmetic subgroup and congruence subgroup of $G(\mathbb{Q})$ are independent of the choice of faithful representation $\rho: G \to \mathrm{GL}_V$ and lattice $L \subset V$ used in the definitions.

# Core Definition

Proposition 4.2 (Milne, p. 399): "For any faithful representations $G \to \mathrm{GL}_V$ and $G \to \mathrm{GL}_{V'}$ of $G$ and lattices $L$ and $L'$ in $V$ and $V'$, $G(\mathbb{Q})_L$ and $G(\mathbb{Q})_{L'}$ are commensurable."

The key lemma (4.1): for any representation $\rho: G \to \mathrm{GL}_V$ and lattice $L \subset V$, there exists a congruence subgroup of $G(\mathbb{Q})$ leaving $L$ stable. This is proved by showing that the polynomial expressions for $\rho(g)$ are integral for $g \equiv I \bmod m$ with sufficiently large $m$.

# Prerequisites

- **Arithmetic subgroup** — the concept whose independence is being proved
- **Principal congruence subgroup** — used in the proof

# Key Properties

1. $G(\mathbb{Q})_L$ and $G(\mathbb{Q})_{L'}$ are commensurable for any two faithful representations and lattices
2. The set of arithmetic subgroups is an intrinsic invariant of $G$
3. The set of congruence subgroups is also independent of choices
4. For any $N$, there exists $m$ such that $\Gamma(Nm) \subset \Gamma_L(N)$ for any lattice $L$

# Construction / Recognition

## The Independence Proof:
1. By Lemma 4.1, for representation $\rho'$ and lattice $L'$, some congruence subgroup $\Gamma$ of $(G, \rho, L)$ stabilizes $L'$
2. Hence $\Gamma \subset G(\mathbb{Q})_L \cap G(\mathbb{Q})_{L'}$
3. Since $\Gamma$ has finite index in $G(\mathbb{Q})_L$, we get $(G(\mathbb{Q})_L : G(\mathbb{Q})_L \cap G(\mathbb{Q})_{L'}) < \infty$
4. By symmetry, the same holds with $L$ and $L'$ swapped

# Context & Application

This independence result is essential: without it, the theory of arithmetic subgroups would depend on arbitrary choices and would not be intrinsic to the algebraic group $G$. It allows us to speak of "the arithmetic subgroups of $G(\mathbb{Q})$" without specifying a representation.

# Examples

**Example 1** (p. 399): For $G \subset \mathrm{GL}_n$, $G(\mathbb{Q})_L = G(\mathbb{Q}) \cap \mathrm{GL}_n(\mathbb{Z})$ when $L = \mathbb{Z}^n$. Changing to a different embedding gives a commensurable group.

# Relationships

## Builds Upon
- **Arithmetic subgroup** — proves the definition is well-defined
- **Principal congruence subgroup** — the proof uses congruence subgroups as intermediaries

## Enables
- **Congruence subgroup** — the independence extends to congruence subgroups

# Common Errors

- **Error**: Assuming $G(\mathbb{Q})_L = G(\mathbb{Q})_{L'}$ for different lattices
  **Correction**: They are commensurable but typically not equal

# Common Confusions

- **Confusion**: Thinking the specific group $\Gamma(N)$ is independent of the representation
  **Clarification**: The individual group $\Gamma(N)_L$ depends on $L$; only the commensurability class is independent

# Source Reference

Chapter VII: Arithmetic Subgroups, Section 4, pages 399-400. Lemma 4.1, Proposition 4.2.

# Verification Notes

- Definition source: Proposition 4.2 from p. 399
- Confidence: HIGH — explicit proposition with proof
- Uncertainties: None
- Cross-reference status: Verified
