---
concept: Rational Canonical Form
slug: rational-canonical-form
category: linear-algebra
subcategory: canonical-forms
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Modules over Principal Ideal Domains"
chapter_number: 12
pdf_page: 474
section: "12.2 The Rational Canonical Form"
extraction_confidence: high
aliases:
  - "RCF"
prerequisites:
  - structure-theorem-modules-over-pids
  - fx-module
  - companion-matrix
  - invariant-factors
extends: []
related:
  - jordan-canonical-form
  - characteristic-polynomial
  - minimal-polynomial
  - similar-matrices
contrasts_with:
  - jordan-canonical-form
answers_questions:
  - "How do I find the rational canonical form?"
  - "What distinguishes the rational canonical form from the Jordan canonical form?"
---

# Quick Definition
The rational canonical form of a linear transformation T on a finite dimensional vector space V over F is the block diagonal matrix with companion matrices of the invariant factors $a_1(x) \mid a_2(x) \mid \cdots \mid a_m(x)$ of V as an F[x]-module. It exists over any field and is unique.

# Core Definition
By the structure theorem, $V \cong F[x]/(a_1(x)) \oplus \cdots \oplus F[x]/(a_m(x))$ as F[x]-modules with $a_1(x) \mid \cdots \mid a_m(x)$. Choosing the standard basis $\{1, \bar{x}, \ldots, \bar{x}^{k-1}\}$ for each $F[x]/(a_i(x))$, the matrix of T is the block diagonal matrix $\text{diag}(C_{a_1(x)}, \ldots, C_{a_m(x)})$ where $C_{a_i(x)}$ is the companion matrix of $a_i(x)$. This is the rational canonical form, and it is unique (Dummit & Foote, Theorem 14, pp. 478-479).

# Prerequisites
- **structure-theorem-modules-over-pids** — Provides the decomposition
- **fx-module** — V is viewed as an F[x]-module via T
- **companion-matrix** — Building blocks of the RCF
- **invariant-factors** — The polynomials $a_i(x)$ determining the form

# Key Properties
1. Exists over ANY field (does not require algebraic closure)
2. Unique for each linear transformation / similarity class
3. The minimal polynomial is the last (largest) invariant factor $a_m(x)$
4. The characteristic polynomial is the product $a_1(x) a_2(x) \cdots a_m(x)$
5. Two matrices are similar iff they have the same rational canonical form
6. The Cayley-Hamilton Theorem follows: $m_T(x) \mid c_T(x)$

# Construction / Recognition
## To Find the RCF:
1. Compute the characteristic polynomial $c_T(x) = \det(xI - A)$
2. Compute the minimal polynomial $m_T(x)$
3. The last invariant factor is $m_T(x)$; work backwards using divisibility to find all invariant factors
4. Alternatively, use the Smith normal form of $xI - A$

# Context & Application
The RCF provides a complete invariant for similarity of matrices. Unlike the JCF, it works over any field. It is "rational" because no field extension is needed.

# Examples
**Example** (p. 479): A $3 \times 3$ matrix with char. poly. $(x-1)(x^2+1)$ and min. poly. $(x-1)(x^2+1)$ has RCF = companion matrix of $(x-1)(x^2+1) = x^3 - x^2 + x - 1$.

# Relationships
## Builds Upon
- **structure-theorem-modules-over-pids**, **fx-module**, **companion-matrix**

## Related
- **characteristic-polynomial** — Product of invariant factors
- **minimal-polynomial** — Last invariant factor

## Contrasts With
- **jordan-canonical-form** — JCF uses elementary divisors; requires algebraically closed field

# Common Confusions
- **Confusion**: Thinking RCF requires eigenvalues to be in F. **Clarification**: The RCF works over ANY field; no splitting is required.

# Source Reference
Chapter 12, Section 12.2, Theorem 14, pp. 474-488.

# Verification Notes
- Confidence: HIGH — major theorem with detailed development
