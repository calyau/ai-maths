---
concept: Jordan Canonical Form
slug: jordan-canonical-form
category: linear-algebra
subcategory: canonical-forms
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Modules over Principal Ideal Domains"
chapter_number: 12
pdf_page: 491
section: "12.3 The Jordan Canonical Form"
extraction_confidence: high
aliases:
  - "JCF"
  - "Jordan form"
  - "Jordan normal form"
prerequisites:
  - elementary-divisors
  - fx-module
  - jordan-block
extends: []
related:
  - rational-canonical-form
  - generalized-eigenspace
  - characteristic-polynomial
  - minimal-polynomial
contrasts_with:
  - rational-canonical-form
answers_questions:
  - "How do I find the Jordan canonical form?"
  - "What distinguishes the rational canonical form from the Jordan canonical form?"
---

# Quick Definition
The Jordan canonical form exists when the characteristic polynomial of T splits completely over F (e.g., when F is algebraically closed). It is a block diagonal matrix of Jordan blocks $J_k(\lambda)$, one for each elementary divisor $(x - \lambda)^k$.

# Core Definition
If the characteristic polynomial of T splits over F as $\prod (x - \lambda_i)^{n_i}$, then the elementary divisors of V as an F[x]-module are powers $(x - \lambda_i)^{k_j}$. Each elementary divisor gives a Jordan block $J_k(\lambda)$: a $k \times k$ matrix with $\lambda$ on the diagonal, 1's on the superdiagonal, and zeros elsewhere. The JCF is the block diagonal matrix of these Jordan blocks, unique up to ordering of blocks (Dummit & Foote, Theorem 22, pp. 492-494).

# Prerequisites
- **elementary-divisors** — Jordan blocks correspond to elementary divisors
- **fx-module** — V is an F[x]-module
- **jordan-block** — Building blocks of the JCF

# Key Properties
1. Exists iff the characteristic polynomial splits completely over F
2. Always exists over algebraically closed fields (e.g., $\mathbb{C}$)
3. Unique up to ordering of Jordan blocks
4. The minimal polynomial is $\prod (x - \lambda_i)^{m_i}$ where $m_i$ is the size of the largest Jordan block for $\lambda_i$
5. T is diagonalizable iff all Jordan blocks are $1 \times 1$ (iff the minimal polynomial has no repeated roots)
6. Two matrices are similar iff they have the same JCF

# Construction / Recognition
## To Find the JCF:
1. Find all eigenvalues (roots of the characteristic polynomial)
2. For each eigenvalue $\lambda$, find the dimensions of $\ker(T - \lambda I)^k$ for $k = 1, 2, \ldots$
3. The sizes of Jordan blocks for $\lambda$ are determined by the jumps in these dimensions

# Context & Application
The JCF is the "simplest" matrix representation of a linear transformation when the field is large enough. It is central to differential equations, dynamical systems, and representation theory.

# Examples
**Example** (p. 494): A $4 \times 4$ matrix with char. poly. $(x-2)^2(x-3)^2$ and min. poly. $(x-2)^2(x-3)$ has JCF $\text{diag}(J_2(2), J_1(3), J_1(3))$.

# Relationships
## Builds Upon
- **elementary-divisors**, **fx-module**, **jordan-block**

## Related
- **characteristic-polynomial**, **minimal-polynomial**, **generalized-eigenspace**

## Contrasts With
- **rational-canonical-form** — RCF works over any field; JCF requires splitting

# Common Confusions
- **Confusion**: Thinking the JCF always exists. **Clarification**: It requires all eigenvalues to be in F. Over $\mathbb{R}$, a matrix with complex eigenvalues has no JCF.

# Source Reference
Chapter 12, Section 12.3, Theorem 22, pp. 491-504.

# Verification Notes
- Confidence: HIGH — major theorem with detailed development
