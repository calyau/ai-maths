---
concept: R-Algebra
slug: r-algebra
category: module-theory
subcategory: basic-definitions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Module Theory"
chapter_number: 10
pdf_page: 345
section: "10.1 Basic Definitions and Examples"
extraction_confidence: high
aliases:
  - "algebra over a ring"
  - "algebra over R"
prerequisites:
  - ring
  - ring-homomorphism
  - left-module
extends:
  - ring
related:
  - tensor-product-of-algebras
  - polynomial-ring
contrasts_with: []
answers_questions:
  - "What is an algebra over a commutative ring?"
---

# Quick Definition
An R-algebra is a ring A with identity together with a ring homomorphism $f: R \to A$ mapping $1_R$ to $1_A$ such that $f(R)$ is contained in the center of A. This gives A a natural R-module structure.

# Core Definition
Let R be a commutative ring with identity. An R-algebra is a ring A with identity together with a ring homomorphism $f: R \to A$ mapping $1_R$ to $1_A$ such that the subring $f(R)$ of A is contained in the center of A. The natural R-module structure is given by $r \cdot a = f(r)a$ (Dummit & Foote, p. 345).

# Prerequisites
- **ring** — An R-algebra is a ring with extra structure
- **ring-homomorphism** — The structure map $f: R \to A$
- **left-module** — Every R-algebra has a natural R-module structure

# Key Properties
1. Any ring with identity is a $\mathbb{Z}$-algebra
2. If A is an algebra over a field F, then F is (isomorphic to) a subring of the center of A
3. The polynomial ring R[x] is an R-algebra
4. The group ring RG for a finite group G is an R-algebra
5. An R-algebra homomorphism is a ring homomorphism that is also an R-module map

# Context & Application
R-algebras unify the study of rings and modules. Important examples include polynomial rings, group rings, matrix rings, and tensor products of algebras.

# Examples
**Example 1** (p. 346): For any ring A with identity, if R is a subring of the center of A containing $1_A$, then A is an R-algebra.
**Example 2** (p. 346): The polynomial ring R[x] is an R-algebra for any commutative ring R with 1.

# Relationships
## Builds Upon
- **ring**, **left-module**

## Enables
- **tensor-product-of-algebras** — $A \otimes_R B$ is an R-algebra when A and B are

# Source Reference
Chapter 10, Section 10.1, pp. 345-347.

# Verification Notes
- Definition: direct from p. 345
- Confidence: HIGH — explicit definition with examples
