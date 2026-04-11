---
concept: Permutation
slug: permutation
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
aliases: []
prerequisites:
  - bijection
extends:
  - bijection
related:
  - symmetric-group
  - cycle-decomposition
contrasts_with: []
answers_questions:
  - "What is a permutation?"
---

# Quick Definition
A permutation of a set A is a bijection from A to itself. The set of all permutations of A forms the symmetric group $S_A$ under composition.

# Core Definition
A *permutation* of a set A is simply a bijection from A to itself (Dummit & Foote, p. 3). Permutations compose as functions, with composition being associative.

# Prerequisites
- **Bijection** — a permutation is a bijection from a set to itself

# Key Properties
1. Permutations compose associatively
2. The identity permutation fixes all elements
3. Every permutation has an inverse permutation
4. The set of all permutations of A forms a group $S_A$

# Construction / Recognition
## To Identify/Recognize:
1. Check the map is a bijection from a set to itself

# Context & Application
Permutations are the elements of symmetric groups, which are fundamental to all of group theory via Cayley's Theorem.

# Examples
**Example 1** (p. 3): Any bijection from $\{1, 2, \ldots, n\}$ to itself is a permutation in $S_n$.

# Relationships
## Builds Upon
- **bijection**

## Enables
- **symmetric-group** — the group of all permutations
- **cycle-decomposition** — efficient notation for permutations

# Source Reference
Chapter 0, Section 0.1 "Basics," page 3.

# Verification Notes
- Definition source: direct from source p. 3
- Confidence rationale: explicitly defined
- Uncertainties: none
- Cross-reference status: verified
