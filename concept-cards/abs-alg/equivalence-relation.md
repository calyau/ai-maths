---
concept: Equivalence Relation
slug: equivalence-relation
category: foundations
subcategory: set-theory
tier: foundational
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Preliminaries"
chapter_number: 0
pdf_page: 14
section: "0.1 Basics"
extraction_confidence: high
aliases:
  - "equivalence"
prerequisites:
  - set
extends: []
related:
  - partition
  - congruence-mod-n
  - coset
contrasts_with: []
answers_questions:
  - "What is an equivalence relation?"
  - "How do equivalence relations relate to partitions?"
---

# Quick Definition
An equivalence relation on a set A is a binary relation that is reflexive, symmetric, and transitive. Its equivalence classes partition A.

# Core Definition
A binary relation $\sim$ on a set A is an *equivalence relation* if it is: (a) reflexive ($a \sim a$ for all $a \in A$), (b) symmetric ($a \sim b \implies b \sim a$), and (c) transitive ($a \sim b$ and $b \sim c \implies a \sim c$). The *equivalence class* of $a$ is $\{x \in A \mid x \sim a\}$; any element of the class is a *representative*. The equivalence classes form a partition of A, and conversely any partition determines an equivalence relation (Dummit & Foote, pp. 3-4, Proposition 2).

# Prerequisites
- **Set** — Equivalence relations are defined on sets

# Key Properties
1. Reflexive, symmetric, and transitive
2. Equivalence classes partition the set (Proposition 2)
3. Every partition determines a unique equivalence relation
4. Two elements are equivalent iff they belong to the same class

# Construction / Recognition
## To Construct/Create:
1. Define a relation $\sim$ on A
2. Verify reflexivity, symmetry, and transitivity

## To Identify/Recognize:
1. Check all three properties, or identify the induced partition

# Context & Application
Equivalence relations underlie all quotient constructions in algebra. Congruence modulo n, coset decomposition, and fiber decomposition of homomorphisms are all instances.

# Examples
**Example 1** (p. 7): $a \equiv b \pmod{n}$ iff $n \mid (b-a)$ is an equivalence relation on $\mathbb{Z}$ with n equivalence classes.

# Relationships
## Builds Upon
- **set**

## Enables
- **congruence-mod-n** — modular arithmetic via equivalence
- **coset** — cosets as equivalence classes
- **quotient-group** — elements are equivalence classes

## Related
- **partition** — equivalent formulation

# Common Errors
- **Error**: Forgetting to verify transitivity. **Correction**: Transitivity is the most commonly violated property; always check it explicitly.

# Common Confusions
- **Confusion**: Believing different representatives give different equivalence classes. **Clarification**: Any element of a class serves as a representative for the same class.

# Source Reference
Chapter 0: Preliminaries, Section 0.1 "Basics," pages 3-4, Proposition 2.

# Verification Notes
- Definition source: direct from source pp. 3-4
- Confidence rationale: explicitly defined with proposition
- Uncertainties: none
- Cross-reference status: verified
