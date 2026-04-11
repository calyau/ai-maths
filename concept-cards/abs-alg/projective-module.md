---
concept: Projective Module
slug: projective-module
category: module-theory
subcategory: exact-sequences
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Module Theory"
chapter_number: 10
pdf_page: 399
section: "10.5 Exact Sequences"
extraction_confidence: high
aliases: []
prerequisites:
  - free-module
  - short-exact-sequence
  - module-homomorphism
extends: []
related:
  - injective-module
  - flat-module
  - free-module
contrasts_with:
  - injective-module
answers_questions:
  - "What is a projective module?"
  - "What distinguishes a free module from a projective module?"
  - "How do free modules relate to projective modules?"
---

# Quick Definition
An R-module P is projective if every short exact sequence $0 \to A \to B \to P \to 0$ splits, or equivalently, if P is a direct summand of a free module.

# Core Definition
An R-module P is called projective if it satisfies any of these equivalent conditions (Proposition 30): (1) $\text{Hom}_R(P, \_)$ takes short exact sequences to short exact sequences; (2) Every surjection onto P can be lifted: given $\varphi: M \twoheadrightarrow N$ and $f: P \to N$, there exists $F: P \to M$ with $\varphi \circ F = f$; (3) Every short exact sequence $0 \to A \to B \to P \to 0$ splits; (4) P is a direct summand of a free module (Dummit & Foote, Proposition 30, pp. 399-401).

# Prerequisites
- **free-module** — Projective modules are direct summands of free modules
- **short-exact-sequence** — Projectivity is characterized by splitting
- **module-homomorphism** — The lifting property uses homomorphisms

# Key Properties
1. Free modules are projective (Corollary 31)
2. A finitely generated module is projective iff it is a direct summand of a finitely generated free module
3. Every module is a quotient of a projective module
4. $\text{Hom}_R(P, \_)$ is exact iff P is projective
5. Projective modules are flat
6. Over a PID, finitely generated projective = free
7. Direct sums of projective modules are projective

# Construction / Recognition
## To Show P is Projective:
1. Show P is a direct summand of a free module, OR
2. Show every surjection onto P splits, OR
3. Show every homomorphism from P to a quotient lifts

# Context & Application
Projective modules generalize free modules and play a fundamental role in homological algebra. The functor $\text{Hom}_R(P, \_)$ is exact precisely when P is projective. Over "nice" rings (fields, PIDs for f.g. modules), projective = free.

# Examples
**Example 1** (p. 401): $\mathbb{Z}$ is a projective $\mathbb{Z}$-module (it is free).
**Example 2** (p. 403): No nonzero finite abelian group is a projective $\mathbb{Z}$-module.
**Example 3** (p. 403): Let $R = \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$. The ideals $(1,0)R$ and $(0,1)R$ are projective but not free.

# Relationships
## Builds Upon
- **free-module**, **short-exact-sequence**

## Enables
- **flat-module** — Every projective module is flat

## Related
- **injective-module** — The "dual" notion

## Contrasts With
- **injective-module** — Injective modules have the dual lifting property
- **free-module** — Every free module is projective, but not conversely in general

# Common Confusions
- **Confusion**: Thinking projective always means free. **Clarification**: Over general rings, projective modules need not be free. However, over PIDs, finitely generated projective modules are free.

# Source Reference
Chapter 10, Section 10.5, Proposition 30, pp. 399-403. See also Corollaries 31-32.

# Verification Notes
- Definition: four equivalent characterizations from Proposition 30
- Confidence: HIGH — extensive development with examples
