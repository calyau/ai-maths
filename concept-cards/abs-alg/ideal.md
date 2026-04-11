---
concept: Ideal
slug: ideal
category: ring-theory
subcategory: ideals
tier: foundational
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 243
section: "7.3 Ring Homomorphisms and Quotient Rings"
extraction_confidence: high
aliases:
  - "two-sided ideal"
prerequisites:
  - ring
  - subring
extends:
  - subring
related:
  - quotient-ring
  - ring-homomorphism
  - principal-ideal
  - prime-ideal
  - maximal-ideal
contrasts_with:
  - subring
  - normal-subgroup
answers_questions:
  - "What is an ideal?"
  - "How do ideals in rings relate to normal subgroups in groups?"
---

# Quick Definition
An ideal I of a ring R is a subring that is closed under multiplication by arbitrary elements of R: $rI \subseteq I$ and $Ir \subseteq I$ for all $r \in R$.

# Core Definition
A subset I of R is a *left ideal* if (i) I is a subring of R, and (ii) $rI \subseteq I$ for all $r \in R$. Similarly, I is a *right ideal* if (i) holds and $Ir \subseteq I$ for all $r \in R$. A subset that is both a left and right ideal is called an *ideal* (or two-sided ideal) of R. For commutative rings, the notions of left, right, and two-sided ideal coincide (Dummit & Foote, pp. 243-244).

# Prerequisites
- **Ring** — Ideals are subsets of rings
- **Subring** — An ideal must first be a subring

# Key Properties
1. The kernel of any ring homomorphism is an ideal (Proposition 5, p. 243)
2. Every ideal is the kernel of some ring homomorphism (Theorem 7(2), p. 246)
3. $I = R$ iff I contains a unit (Proposition 9(1), p. 253)
4. R is a field iff its only ideals are 0 and R (Proposition 9(2), p. 253)
5. The intersection of any nonempty collection of ideals is an ideal
6. If R has a 1, then I is an ideal iff it is nonempty, closed under addition, and closed under multiplication by all elements of R

# Construction / Recognition
## To Verify I is an Ideal (in a ring with 1):
1. Check I is nonempty
2. Check I is closed under addition
3. Check $rI \subseteq I$ and $Ir \subseteq I$ for all $r \in R$

# Context & Application
Ideals are the ring-theoretic analogue of normal subgroups in group theory. Just as normal subgroups are precisely the kernels of group homomorphisms and allow the formation of quotient groups, ideals are precisely the kernels of ring homomorphisms and allow the formation of quotient rings (p. 243).

# Examples
**Example 1** (p. 245): $n\mathbb{Z}$ is an ideal of $\mathbb{Z}$ for any integer n, and these are all ideals of $\mathbb{Z}$.

**Example 2** (p. 245): In $\mathbb{Z}[x]$, the set of polynomials with even constant term is an ideal.

**Example 3** (p. 249): In $M_n(R)$, $M_n(J)$ is a two-sided ideal for any ideal J of R.

# Relationships

## Builds Upon
- **subring** — Every ideal is a subring (but not conversely)

## Enables
- **quotient-ring** — $R/I$ is a ring when I is an ideal
- **prime-ideal** — A special type of ideal
- **maximal-ideal** — A maximal proper ideal

## Contrasts With
- **subring** — A subring need not absorb multiplication by arbitrary ring elements
- **normal-subgroup** — The analogous concept in group theory

# Common Errors
- **Error**: Only checking closure under multiplication of elements *within* I
  **Correction**: Must check $rI \subseteq I$ for all $r \in R$, not just for $r \in I$

# Common Confusions
- **Confusion**: Thinking every subring is an ideal
  **Clarification**: $\mathbb{Z}$ is a subring of $\mathbb{Q}$ but not an ideal (since $\frac{1}{2} \cdot 1 = \frac{1}{2} \notin \mathbb{Z}$)

# Source Reference
Chapter 7, Section 7.3, Definition on pages 243-244.

# Verification Notes
- Definition: Direct from pp. 243-244
- Confidence: HIGH — explicit definition with extensive discussion
