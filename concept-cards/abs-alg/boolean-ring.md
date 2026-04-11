---
concept: Boolean Ring
slug: boolean-ring
category: ring-theory
subcategory: special-rings
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 234
section: "7.1 Basic Definitions and Examples"
extraction_confidence: high
aliases: []
prerequisites:
  - commutative-ring
extends:
  - commutative-ring
related:
  - characteristic-of-ring
contrasts_with: []
answers_questions:
  - "What is a Boolean ring?"
---

# Quick Definition
A Boolean ring is a ring in which $a^2 = a$ for all elements a. Every Boolean ring is commutative and has characteristic 2.

# Core Definition
A ring R is called a *Boolean ring* if $a^2 = a$ for all $a \in R$ (Exercise 15, Dummit & Foote, p. 234).

# Prerequisites
- **Commutative ring** — Every Boolean ring is commutative (Exercise 15)

# Key Properties
1. Every Boolean ring is commutative (Exercise 15, p. 234)
2. Every Boolean ring has characteristic 2 (Exercise 27, p. 251)
3. The only Boolean ring that is an integral domain is $\mathbb{Z}/2\mathbb{Z}$ (Exercise 16, p. 234)
4. Every prime ideal in a Boolean ring is maximal (Exercise 23, p. 260)
5. A finite Boolean ring with identity is $(\mathbb{Z}/2\mathbb{Z})^n$ (Exercise 2, p. 269)

# Examples
**Example 1** (Exercise 21, p. 234): The power set $\mathcal{P}(X)$ with symmetric difference as addition and intersection as multiplication is a Boolean ring.

# Source Reference
Chapter 7, Section 7.1, Exercise 15, page 234.

# Verification Notes
- Definition: From Exercise 15, p. 234
- Confidence: HIGH — explicit definition in exercises
