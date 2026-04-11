---
concept: General Linear Group
slug: general-linear-group
category: group-theory
subcategory: important-groups
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Groups"
chapter_number: 1
pdf_page: 26
section: "1.4 Matrix Groups"
extraction_confidence: high
aliases:
  - "$GL_n(F)$"
prerequisites:
  - group
extends:
  - group
related:
  - special-linear-group
contrasts_with:
  - abelian-group
answers_questions:
  - "What is the general linear group?"
  - "What are matrix groups?"
---

# Quick Definition
$GL_n(F)$ is the group of all invertible $n \times n$ matrices with entries from a field F, under matrix multiplication. It is non-abelian for $n \geq 2$.

# Core Definition
For each $n \in \mathbb{Z}^+$ and field F, the *general linear group of degree n* is $GL_n(F) = \{A \mid A \text{ is an } n \times n \text{ matrix over } F, \det(A) \neq 0\}$ under matrix multiplication. It is a group since $\det(AB) = \det(A)\det(B)$ ensures closure, and $\det(A) \neq 0$ iff A is invertible. If $|F| = q < \infty$, then $|GL_n(F)| = (q^n - 1)(q^n - q)(q^n - q^2)\cdots(q^n - q^{n-1})$ (Dummit & Foote, pp. 34-35).

# Prerequisites
- **Group** — $GL_n(F)$ is a group under matrix multiplication

# Key Properties
1. Non-abelian for $n \geq 2$
2. $|GL_n(F)|$ has a product formula when F is finite
3. $GL_n(F)$ is finite iff F is finite
4. $SL_n(F) = \{A \in GL_n(F) \mid \det(A) = 1\}$ is a normal subgroup
5. $GL_2(\mathbb{F}_2) \cong S_3$

# Context & Application
Matrix groups provide concrete, computable examples of groups. They connect group theory to linear algebra and are important in representation theory. Many important groups arise as subgroups of $GL_n(F)$.

# Examples
**Example 1** (p. 35): $|GL_2(\mathbb{F}_2)| = (4-1)(4-2) = 6$, and $GL_2(\mathbb{F}_2) \cong S_3$.

# Relationships
## Builds Upon
- **group**

## Related
- **special-linear-group** — $SL_n(F) \trianglelefteq GL_n(F)$ with $GL_n(F)/SL_n(F) \cong F^\times$

## Contrasts With
- **abelian-group** — $GL_n(F)$ is non-abelian for $n \geq 2$

# Source Reference
Chapter 1, Section 1.4 "Matrix Groups," pages 34-36.

# Verification Notes
- Definition source: direct from source pp. 34-35
- Confidence rationale: explicitly defined
- Uncertainties: none
- Cross-reference status: verified
