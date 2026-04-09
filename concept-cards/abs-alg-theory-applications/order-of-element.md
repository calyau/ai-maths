---
# === CORE IDENTIFICATION ===
concept: Order of an Element
slug: order-of-element

# === CLASSIFICATION ===
category: cyclic-groups
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Cyclic Groups"
chapter_number: 4
pdf_page: 60
section: "Cyclic Subgroups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - element order

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
  - cyclic-subgroup
extends: []
related:
  - group-order
  - generator
  - order-in-cyclic-groups
contrasts_with:
  - group-order

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I find the order of an element in a group?"
  - "What is a cyclic group?"
---

# Quick Definition

The order of an element $a$ in a group $G$ is the smallest positive integer $n$ such that $a^n = e$. If no such $n$ exists, the order is infinite.

# Core Definition

"If $a$ is an element of a group $G$, we define the order of $a$ to be the smallest positive integer $n$ such that $a^n = e$, and we write $|a| = n$. If there is no such integer $n$, we say that the order of $a$ is infinite and write $|a| = \infty$" (Judson, p. 60).

Key result: **Proposition 4.12**: In a cyclic group of order $n$ with generator $a$, $a^k = e$ if and only if $n$ divides $k$.

# Prerequisites

- **Group** — Element order is defined within a group
- **Cyclic subgroup** — The order of $a$ equals $|\langle a \rangle|$

# Key Properties

1. $|a|$ equals the size of the cyclic subgroup $\langle a \rangle$
2. $a^k = e$ if and only if $|a|$ divides $k$ (Proposition 4.12)
3. If $|a| = n$ and $b = a^k$, then $|b| = n / \gcd(k, n)$ (Theorem 4.13)
4. $|e| = 1$ for the identity element
5. In a finite group, every element has finite order

# Construction / Recognition

## To Find the Order of $a$:
1. Compute $a, a^2, a^3, \ldots$
2. The first $n$ such that $a^n = e$ is $|a|$
3. If computing in $\mathbb{Z}_n$ (additive), compute $a, 2a, 3a, \ldots$ until reaching 0

# Context & Application

Element order is crucial for understanding cyclic subgroups, determining generators, and classifying group elements. An element generates a cyclic group of order $n$ if and only if its order equals $n$.

# Examples

**Example 1** (p. 60): In $\mathbb{Z}_6$, $|2| = 3$ because $2 + 2 + 2 = 6 \equiv 0 \pmod{6}$ and no smaller multiple of 2 is $\equiv 0$.

**Example 2** (p. 60): In $U(9)$, $|2| = 6$ since $2^1 = 2, 2^2 = 4, 2^3 = 8, 2^4 = 7, 2^5 = 5, 2^6 = 1$.

**Example 3** (p. 62): In $\mathbb{Z}_{16}$, if $|a| = 16$ (a generator), and $b = 4a$, then $|b| = 16/\gcd(4, 16) = 16/4 = 4$.

# Relationships

## Builds Upon
- **group** — Defined within a group
- **cyclic-subgroup** — $|a| = |\langle a \rangle|$

## Enables
- **generator** — $a$ generates $G$ iff $|a| = |G|$

## Contrasts With
- **group-order** — Order of element vs. order of group (same notation $|\cdot|$)

# Common Errors

- **Error**: Confusing element order with group order
  **Correction**: $|a|$ is the order of element $a$ (smallest power giving $e$); $|G|$ is the number of elements in $G$

- **Error**: Forgetting that the identity has order 1, not 0
  **Correction**: $|e| = 1$ since $e^1 = e$

# Common Confusions

- **Confusion**: Thinking element order can be 0
  **Clarification**: Order is always a positive integer or infinite; the smallest positive integer $n$ with $a^n = e$

# Source Reference

Chapter 4: Cyclic Groups, Section 4.1, pages 60-62. Proposition 4.12, Theorem 4.13.

# Verification Notes

- Definition source: Direct quote from p. 60
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
