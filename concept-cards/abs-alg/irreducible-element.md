---
concept: Irreducible Element
slug: irreducible-element
category: ring-theory
subcategory: factorization
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Euclidean Domains, Principal Ideal Domains, and Unique Factorization Domains"
chapter_number: 8
pdf_page: 283
section: "8.3 Unique Factorization Domains (U.F.D.s)"
extraction_confidence: high
aliases: []
prerequisites:
  - integral-domain
  - unit
extends: []
related:
  - prime-element
  - associates
  - unique-factorization-domain
contrasts_with:
  - prime-element
  - unit
answers_questions:
  - "What is an irreducible element in a ring?"
  - "How does irreducible differ from prime?"
---

# Quick Definition
A nonzero non-unit element r in an integral domain R is irreducible if whenever $r = ab$, at least one of a or b must be a unit.

# Core Definition
Suppose $r \in R$ is nonzero and is not a unit. Then r is called *irreducible* in R if whenever $r = ab$ with $a, b \in R$, at least one of a or b must be a unit in R. Otherwise r is said to be *reducible* (Dummit & Foote, p. 284).

# Prerequisites
- **Integral domain** — Irreducibility is defined in integral domains
- **Unit** — The definition involves distinguishing units from non-units

# Key Properties
1. A prime element is always irreducible (Proposition 10, p. 285)
2. The converse is not true in general: 3 is irreducible but not prime in $\mathbb{Z}[\sqrt{-5}]$ (p. 285)
3. In a PID, irreducible = prime (Proposition 11, p. 284)
4. In a UFD, irreducible = prime (Proposition 12, p. 286)
5. If $N(\alpha)$ is a prime integer, then $\alpha$ is irreducible in $\mathcal{O}$ (p. 291)

# Construction / Recognition
## To Verify:
1. Check r is nonzero and not a unit
2. Show: if $r = ab$ then a or b is a unit
3. Equivalently: the only divisors of r are units and associates of r

## Using Norms:
1. If R has a multiplicative norm and $N(r)$ is prime in $\mathbb{Z}$, then r is irreducible

# Context & Application
Irreducible elements are the "atoms" of factorization in integral domains. In a UFD, every nonzero non-unit factors uniquely (up to associates) into irreducibles.

# Examples
**Example 1**: In $\mathbb{Z}$, the irreducible elements are $\pm p$ for prime p.

**Example 2** (p. 285): In $\mathbb{Z}[\sqrt{-5}]$, the element 3 is irreducible but not prime.

**Example 3** (p. 293): In $\mathbb{Z}[i]$, $1+i$ is irreducible (norm = 2, a prime).

# Relationships

## Related
- **prime-element** — Prime implies irreducible; converse holds in PIDs and UFDs
- **associates** — Elements differing by a unit factor
- **unique-factorization-domain** — Factorization into irreducibles

## Contrasts With
- **prime-element** — An irreducible need not be prime in non-UFDs
- **unit** — An irreducible is by definition not a unit

# Common Errors
- **Error**: Assuming irreducible = prime in all domains
  **Correction**: In $\mathbb{Z}[\sqrt{-5}]$, 3 is irreducible but not prime

# Common Confusions
- **Confusion**: Confusing "irreducible" in ring theory with "irreducible polynomial"
  **Clarification**: An irreducible polynomial is an irreducible element of the polynomial ring

# Source Reference
Chapter 8, Section 8.3, Definition (1), page 284.

# Verification Notes
- Definition: Direct from p. 284
- Confidence: HIGH — explicit definition
