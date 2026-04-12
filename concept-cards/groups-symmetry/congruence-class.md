---
# === CORE IDENTIFICATION ===
concept: Congruence Class
slug: congruence-class

# === CLASSIFICATION ===
category: equivalence-partitions
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Partitions"
chapter_number: 12
pdf_page: 68
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "residue class"
  - "congruence class modulo n"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - equivalence-class
  - equivalence-relation
extends:
  - equivalence-class
related:
  - r-n-group
  - cyclic-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a congruence class?"
  - "How does modular arithmetic relate to equivalence relations?"
---

# Quick Definition

The congruence classes modulo $n$ are the equivalence classes of integers under the relation $x \sim y$ iff $n | (x - y)$. There are exactly $n$ such classes: $\mathcal{R}(0), \mathcal{R}(1), \ldots, \mathcal{R}(n-1)$.

# Core Definition

Replacing 3 by a positive integer $n$ in Example (i) gives an equivalence relation on $\mathbb{Z}$ which partitions $\mathbb{Z}$ into $n$ equivalence classes $\mathcal{R}(0), \mathcal{R}(1), \ldots, \mathcal{R}(n-1)$ called **congruence classes**. An integer $x$ belongs to $\mathcal{R}(m)$ precisely when $x$ is congruent to $m$ modulo $n$ (Armstrong, Ch. 12, p. 69).

# Prerequisites

- **Equivalence class** — Congruence classes are equivalence classes of a specific relation
- **Equivalence relation** — Congruence modulo $n$ is an equivalence relation

# Key Properties

1. There are exactly $n$ congruence classes modulo $n$
2. Each integer belongs to exactly one class
3. The classes can be added and multiplied in a well-defined manner (Exercise 12.6)
4. Under addition, the congruence classes form a group isomorphic to $\mathbb{Z}_n$

# Construction / Recognition

## To Construct:
1. Fix a positive integer $n$
2. Define: $x \sim y$ iff $n | (x - y)$
3. The equivalence classes are $\{m + kn \mid k \in \mathbb{Z}\}$ for $m = 0, 1, \ldots, n-1$

# Context & Application

Armstrong uses congruence classes as the most concrete example of equivalence classes, bridging the abstract definition to familiar modular arithmetic. Exercise 12.6 asks the reader to verify that congruence classes under addition form a group isomorphic to $\mathbb{Z}_n$, providing an alternative construction of cyclic groups.

# Examples

**Example 1** (p. 68): Congruence classes modulo 3: $\mathcal{R}(0) = \{0, \pm 3, \pm 6, \ldots\}$, $\mathcal{R}(1) = \{1, 4, -2, \ldots\}$, $\mathcal{R}(2) = \{2, 5, -1, \ldots\}$.

# Relationships

## Builds Upon
- **Equivalence class** — A congruence class is a specific type of equivalence class

## Enables
- **Cyclic group $\mathbb{Z}_n$** — Can be defined as congruence classes under addition (Exercise 12.6)

## Related
- **$R_n$ group** — Uses integers coprime to $n$ with multiplication modulo $n$

# Common Errors

- **Error**: Defining addition of classes using specific representatives without checking well-definedness
  **Correction**: Exercise 12.6 requires verifying that $[x] = [x']$ and $[y] = [y']$ imply $[x + y] = [x' + y']$

# Common Confusions

- **Confusion**: Thinking a congruence class is a single number
  **Clarification**: A congruence class is an infinite set of integers. The notation $[m]$ or $\mathcal{R}(m)$ denotes the entire set of integers congruent to $m$ modulo $n$

# Source Reference

Chapter 12: Partitions, Example (ii), p. 69 (pdf). Also Exercise 12.6.

# Verification Notes

- Definition source: Direct from p. 69, Example (ii)
- Confidence rationale: HIGH — explicitly defined and named
- Uncertainties: None
