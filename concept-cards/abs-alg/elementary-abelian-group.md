---
concept: Elementary Abelian Group
slug: elementary-abelian-group
category: group-theory
subcategory: direct-semidirect-products
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Direct and Semidirect Products and Abelian Groups"
chapter_number: 5
pdf_page: 160
section: "5.1 Direct Products"
extraction_confidence: high
aliases:
  - "elementary abelian p-group"
prerequisites:
  - direct-product
  - cyclic-group
  - p-group
extends:
  - p-group
related:
  - automorphism-group
  - fundamental-theorem-finitely-generated-abelian-groups
contrasts_with: []
answers_questions:
  - "What is an elementary abelian group?"
  - "Why does Aut(Z_p x Z_p) equal GL_2(F_p)?"
---

# Quick Definition
The elementary abelian group of order p^n is E_{p^n} = Z_p x Z_p x ... x Z_p (n copies), an abelian p-group where every nonidentity element has order p. Its automorphism group is GL_n(F_p).

# Core Definition
For a prime p and n in Z^+, E_{p^n} = Z_p x Z_p x ... x Z_p (n factors) is an abelian group of order p^n with the property that x^p = 1 for all x. This is the elementary abelian group of order p^n (Dummit & Foote, p. 160). By Proposition 4.17(3), it can be viewed as an n-dimensional vector space over F_p, and Aut(E_{p^n}) = GL_n(F_p). The Klein 4-group V_4 is the elementary abelian group of order 4.

# Prerequisites
- **Direct product** — Defined as a direct product of copies of Z_p
- **Cyclic group** — Each factor is Z_p
- **p-group** — E_{p^n} is a p-group

# Key Properties
1. Every nonidentity element has order p
2. |E_{p^n}| = p^n
3. E_{p^n} is an n-dimensional vector space over F_p
4. Aut(E_{p^n}) = GL_n(F_p)
5. E_{p^2} has exactly p+1 subgroups of order p
6. Uniquely determined up to isomorphism by p and n

# Examples
**Example 1** (p. 160): V_4 = Z_2 x Z_2 is the elementary abelian group of order 4.

**Example 2** (p. 161): E_{p^2} has p+1 subgroups of order p.

# Relationships
## Builds Upon
- **p-group** — E_{p^n} is a special p-group
## Related
- **Automorphism group** — Aut(E_{p^n}) = GL_n(F_p)

# Source Reference
Chapter 5, Section 5.1, pages 160-161. Also Section 4.4, Proposition 17(3).

# Verification Notes
- Definition source: Direct from p. 160
- Confidence: HIGH
- Uncertainties: None
