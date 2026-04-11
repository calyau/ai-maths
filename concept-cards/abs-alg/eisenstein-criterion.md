---
concept: "Eisenstein's Criterion"
slug: eisenstein-criterion
category: ring-theory
subcategory: polynomial-rings
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Polynomial Rings"
chapter_number: 9
pdf_page: 309
section: "9.4 Irreducibility Criteria"
extraction_confidence: high
aliases:
  - "Eisenstein-Schoenemann Criterion"
  - "Eisenstein criterion"
prerequisites:
  - polynomial-ring
  - prime-ideal
  - irreducible-polynomial
extends: []
related:
  - gauss-lemma
  - reduction-mod-p
  - irreducible-polynomial
contrasts_with: []
answers_questions:
  - "How do I determine whether a polynomial is irreducible?"
  - "What is Eisenstein's Criterion?"
---

# Quick Definition
A monic polynomial $f(x) = x^n + a_{n-1}x^{n-1} + \cdots + a_0 \in R[x]$ is irreducible if all non-leading coefficients lie in a prime ideal P and the constant term $a_0 \notin P^2$.

# Core Definition
(Proposition 13) Let P be a prime ideal of the integral domain R and let $f(x) = x^n + a_{n-1}x^{n-1} + \cdots + a_0 \in R[x]$ with $n \geq 1$. If $a_{n-1}, \ldots, a_0 \in P$ and $a_0 \notin P^2$, then $f(x)$ is irreducible in $R[x]$ (Dummit & Foote, p. 309).

For $\mathbb{Z}[x]$: if prime p divides all $a_i$ for $i < n$ but $p^2 \nmid a_0$, then $f(x)$ is irreducible in both $\mathbb{Z}[x]$ and $\mathbb{Q}[x]$ (Corollary 14, p. 310).

# Prerequisites
- **Polynomial ring** — Applied to polynomials
- **Prime ideal** — The criterion uses a prime ideal
- **Irreducible polynomial** — The conclusion is irreducibility

# Key Properties
1. Applies to monic polynomials (or polynomials whose leading coefficient is not in P)
2. Can sometimes be applied after a substitution $x \mapsto x + c$ (p. 310)
3. Does not apply to all irreducible polynomials: $x^4 + 1$ is irreducible in $\mathbb{Z}[x]$ but Eisenstein does not apply directly (p. 310)

# Construction / Recognition
## To Apply (in $\mathbb{Z}[x]$):
1. Find a prime p dividing all non-leading coefficients
2. Verify $p^2$ does not divide the constant term
3. Conclude irreducibility in $\mathbb{Z}[x]$ and $\mathbb{Q}[x]$

## Substitution Trick:
1. If Eisenstein doesn't apply to $f(x)$, try $g(x) = f(x + a)$
2. If $g(x)$ is irreducible by Eisenstein, so is $f(x)$

# Context & Application
Eisenstein's Criterion is one of the most frequently used irreducibility tests. It proves, for example, that the $p$th cyclotomic polynomial $\Phi_p(x) = x^{p-1} + x^{p-2} + \cdots + 1$ is irreducible over $\mathbb{Q}$.

# Examples
**Example 1** (p. 309): $x^4 + 10x + 5$ is irreducible by Eisenstein with $p = 5$.

**Example 2** (p. 310): $x^n - p$ is irreducible for any prime p and $n \geq 1$.

**Example 3** (p. 310): $x^4 + 1$ is irreducible: substitute $x \mapsto x + 1$ to get $x^4 + 4x^3 + 6x^2 + 4x + 2$, then apply Eisenstein with $p = 2$.

# Relationships

## Related
- **gauss-lemma** — Used in the proof to pass from $R[x]$ to $F[x]$
- **reduction-mod-p** — Eisenstein is a special case of reduction arguments
- **irreducible-polynomial** — The conclusion of the criterion

# Common Errors
- **Error**: Applying Eisenstein to a polynomial that is not monic without adjusting
  **Correction**: The criterion requires the leading coefficient to NOT be in P

- **Error**: Concluding a polynomial is reducible because Eisenstein doesn't apply
  **Correction**: Eisenstein is sufficient but not necessary for irreducibility

# Common Confusions
- **Confusion**: Thinking Eisenstein applies only to $\mathbb{Z}[x]$
  **Clarification**: The general form works for any integral domain R with a prime ideal P

# Source Reference
Chapter 9, Section 9.4, Proposition 13 and Corollary 14, pages 309-310.

# Verification Notes
- Definition: Direct from Proposition 13, p. 309
- Confidence: HIGH — explicit theorem with complete proof
