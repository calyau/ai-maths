---
# === CORE IDENTIFICATION ===
concept: Index of a Subgroup
slug: index-of-subgroup

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
pdf_page: 17
section: "Cosets"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - subgroup index

# === TYPED RELATIONSHIPS ===
prerequisites:
  - left-coset
extends: []
related:
  - lagrange-theorem
  - normal-subgroup
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the index of a subgroup?"
  - "How does the index relate to the order of the group?"
---

# Quick Definition

The index $(G : H)$ of a subgroup $H$ in $G$ is the number of distinct left cosets of $H$ in $G$. It can be finite or infinite.

# Core Definition

"The *index* $(G : H)$ of $H$ in $G$ is defined to be the number of left cosets of $H$ in $G$." (Milne, p. 17)

Note: $(G : H)$ also equals the number of right cosets (1.29).

# Prerequisites

- **Left coset** — The index counts the number of cosets

# Key Properties

1. $(G : 1)$ is the order of $G$
2. Lagrange's theorem: $(G : 1) = (G : H)(H : 1)$ for finite $G$ (Theorem 1.26)
3. Multiplicativity: $(G : K) = (G : H)(H : K)$ for $H \supset K$ (Proposition 1.31)
4. A subgroup of index 2 is always normal (Example 1.36a)

# Construction / Recognition

## To Compute the Index:
1. Count the distinct cosets $aH$ as $a$ ranges over $G$
2. For finite groups: $(G : H) = |G| / |H|$

# Context & Application

The index measures how "large" a subgroup is relative to the group. Index-2 subgroups are automatically normal, which is a frequently used criterion.

# Examples

**Example 1** (p. 18): In $D_n$, the cyclic subgroup $C_n = \langle r \rangle$ has index 2, since $D_n = C_n \sqcup sC_n$.

**Example 2**: $(G : 1) = |G|$ for any group $G$.

# Relationships

## Builds Upon
- **left-coset** — the index counts cosets

## Enables
- **lagrange-theorem** — relates index to group/subgroup orders
- **normal-subgroup** — index 2 implies normality

# Common Errors

- **Error**: Assuming the index is always finite
  **Correction**: For infinite groups, the index can be infinite (e.g., $(\mathbb{Z} : 0)$ is infinite)

# Source Reference

Chapter 1, p. 17, Proposition 1.31.

# Verification Notes

- Definition source: Direct from p. 17
- Confidence: HIGH — explicit definition
- Uncertainties: None
