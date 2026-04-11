---
concept: Formal Power Series Ring
slug: formal-power-series
category: ring-theory
subcategory: ring-constructions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 239
section: "7.2 Examples: Polynomial Rings, Matrix Rings, and Group Rings"
extraction_confidence: high
aliases:
  - "power series ring"
prerequisites:
  - commutative-ring
  - polynomial-ring
extends:
  - ring
related:
  - polynomial-ring
  - field-of-fractions
contrasts_with:
  - polynomial-ring
answers_questions:
  - "What is the ring of formal power series?"
  - "When is a formal power series a unit?"
---

# Quick Definition
The ring $R[[x]]$ of formal power series consists of all infinite sums $\sum_{n=0}^{\infty} a_nx^n$ with $a_n \in R$, with the same addition and multiplication rules as polynomials.

# Core Definition
$R[[x]]$ is defined as the set of all formal infinite sums $\sum_{n=0}^{\infty} a_nx^n$ with coefficients $a_n \in R$. Addition is componentwise and multiplication is defined by $(\sum a_nx^n)(\sum b_nx^n) = \sum_{n=0}^{\infty}(\sum_{k=0}^n a_kb_{n-k})x^n$. The term "formal" indicates convergence is not considered (Exercise 3, Dummit & Foote, pp. 239-240).

# Prerequisites
- **Commutative ring** — R is a commutative ring with identity
- **Polynomial ring** — $R[x] \subset R[[x]]$

# Key Properties
1. $R[[x]]$ is a commutative ring with identity
2. $\sum a_nx^n$ is a unit iff $a_0$ is a unit in R (Exercise 3(c))
3. $1 - x$ is a unit with inverse $1 + x + x^2 + \cdots$ (Exercise 3(b))
4. If R is an integral domain, so is $R[[x]]$ (Exercise 4)
5. $(x)$ is a prime ideal; $(x)$ is maximal iff R is a field (Exercise 18, p. 259)

# Examples
**Example 1**: $1/(1-x) = 1 + x + x^2 + \cdots$ in $R[[x]]$.

**Example 2**: If $F$ is a field, $F[[x]]$ is a local ring with maximal ideal $(x)$.

# Relationships

## Related
- **polynomial-ring** — $R[x]$ is a subring of $R[[x]]$
- **field-of-fractions** — The field of fractions of $F[[x]]$ is the Laurent series ring $F((x))$

## Contrasts With
- **polynomial-ring** — Power series have infinitely many terms; polynomials have finitely many

# Source Reference
Chapter 7, Section 7.2, Exercise 3, pages 239-240.

# Verification Notes
- Definition: From Exercise 3, pp. 239-240
- Confidence: HIGH — detailed exercise with multiple parts
