---
concept: Kernel of Ring Homomorphism
slug: kernel-of-ring-homomorphism
category: ring-theory
subcategory: morphisms
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 239
section: "7.3 Ring Homomorphisms and Quotient Rings"
extraction_confidence: high
aliases: []
prerequisites:
  - ring-homomorphism
  - ideal
extends: []
related:
  - first-isomorphism-theorem-rings
  - quotient-ring
contrasts_with: []
answers_questions:
  - "What is the kernel of a ring homomorphism?"
  - "Why is the kernel always an ideal?"
---

# Quick Definition
The kernel of a ring homomorphism $\varphi: R \to S$ is the set of elements of R mapping to 0: $\ker\varphi = \{r \in R \mid \varphi(r) = 0\}$.

# Core Definition
The *kernel* of the ring homomorphism $\varphi$, denoted $\ker\varphi$, is the set of elements of R that map to 0 in S. The kernel is an ideal of R, and furthermore $r\alpha, \alpha r \in \ker\varphi$ for every $r \in R$ and $\alpha \in \ker\varphi$ (Dummit & Foote, p. 240, Proposition 5(2)).

# Prerequisites
- **Ring homomorphism** — The kernel is defined for a ring homomorphism
- **Ideal** — The kernel is always an ideal

# Key Properties
1. $\ker\varphi$ is an ideal of R (Proposition 5(2), p. 242)
2. $\varphi$ is injective iff $\ker\varphi = \{0\}$
3. Every ideal is the kernel of some ring homomorphism (Theorem 7(2), p. 246)
4. $R/\ker\varphi \cong \varphi(R)$ (First Isomorphism Theorem, Theorem 7(1), p. 246)

# Construction / Recognition
## To Find:
1. Given $\varphi: R \to S$, compute $\{r \in R \mid \varphi(r) = 0\}$

# Context & Application
The kernel-ideal correspondence is one of the central results: ideals are precisely kernels of ring homomorphisms, just as normal subgroups are precisely kernels of group homomorphisms.

# Examples
**Example 1** (p. 240): The kernel of reduction mod n ($\mathbb{Z} \to \mathbb{Z}/n\mathbb{Z}$) is $n\mathbb{Z}$.

**Example 2** (p. 241): The kernel of evaluation at 0 ($\mathbb{Q}[x] \to \mathbb{Q}$) is the set of polynomials with zero constant term.

# Relationships

## Related
- **first-isomorphism-theorem-rings** — Connects kernel, image, and quotient
- **quotient-ring** — $R/\ker\varphi$ is a ring isomorphic to the image

# Common Errors
- **Error**: Forgetting that the kernel of a ring homomorphism is more than just a subring
  **Correction**: The kernel is an ideal, which is stronger than being a subring

# Common Confusions
- **Confusion**: Thinking the kernel is just the additive kernel
  **Clarification**: The kernel is defined as the set mapping to 0, but Proposition 5 shows it automatically absorbs ring multiplication, making it an ideal

# Source Reference
Chapter 7, Section 7.3, Definition (2) on page 240 and Proposition 5 on page 242.

# Verification Notes
- Definition: Direct from p. 240
- Confidence: HIGH — explicit definition
