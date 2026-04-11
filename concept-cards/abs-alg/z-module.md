---
concept: Z-Module
slug: z-module
category: module-theory
subcategory: basic-definitions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Module Theory"
chapter_number: 10
pdf_page: 339
section: "10.1 Basic Definitions and Examples"
extraction_confidence: high
aliases:
  - "module over the integers"
prerequisites:
  - left-module
  - abelian-group
extends:
  - left-module
related:
  - free-abelian-group
  - torsion-module
contrasts_with: []
answers_questions:
  - "What is the relationship between abelian groups and Z-modules?"
---

# Quick Definition
A $\mathbb{Z}$-module is simply an abelian group with the natural action of the integers given by repeated addition. The categories of $\mathbb{Z}$-modules and abelian groups are identical.

# Core Definition
Let $R = \mathbb{Z}$, let A be any abelian group written additively. Define $na$ for $n \in \mathbb{Z}$ and $a \in A$ as the n-fold sum (or negative sum) of a. This makes A into a $\mathbb{Z}$-module, and this is the only possible unital $\mathbb{Z}$-module structure on A. Thus $\mathbb{Z}$-modules are the same as abelian groups, and $\mathbb{Z}$-submodules are the same as subgroups (Dummit & Foote, p. 339).

# Prerequisites
- **left-module** — $\mathbb{Z}$-modules are a special case of modules
- **abelian-group** — Every abelian group is a $\mathbb{Z}$-module

# Key Properties
1. $\mathbb{Z}$-modules and abelian groups are the same objects
2. $\mathbb{Z}$-submodules are exactly subgroups
3. A $\mathbb{Z}$-module may have nonzero torsion elements (elements x with $nx = 0$ for some nonzero n)
4. If A has order m, then $mx = 0$ for all $x \in A$ by Lagrange's Theorem
5. An abelian p-group with $px = 0$ for all x is a vector space over $\mathbb{F}_p$

# Construction / Recognition
1. Take any abelian group A
2. Define $na$ as the n-fold sum for positive n, $-(|n|$-fold sum) for negative n, and $0a = 0$
3. This is automatically a unital $\mathbb{Z}$-module

# Context & Application
The identification of $\mathbb{Z}$-modules with abelian groups is fundamental. It forms the basis for the proof of the Fundamental Theorem of Finitely Generated Abelian Groups in Chapter 12, which is obtained by applying the structure theorem for modules over PIDs to $R = \mathbb{Z}$.

# Examples
**Example** (p. 339): The Klein 4-group is a 2-dimensional vector space over $\mathbb{F}_2 = \mathbb{Z}/2\mathbb{Z}$, since it is an abelian group with $2x = 0$ for all elements.

# Relationships
## Builds Upon
- **left-module** — $\mathbb{Z}$-modules are modules over the ring $\mathbb{Z}$

## Enables
- **torsion-module** — Torsion theory for $\mathbb{Z}$-modules is the theory of torsion abelian groups
- **free-abelian-group** — Free $\mathbb{Z}$-modules are free abelian groups

# Source Reference
Chapter 10, Section 10.1, pp. 339-340.

# Verification Notes
- Definition: direct from p. 339
- Confidence: HIGH — explicitly stated equivalence
