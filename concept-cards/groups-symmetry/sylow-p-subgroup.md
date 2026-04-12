---
# === CORE IDENTIFICATION ===
concept: Sylow p-Subgroup
slug: sylow-p-subgroup

# === CLASSIFICATION ===
category: finite-group-classification
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "The Sylow Theorems"
chapter_number: 20
pdf_page: 120
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Sylow subgroup"
  - "p-Sylow subgroup"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - subgroup
  - lagranges-theorem
extends: []
related:
  - first-sylow-theorem
  - second-sylow-theorem
  - third-sylow-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Sylow p-subgroup?"
  - "How do Sylow subgroups relate to the prime factorization of |G|?"
---

# Quick Definition

Let $G$ be a finite group with $|G| = kp^m$ where $p$ is prime and $p \nmid k$. A Sylow $p$-subgroup of $G$ is a subgroup of order $p^m$ -- the largest power of $p$ dividing $|G|$.

# Core Definition

Let $G$ be a finite group whose order is divisible by the prime $p$. Suppose $p^m$ is the highest power of $p$ which is a factor of $|G|$ and set $k = |G|/p^m$. Any subgroup of $G$ which contains $p^m$ elements is called a **Sylow $p$-subgroup** of $G$, or just a **Sylow subgroup** if we do not need to emphasise the prime $p$ (Armstrong, p. 124, Exercises preamble).

# Prerequisites

- **Subgroup** -- a Sylow $p$-subgroup is a subgroup of specific order
- **Lagrange's theorem** -- the order of a subgroup divides $|G|$

# Key Properties

1. Order of a Sylow $p$-subgroup is $p^m$ where $p^m \| |G|$ (exactly divides)
2. At least one Sylow $p$-subgroup always exists (First Sylow Theorem)
3. All Sylow $p$-subgroups are conjugate (Second Sylow Theorem)
4. The number of Sylow $p$-subgroups is $\equiv 1 \pmod{p}$ and divides $k$ (Third Sylow Theorem)
5. A Sylow $p$-subgroup is normal iff it is the unique Sylow $p$-subgroup

# Construction / Recognition

## To Identify Sylow p-Subgroups:
1. Factor $|G| = kp^m$ where $\gcd(k, p) = 1$
2. Look for subgroups of order $p^m$
3. Any subgroup of order $p^m$ is a Sylow $p$-subgroup

# Context & Application

Sylow subgroups are the fundamental building blocks for understanding the structure of finite groups. Armstrong uses them to classify all groups of order 12. The existence, conjugacy, and count of Sylow subgroups severely constrain the structure of finite groups.

# Examples

**Groups of order 12** (p. 121): $|G| = 12 = 4 \cdot 3$. Sylow 3-subgroups have order 3; there are either 1 or 4 of them. Sylow 2-subgroups have order 4; there are either 1 or 3 of them.

**Exercise 20.2** (p. 124): All Sylow subgroups of $A_5$ can be listed explicitly. None are normal (since $A_5$ is simple).

# Relationships

## Builds Upon
- **Subgroup** -- a Sylow $p$-subgroup is a specific kind of subgroup
- **Lagrange's theorem** -- constrains possible subgroup orders

## Enables
- **First Sylow theorem** -- guarantees existence
- **Second Sylow theorem** -- establishes conjugacy
- **Third Sylow theorem** -- counts Sylow subgroups
- **Classification of groups of order 12** -- applies Sylow theory

## Related
- **Normal subgroup** -- a unique Sylow $p$-subgroup must be normal

# Common Errors

- **Error**: Confusing "Sylow $p$-subgroup" with "any $p$-subgroup."
  **Correction**: A Sylow $p$-subgroup has order $p^m$ (the maximal power). A $p$-subgroup has order $p^j$ for any $j \le m$.

# Common Confusions

- **Confusion**: Thinking Sylow subgroups exist only for certain primes.
  **Clarification**: For every prime $p$ dividing $|G|$, there exists at least one Sylow $p$-subgroup.

# Source Reference

Chapter 20: The Sylow Theorems, pages 120--124. Definition on p. 124 (exercises preamble), theorems on p. 120.

# Verification Notes

- Definition: From exercises preamble, p. 124
- Confidence: HIGH -- standard definition, clearly stated
