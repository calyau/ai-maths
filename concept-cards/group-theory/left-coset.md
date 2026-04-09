---
# === CORE IDENTIFICATION ===
concept: Left Coset
slug: left-coset

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
  - coset

# === TYPED RELATIONSHIPS ===
prerequisites:
  - subgroup
extends: []
related:
  - right-coset
  - index-of-subgroup
  - lagrange-theorem
  - normal-subgroup
contrasts_with:
  - right-coset

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a coset?"
  - "How do cosets partition a group?"
---

# Quick Definition

For a subgroup $H$ of $G$ and an element $a \in G$, the left coset of $H$ containing $a$ is the set $aH = \{ah \mid h \in H\}$. The left cosets of $H$ partition $G$.

# Core Definition

"When $H$ is a subgroup of $G$, the sets of the form $aH$ are called the **left cosets** of $H$ in $G$." (Milne, p. 17)

Properties (Proposition 1.25):
- (a) $a \in aH$, and if $a$ lies in a left coset $C$, then $C = aH$
- (b) Two left cosets are either disjoint or equal
- (c) $aH = bH$ if and only if $a^{-1}b \in H$
- (d) Any two left cosets have the same number of elements

# Prerequisites

- **Subgroup** — Cosets are defined relative to a subgroup

# Key Properties

1. $aH = H$ if and only if $a \in H$
2. Left cosets partition $G$ into equivalence classes
3. The equivalence relation is: $a \sim b \iff a^{-1}b \in H$
4. All left cosets have the same cardinality as $H$
5. Because of associativity, $a(bH) = (ab)H$

# Construction / Recognition

## To Compute Cosets:
1. Pick $a \in G$
2. Compute $aH = \{ah \mid h \in H\}$
3. For the next coset, pick $b \notin aH$ and compute $bH$
4. Continue until $G$ is exhausted

# Context & Application

Cosets are the building blocks of Lagrange's theorem and quotient groups. They partition $G$ into equal-sized pieces, which forces $|H|$ to divide $|G|$ when $G$ is finite.

# Examples

**Example 1** (p. 17): Let $G = (\mathbb{R}^2, +)$ and $H$ a line through the origin. The cosets are the lines $a + H$ parallel to $H$.

**Example 2**: For $H = \{e, r, r^2, \ldots, r^{n-1}\}$ in $D_n$, the two cosets are $H$ and $sH = \{s, rs, \ldots, r^{n-1}s\}$.

# Relationships

## Builds Upon
- **subgroup** — cosets are defined relative to a subgroup

## Enables
- **index-of-subgroup** — the number of distinct cosets
- **lagrange-theorem** — counts cosets
- **quotient-group** — cosets become elements of the quotient

## Contrasts With
- **right-coset** — $Ha$ instead of $aH$; in general $aH \neq Ha$

# Common Errors

- **Error**: Assuming $aH = Ha$ for any subgroup $H$
  **Correction**: Left and right cosets coincide only when $H$ is normal

# Common Confusions

- **Confusion**: Thinking cosets are subgroups
  **Clarification**: A coset $aH$ is a subgroup only when $a \in H$ (in which case $aH = H$)

# Source Reference

Chapter 1, Section "Cosets", Proposition 1.25, pages 17-18.

# Verification Notes

- Definition source: Direct quote from p. 17
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified with Proposition 1.25
- Uncertainties: None
