---
# === CORE IDENTIFICATION ===
concept: Equivalence Class
slug: equivalence-class

# === CLASSIFICATION ===
category: foundations
subcategory: set-theory
tier: foundational

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Preliminaries"
chapter_number: 1
pdf_page: 25
section: "Equivalence Relations and Partitions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - equivalence-relation
extends: []
related:
  - partition
  - congruence-modulo-n
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
  - "What is an equivalence class?"
---

# Quick Definition

The equivalence class of an element $x$ under an equivalence relation $\sim$ is the set of all elements equivalent to $x$: $[x] = \{y \in X : y \sim x\}$.

# Core Definition

"Let $\sim$ be an equivalence relation on a set $X$ and let $x \in X$. Then $[x] = \{y \in X : y \sim x\}$ is called the equivalence class of $x$" (Judson, p. 25). Two equivalence classes are either disjoint or equal (Corollary 1.26).

# Prerequisites

- **Equivalence relation** — Equivalence classes arise from equivalence relations

# Key Properties

1. Every element belongs to exactly one equivalence class
2. $[x] = [y]$ if and only if $x \sim y$
3. Two equivalence classes are either disjoint or equal (Corollary 1.26)
4. The equivalence classes partition the set $X$ (Theorem 1.25)
5. Every equivalence class is nonempty (since $x \in [x]$)

# Construction / Recognition

## To Construct $[x]$:
1. Start with element $x$
2. Find all elements $y$ such that $y \sim x$
3. Collect them into the set $[x]$

# Context & Application

Equivalence classes are the building blocks of modular arithmetic: $\mathbb{Z}_n$ consists of the equivalence classes of integers modulo $n$. Groups can often be studied by examining their cosets, which are equivalence classes of an equivalence relation.

# Examples

**Example 1** (p. 26): Under congruence mod 3, the equivalence classes are:
- $[0] = \{\ldots, -3, 0, 3, 6, \ldots\}$
- $[1] = \{\ldots, -2, 1, 4, 7, \ldots\}$
- $[2] = \{\ldots, -1, 2, 5, 8, \ldots\}$

**Example 2** (p. 26): Under the relation $p/q \sim r/s$ (if $ps = qr$), the equivalence class of $1/2$ is $\{1/2, 2/4, 3/6, \ldots, -1/(-2), \ldots\}$ — all fractions reducing to $1/2$.

**Example 3** (p. 26): Under $(x_1, y_1) \sim (x_2, y_2)$ if $x_1^2 + y_1^2 = x_2^2 + y_2^2$ on $\mathbb{R}^2$, the equivalence classes are circles centered at the origin.

# Relationships

## Builds Upon
- **equivalence-relation** — Classes arise from equivalence relations

## Enables
- **integers-mod-n** — $\mathbb{Z}_n$ is the set of equivalence classes under congruence mod $n$
- **partition** — Equivalence classes form a partition

# Common Errors

- **Error**: Assuming different representatives always yield different equivalence classes
  **Correction**: $[x] = [y]$ whenever $x \sim y$; the same class can be represented by many elements

# Common Confusions

- **Confusion**: Confusing an equivalence class with a single element
  **Clarification**: An equivalence class is a set of all elements equivalent to a given element

# Source Reference

Chapter 1: Preliminaries, Section 1.2, pages 25-27. Theorem 1.25 and Corollary 1.26.

# Verification Notes

- Definition source: Direct quote from p. 25
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
