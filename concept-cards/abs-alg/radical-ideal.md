---
concept: Radical of an Ideal
slug: radical-ideal
category: ring-theory
subcategory: ideals
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 260
section: "7.4 Properties of Ideals"
extraction_confidence: high
aliases:
  - "radical ideal"
prerequisites:
  - ideal
  - commutative-ring
  - nilradical
extends: []
related:
  - nilradical
  - prime-ideal
contrasts_with: []
answers_questions:
  - "What is the radical of an ideal?"
  - "What is a radical ideal?"
---

# Quick Definition
The radical of an ideal I is $\text{rad}(I) = \{r \in R \mid r^n \in I \text{ for some } n > 0\}$. An ideal is radical if $\text{rad}(I) = I$.

# Core Definition
For an ideal I of a commutative ring R, the *radical* of I is $\text{rad}(I) = \{r \in R \mid r^n \in I \text{ for some } n \in \mathbb{Z}^+\}$. This is an ideal containing I, and $(\text{rad}(I))/I = \mathfrak{N}(R/I)$ is the nilradical of the quotient (Exercise 30, Dummit & Foote, p. 260). An ideal I is *radical* if $\text{rad}(I) = I$ (Exercise 31).

# Prerequisites
- **Ideal** — rad(I) is an ideal
- **Commutative ring** — R must be commutative
- **Nilradical** — rad(I)/I is the nilradical of R/I

# Key Properties
1. $\text{rad}(I)$ is an ideal containing I (Exercise 30)
2. Every prime ideal is a radical ideal (Exercise 31(a))
3. In $\mathbb{Z}$: $\text{rad}((n)) = (p_1 p_2 \cdots p_k)$ where the $p_i$ are the distinct prime factors of n

# Relationships

## Related
- **nilradical** — $\text{rad}(0) = \mathfrak{N}(R)$
- **prime-ideal** — Every prime ideal is radical

# Source Reference
Chapter 7, Section 7.4, Exercises 30-31, page 260.

# Verification Notes
- Definition: From Exercises 30-31, p. 260
- Confidence: MEDIUM — definition in exercises
