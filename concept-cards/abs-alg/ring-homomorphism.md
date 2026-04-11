---
concept: Ring Homomorphism
slug: ring-homomorphism
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
aliases:
  - "ring map"
prerequisites:
  - ring
extends:
  - homomorphism
related:
  - kernel-of-ring-homomorphism
  - ideal
  - first-isomorphism-theorem-rings
  - quotient-ring
contrasts_with:
  - group-homomorphism
answers_questions:
  - "What is a ring homomorphism?"
  - "What is the relationship between ring homomorphisms and ideals?"
---

# Quick Definition
A ring homomorphism is a map $\varphi: R \to S$ between rings that preserves both addition and multiplication: $\varphi(a+b) = \varphi(a) + \varphi(b)$ and $\varphi(ab) = \varphi(a)\varphi(b)$.

# Core Definition
A *ring homomorphism* is a map $\varphi: R \to S$ satisfying (i) $\varphi(a+b) = \varphi(a) + \varphi(b)$ for all $a, b \in R$ and (ii) $\varphi(ab) = \varphi(a)\varphi(b)$ for all $a, b \in R$ (Dummit & Foote, p. 239).

# Prerequisites
- **Ring** — Domain and codomain must be rings

# Key Properties
1. The image of $\varphi$ is a subring of S (Proposition 5(1), p. 242)
2. The kernel of $\varphi$ is an ideal of R (Proposition 5(2), p. 242)
3. A bijective ring homomorphism is an isomorphism (p. 240)
4. If R has identity and $\varphi$ is nonzero to an integral domain, then $\varphi(1_R) = 1_S$ (Exercise 17, p. 249)
5. Any nonzero homomorphism from a field is injective (Corollary 10, p. 254)

# Construction / Recognition
## To Verify:
1. Check $\varphi(a+b) = \varphi(a) + \varphi(b)$ for all $a, b$
2. Check $\varphi(ab) = \varphi(a)\varphi(b)$ for all $a, b$

# Context & Application
Ring homomorphisms are the structure-preserving maps of ring theory. The First Isomorphism Theorem connects homomorphisms, kernels (ideals), and quotient rings.

# Examples
**Example 1** (p. 240): The map $\mathbb{Z} \to \mathbb{Z}/n\mathbb{Z}$ reducing modulo n is a surjective ring homomorphism.

**Example 2** (p. 241): The evaluation map $p(x) \mapsto p(0)$ from $\mathbb{Q}[x]$ to $\mathbb{Q}$ is a ring homomorphism.

**Example 3** (p. 241): The map $x \mapsto nx$ on $\mathbb{Z}$ is *not* a ring homomorphism (for $n \neq 0, 1$) since $\varphi(xy) \neq \varphi(x)\varphi(y)$ in general.

# Relationships

## Enables
- **kernel-of-ring-homomorphism** — The kernel is always an ideal
- **first-isomorphism-theorem-rings** — $R/\ker\varphi \cong \varphi(R)$
- **quotient-ring** — Arises from surjective homomorphisms

## Related
- **ideal** — Ideals are precisely the kernels of ring homomorphisms

# Common Errors
- **Error**: Checking only additivity and assuming multiplicativity follows
  **Correction**: Must check both properties; $x \mapsto 2x$ on $\mathbb{Z}$ is additive but not multiplicative

# Common Confusions
- **Confusion**: Assuming a ring homomorphism sends 1 to 1
  **Clarification**: This holds if the codomain is an integral domain and the map is nonzero, but not in general

# Source Reference
Chapter 7, Section 7.3, Definition on page 239.

# Verification Notes
- Definition: Direct from p. 239
- Confidence: HIGH — explicit definition
