---
concept: Direct Sum of Modules
slug: direct-sum-of-modules
category: module-theory
subcategory: generation
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Module Theory"
chapter_number: 10
pdf_page: 354
section: "10.3 Generation of Modules, Direct Sums, and Free Modules"
extraction_confidence: high
aliases:
  - "internal direct sum"
  - "external direct sum"
prerequisites:
  - left-module
  - submodule
extends:
  - direct-product
related:
  - free-module
  - split-exact-sequence
contrasts_with:
  - direct-product-of-modules
answers_questions:
  - "What is the direct sum of modules?"
---

# Quick Definition
The direct sum $M = N_1 \oplus N_2 \oplus \cdots \oplus N_k$ means every element of M can be written uniquely as $n_1 + n_2 + \cdots + n_k$ with $n_i \in N_i$.

# Core Definition
An R-module $M = N_1 + N_2 + \cdots + N_k$ is the (internal) direct sum of submodules $N_1, \ldots, N_k$, written $M = N_1 \oplus N_2 \oplus \cdots \oplus N_k$, if every element $m \in M$ can be written uniquely as $m = n_1 + n_2 + \cdots + n_k$ with $n_i \in N_i$. This is equivalent to $N_j \cap (N_1 + \cdots + N_{j-1} + N_{j+1} + \cdots + N_k) = 0$ for all j. The internal direct sum is isomorphic to the external direct product $N_1 \times N_2 \times \cdots \times N_k$ (Dummit & Foote, Proposition 5, p. 354).

# Prerequisites
- **left-module** — Direct sums are built from modules
- **submodule** — Internal direct sum involves submodules

# Key Properties
1. Three equivalent conditions (Proposition 5): unique representation, trivial intersections, isomorphism with external direct product
2. For finitely many modules, direct sum equals direct product
3. For infinitely many modules, the direct sum consists of elements with only finitely many nonzero components

# Context & Application
Direct sums decompose modules into simpler pieces. The structure theorem for modules over PIDs expresses finitely generated modules as direct sums of cyclic modules.

# Relationships
## Builds Upon
- **left-module**, **submodule**

## Enables
- **free-module** — Free modules of finite rank are direct sums of copies of R
- **structure-theorem-modules-over-pids**

## Contrasts With
- **direct-product-of-modules** — For infinite families, direct product includes elements with infinitely many nonzero components

# Source Reference
Chapter 10, Section 10.3, Proposition 5, pp. 354-355.

# Verification Notes
- Definition: from Proposition 5, p. 354
- Confidence: HIGH — explicit proposition with three equivalent characterizations
