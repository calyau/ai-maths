---
concept: Associates
slug: associates
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
aliases:
  - "associate elements"
prerequisites:
  - integral-domain
  - unit
extends: []
related:
  - principal-ideal
  - irreducible-element
  - unique-factorization-domain
contrasts_with: []
answers_questions:
  - "What does it mean for two elements to be associates?"
  - "How are associates related to principal ideals?"
---

# Quick Definition
Two elements a and b of an integral domain R are associates if $a = ub$ for some unit $u \in R$.

# Core Definition
Two elements a and b of R differing by a unit are said to be *associate* in R, i.e., $a = ub$ for some unit $u$ in R (Dummit & Foote, p. 284).

# Prerequisites
- **Integral domain** — Associates are defined in integral domains
- **Unit** — Two elements differ by a unit factor

# Key Properties
1. $a$ and $b$ are associates iff $(a) = (b)$ (Proposition 3, p. 277)
2. Being associate is an equivalence relation
3. In $\mathbb{Z}$, $a$ and $b$ are associates iff $a = \pm b$
4. In a UFD, factorization is unique up to associates

# Construction / Recognition
## To Check:
1. Verify $a = ub$ for some unit $u \in R$
2. Equivalently, check $(a) = (b)$

# Context & Application
The notion of associates captures when two elements are "essentially the same" for factorization purposes.

# Examples
**Example 1**: In $\mathbb{Z}$, 3 and $-3$ are associates (the units are $\pm 1$).

**Example 2**: In $\mathbb{Z}[i]$, $1+i$ and $1-i$ are associates since $1-i = (-i)(1+i)$.

# Relationships

## Related
- **principal-ideal** — Associates generate the same principal ideal
- **unique-factorization-domain** — Factorization is unique up to associates

# Common Errors
- **Error**: Forgetting to check all units, not just $\pm 1$
  **Correction**: In $\mathbb{Z}[i]$, the units are $\{\pm 1, \pm i\}$, giving four associates per element

# Common Confusions
- **Confusion**: Thinking associates must be equal
  **Clarification**: Associates can look quite different; in $\mathbb{Z}[i]$, $2+i$ and $1-2i$ are associates

# Source Reference
Chapter 8, Section 8.3, Definition (3), page 284. See Proposition 3, page 277.

# Verification Notes
- Definition: Direct from p. 284
- Confidence: HIGH — explicit definition
