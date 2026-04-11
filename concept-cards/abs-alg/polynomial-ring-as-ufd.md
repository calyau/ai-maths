---
concept: Polynomial Ring as UFD
slug: polynomial-ring-as-ufd
category: ring-theory
subcategory: polynomial-rings
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Polynomial Rings"
chapter_number: 9
pdf_page: 304
section: "9.3 Polynomial Rings that are Unique Factorization Domains"
extraction_confidence: high
aliases: []
prerequisites:
  - unique-factorization-domain
  - polynomial-ring
  - gauss-lemma
extends: []
related:
  - unique-factorization-domain
  - gauss-lemma
contrasts_with: []
answers_questions:
  - "When is a polynomial ring a UFD?"
  - "Is Z[x] a UFD?"
---

# Quick Definition
R is a UFD if and only if $R[x]$ is a UFD. In particular, $\mathbb{Z}[x]$, $\mathbb{Z}[x,y]$, $F[x,y]$, etc., are all UFDs.

# Core Definition
(Theorem 7) R is a Unique Factorization Domain if and only if $R[x]$ is a Unique Factorization Domain (Dummit & Foote, p. 304). By induction, $R[x_1, \ldots, x_n]$ is a UFD whenever R is (Corollary 8, p. 305).

# Prerequisites
- **Unique factorization domain** — R must be a UFD
- **Polynomial ring** — The result is about $R[x]$
- **Gauss's lemma** — Key tool in the proof

# Key Properties
1. The UFD property passes to polynomial rings (unlike PID or Euclidean)
2. $\mathbb{Z}[x]$ is a UFD but not a PID
3. $F[x, y]$ is a UFD but not a PID
4. Factoring in $R[x]$: first factor out the content (GCD of coefficients), then factor the primitive part using $F[x]$

# Construction / Recognition
## To Factor in $R[x]$ (R a UFD):
1. Write $p(x) = d \cdot p'(x)$ where d is the content and $p'(x)$ is primitive
2. Factor d into irreducibles in R
3. Factor $p'(x)$ in $F[x]$ and use Gauss's Lemma to transfer back to $R[x]$

# Context & Application
This theorem shows that polynomial rings over UFDs always have unique factorization, even when they are not PIDs. It is fundamental for computational algebra.

# Examples
**Example 1** (p. 305): $\mathbb{Z}[x]$ is a UFD (but not a PID since $(2, x)$ is not principal).

**Example 2** (p. 305): $\mathbb{Q}[x, y]$ is a UFD (but not a PID since $(x, y)$ is not principal).

**Example 3** (p. 305): $\mathbb{Z}[\sqrt{-5}][x]$ is NOT a UFD since $\mathbb{Z}[\sqrt{-5}]$ is not a UFD.

# Relationships

## Related
- **unique-factorization-domain** — The theorem characterizes when $R[x]$ is a UFD
- **gauss-lemma** — The essential tool for the proof

# Common Errors
- **Error**: Assuming $R[x]$ is a PID when R is a UFD
  **Correction**: $\mathbb{Z}$ is a PID but $\mathbb{Z}[x]$ is not; UFD property transfers, PID does not

# Source Reference
Chapter 9, Section 9.3, Theorem 7 and Corollary 8, pages 304-305.

# Verification Notes
- Definition: Direct from Theorem 7, p. 304
- Confidence: HIGH — fundamental theorem with complete proof
