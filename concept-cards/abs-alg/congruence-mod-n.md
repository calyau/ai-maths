---
concept: "Congruence Modulo n"
slug: congruence-mod-n
category: foundations
subcategory: modular-arithmetic
tier: foundational
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Preliminaries"
chapter_number: 0
pdf_page: 14
section: "0.3 The Integers Modulo n"
extraction_confidence: high
aliases:
  - "modular congruence"
  - "congruence"
prerequisites:
  - equivalence-relation
  - greatest-common-divisor
extends:
  - equivalence-relation
related:
  - integers-mod-n
  - residue-class
contrasts_with: []
answers_questions:
  - "What does it mean for two integers to be congruent modulo n?"
  - "How many residue classes are there modulo n?"
---

# Quick Definition
Two integers a and b are congruent modulo n, written $a \equiv b \pmod{n}$, if n divides $b - a$. This is an equivalence relation on $\mathbb{Z}$ with exactly n equivalence classes.

# Core Definition
Let n be a fixed positive integer. Define a relation on $\mathbb{Z}$ by $a \sim b$ iff $n \mid (b - a)$. This relation is reflexive, symmetric, and transitive, hence an equivalence relation. We write $a \equiv b \pmod{n}$. The equivalence class of a is $\bar{a} = \{a + kn \mid k \in \mathbb{Z}\}$, called the *congruence class* or *residue class* of a mod n. There are exactly n distinct residue classes: $\bar{0}, \bar{1}, \ldots, \overline{n-1}$ (Dummit & Foote, pp. 7-8).

# Prerequisites
- **Equivalence relation** — congruence is an equivalence relation
- **Greatest common divisor** — needed for modular inverses

# Key Properties
1. Exactly n distinct residue classes mod n
2. Addition and multiplication are well defined on classes: $\bar{a} + \bar{b} = \overline{a+b}$, $\bar{a} \cdot \bar{b} = \overline{ab}$
3. The set $\mathbb{Z}/n\mathbb{Z}$ of residue classes is an abelian group under addition
4. $(\mathbb{Z}/n\mathbb{Z})^\times = \{\bar{a} \mid (a,n) = 1\}$ is an abelian group under multiplication

# Construction / Recognition
## To Construct/Create:
1. Fix a positive integer n
2. Reduce any integer a mod n by finding the remainder upon division by n

## To Identify/Recognize:
1. Two integers are congruent mod n iff their difference is divisible by n
2. The least nonnegative representative is the remainder in $\{0, 1, \ldots, n-1\}$

# Context & Application
$\mathbb{Z}/n\mathbb{Z}$ under addition is the prototypical cyclic group of order n. The construction of $\mathbb{Z}/n\mathbb{Z}$ as equivalence classes with well-defined operations foreshadows the general quotient group construction. Modular arithmetic has applications in number theory and cryptography.

# Examples
**Example 1** (p. 8): In $\mathbb{Z}/12\mathbb{Z}$, $\bar{5} + \bar{8} = \overline{13} = \bar{1}$ and $\bar{5} \cdot \bar{8} = \overline{40} = \bar{4}$.
**Example 2** (p. 9): Computing $2^{1000} \pmod{100}$: successive squaring gives the last two digits as 76.

# Relationships
## Builds Upon
- **equivalence-relation** — congruence is an instance

## Enables
- **integers-mod-n** — the group $\mathbb{Z}/n\mathbb{Z}$
- **cyclic-group** — $\mathbb{Z}/n\mathbb{Z}$ is the prototypical finite cyclic group
- **quotient-group** — $\mathbb{Z}/n\mathbb{Z}$ is a quotient of $\mathbb{Z}$

## Related
- **residue-class** — elements of $\mathbb{Z}/n\mathbb{Z}$

# Common Errors
- **Error**: Computing with representatives without reducing mod n. **Correction**: Always reduce the result modulo n to find the canonical representative.

# Common Confusions
- **Confusion**: Thinking elements of $\mathbb{Z}/n\mathbb{Z}$ are integers. **Clarification**: Elements are *classes* of integers; the arithmetic differs from integer arithmetic (e.g., $5 + 8 = 1$ in $\mathbb{Z}/12\mathbb{Z}$).

# Source Reference
Chapter 0: Preliminaries, Section 0.3 "The Integers Modulo n," pages 7-10, Theorem 3, Proposition 4.

# Verification Notes
- Definition source: direct from source pp. 7-8
- Confidence rationale: extensively developed with examples
- Uncertainties: none
- Cross-reference status: verified
