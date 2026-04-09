---
# === CORE IDENTIFICATION ===
concept: Left Coset
slug: left-coset

# === CLASSIFICATION ===
category: group-structure
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Cosets and Lagrange's Theorem"
chapter_number: 6
pdf_page: 87
section: "6.1 Cosets"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - permutation-group
extends: []
related:
  - right-coset
  - index-of-a-subgroup
  - lagranges-theorem
contrasts_with:
  - right-coset

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a coset?"
  - "What is a left coset?"
  - "How do I compute cosets of a subgroup?"
---

# Quick Definition

A left coset of a subgroup $H$ in a group $G$ with representative $g \in G$ is the set $gH = \{gh : h \in H\}$. Left cosets partition $G$ into disjoint subsets of equal size.

# Core Definition

"Let $G$ be a group and $H$ a subgroup of $G$. Define a *left coset* of $H$ with representative $g \in G$ to be the set $gH = \{gh : h \in H\}$" (Judson, p. 87). The left cosets of $H$ in $G$ partition $G$ (Theorem 6.4).

# Prerequisites

- **Subgroup** (Ch. 3-4) — Cosets are defined relative to a subgroup

# Key Properties

1. The left cosets of $H$ partition $G$ into disjoint subsets (Theorem 6.4)
2. Every left coset $gH$ has exactly $|H|$ elements (Proposition 6.9)
3. $g_1H = g_2H$ if and only if $g_1^{-1}g_2 \in H$ (Lemma 6.3)
4. $gH = H$ if and only if $g \in H$
5. The number of left cosets equals the number of right cosets (Theorem 6.8)

# Construction / Recognition

## To Compute Left Cosets of $H$ in $G$:
1. Choose any $g \in G$
2. Compute $gH = \{gh : h \in H\}$
3. Choose an element $g'$ not in any previously computed coset
4. Compute $g'H$
5. Repeat until all elements of $G$ are covered

# Context & Application

Cosets are central to Lagrange's Theorem and to the theory of quotient groups. They reveal the internal structure of groups by showing how subgroups "tile" the group.

# Examples

**Example 1** (p. 87): Let $H = \{0, 3\}$ in $\mathbb{Z}_6$. The left cosets are $0 + H = 3 + H = \{0, 3\}$, $1 + H = 4 + H = \{1, 4\}$, $2 + H = 5 + H = \{2, 5\}$.

**Example 2** (p. 87): Let $H = \{(1), (123), (132)\}$ in $S_3$. The left cosets are $(1)H = \{(1), (123), (132)\}$ and $(12)H = \{(12), (13), (23)\}$.

# Relationships

## Builds Upon
- **Subgroup** — Cosets are defined relative to a subgroup

## Enables
- **Lagrange's Theorem** — Uses the partition into cosets
- **Index of a Subgroup** — The number of distinct cosets
- **Coset Decoding** — Used in coding theory (Chapter 8)

## Contrasts With
- **Right Coset** — Left and right cosets may differ for non-normal subgroups

# Common Errors

- **Error**: Assuming left cosets are the same as right cosets
  **Correction**: $gH \neq Hg$ in general; they coincide only when $H$ is normal

# Common Confusions

- **Confusion**: Thinking a coset is a subgroup
  **Clarification**: A coset $gH$ is a subgroup only when $g \in H$ (in which case $gH = H$)

# Source Reference

Chapter 6: Cosets and Lagrange's Theorem, Section 6.1, pages 87-89.

# Verification Notes

- Definition source: Direct from p. 87
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
