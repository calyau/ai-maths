---
concept: "Gauss's Lemma"
slug: gauss-lemma
category: ring-theory
subcategory: polynomial-rings
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Polynomial Rings"
chapter_number: 9
pdf_page: 303
section: "9.3 Polynomial Rings that are Unique Factorization Domains"
extraction_confidence: high
aliases:
  - "Gauss' Lemma"
prerequisites:
  - unique-factorization-domain
  - polynomial-ring
  - field-of-fractions
extends: []
related:
  - irreducible-polynomial
  - content-of-polynomial
  - primitive-polynomial
  - polynomial-ring-as-ufd
contrasts_with: []
answers_questions:
  - "How do I determine whether a polynomial is irreducible?"
  - "What is the relationship between factoring in R[x] and F[x]?"
---

# Quick Definition
If R is a UFD with field of fractions F and $p(x) \in R[x]$ is reducible in $F[x]$, then $p(x)$ is reducible in $R[x]$. Equivalently, a primitive polynomial irreducible in $R[x]$ is also irreducible in $F[x]$.

# Core Definition
(Proposition 5) Let R be a UFD with field of fractions F and $p(x) \in R[x]$. If $p(x)$ is reducible in $F[x]$ then $p(x)$ is reducible in $R[x]$. More precisely, if $p(x) = A(x)B(x)$ for nonconstant $A(x), B(x) \in F[x]$, then there exist $r, s \in F$ such that $rA(x) = a(x)$ and $sB(x) = b(x)$ lie in $R[x]$ and $p(x) = a(x)b(x)$ (Dummit & Foote, p. 303).

# Prerequisites
- **Unique factorization domain** — R must be a UFD
- **Polynomial ring** — The lemma applies to $R[x]$
- **Field of fractions** — F is the field of fractions of R

# Key Properties
1. Reducibility in $F[x]$ implies reducibility in $R[x]$ (for polynomials in $R[x]$)
2. Contrapositive: irreducibility in $R[x]$ implies irreducibility in $F[x]$ (for primitive polynomials)
3. For primitive polynomials: irreducible in $R[x]$ iff irreducible in $F[x]$ (Corollary 6)
4. Key technique: "clear denominators" in a factorization over F to get one over R

# Construction / Recognition
## To Apply:
1. Factor $p(x)$ in $F[x]$ (where the Euclidean Algorithm is available)
2. Use Gauss's Lemma to transfer the factorization (or irreducibility) back to $R[x]$

# Context & Application
Gauss's Lemma is the bridge between factoring over a UFD and its fraction field. It is essential for proving that $R[x]$ is a UFD when R is, and for applying irreducibility criteria.

# Examples
**Example 1** (p. 304): $7x$ factors as $7 \cdot x$ in $\mathbb{Z}[x]$ (two irreducibles), but $7x$ is irreducible in $\mathbb{Q}[x]$ (since 7 is a unit there).

**Example 2** (p. 305): $x^2 + 1$ is irreducible in $\mathbb{Z}[2i][x]$ but reducible in $\mathbb{Q}(i)[x]$. This does not contradict Gauss since $\mathbb{Z}[2i]$ is not a UFD.

# Relationships

## Related
- **content-of-polynomial** — The GCD of coefficients, factored out before applying Gauss
- **primitive-polynomial** — A polynomial with content 1
- **polynomial-ring-as-ufd** — Gauss's Lemma is key to proving R[x] is a UFD

# Common Errors
- **Error**: Applying Gauss's Lemma when R is not a UFD
  **Correction**: The lemma requires R to be a UFD; it fails for $\mathbb{Z}[2i]$

# Common Confusions
- **Confusion**: Thinking Gauss's Lemma says factors in $F[x]$ directly lie in $R[x]$
  **Clarification**: Factors may need to be rescaled; $r A(x)$ and $s B(x)$ lie in $R[x]$, not necessarily $A(x)$ and $B(x)$

# Source Reference
Chapter 9, Section 9.3, Proposition 5 and Corollary 6, pages 303-304.

# Verification Notes
- Definition: Direct from Proposition 5, p. 303
- Confidence: HIGH — complete proof given
