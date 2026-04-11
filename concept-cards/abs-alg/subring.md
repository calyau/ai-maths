---
concept: Subring
slug: subring
category: ring-theory
subcategory: basic-definitions
tier: foundational
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 223
section: "7.1 Basic Definitions and Examples"
extraction_confidence: high
aliases: []
prerequisites:
  - ring
extends: []
related:
  - ideal
  - ring-homomorphism
contrasts_with:
  - ideal
answers_questions:
  - "What is a subring?"
  - "How do you test whether a subset is a subring?"
---

# Quick Definition
A subring of a ring R is a subgroup of R (under addition) that is closed under multiplication.

# Core Definition
A *subring* of the ring R is a subgroup of R that is closed under multiplication. To show that a subset S of a ring R is a subring, it suffices to check that it is nonempty and closed under subtraction and under multiplication (Dummit & Foote, p. 229).

# Prerequisites
- **Ring** — Subrings are subsets of rings

# Key Properties
1. A subring inherits the ring structure from the ambient ring
2. The "is a subring of" relation is transitive (p. 230)
3. The intersection of any nonempty collection of subrings is a subring (Exercise 4, p. 233)
4. A subring of a ring with identity need not contain the identity

# Construction / Recognition
## Subring Test:
1. Check S is nonempty
2. Check S is closed under subtraction: $a - b \in S$ for all $a, b \in S$
3. Check S is closed under multiplication: $ab \in S$ for all $a, b \in S$

# Context & Application
Subrings generalize the notion of "sub-structure" from groups to rings. Every ideal is a subring (but not conversely).

# Examples
**Example 1** (p. 230): $\mathbb{Z}$ is a subring of $\mathbb{Q}$, and $\mathbb{Q}$ is a subring of $\mathbb{R}$.

**Example 2** (p. 230): $n\mathbb{Z}$ is a subring of $\mathbb{Z}$ for any integer n.

**Example 3** (p. 230): $\mathbb{Z}[i]$ (Gaussian integers) is a subring of $\mathbb{C}$.

# Relationships

## Enables
- **ideal** — An ideal is a subring with additional absorption properties

## Contrasts With
- **ideal** — An ideal must absorb multiplication by all ring elements; a subring need not

# Common Errors
- **Error**: Assuming a subring of a ring with identity must contain the identity
  **Correction**: $2\mathbb{Z}$ is a subring of $\mathbb{Z}$ but does not contain 1

# Common Confusions
- **Confusion**: Confusing subring with ideal
  **Clarification**: Every ideal is a subring, but not every subring is an ideal. E.g., $\mathbb{Z}$ is a subring of $\mathbb{Q}$ but not an ideal of $\mathbb{Q}$

# Source Reference
Chapter 7, Section 7.1, Definition on page 229.

# Verification Notes
- Definition: Direct from p. 229
- Confidence: HIGH — explicit definition
