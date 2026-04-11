---
concept: Unit
slug: unit
category: ring-theory
subcategory: basic-definitions
tier: foundational
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 223
section: "7.1 Basic Definitions and Examples"
extraction_confidence: high
aliases:
  - "invertible element"
  - "unit element"
prerequisites:
  - ring-with-identity
extends: []
related:
  - group-of-units
  - field
  - division-ring
contrasts_with:
  - zero-divisor
  - irreducible-element
answers_questions:
  - "What is a unit in a ring?"
  - "Can a zero divisor be a unit?"
---

# Quick Definition
A unit in a ring R with identity $1 \neq 0$ is an element u that has a multiplicative inverse: there exists $v \in R$ with $uv = vu = 1$.

# Core Definition
Assume R has an identity $1 \neq 0$. An element u of R is called a *unit* in R if there is some $v \in R$ such that $uv = vu = 1$. The set of units in R is denoted $R^{\times}$ (Dummit & Foote, p. 227).

# Prerequisites
- **Ring with identity** — Units require a multiplicative identity to be defined

# Key Properties
1. The units form a group under multiplication ($R^{\times}$ is the *group of units*)
2. A zero divisor can never be a unit (p. 227)
3. A field is a commutative ring where $F^{\times} = F - \{0\}$
4. Being a unit depends on the ambient ring: $2 \notin \mathbb{Z}^{\times}$ but $2 \in \mathbb{Q}^{\times}$ (p. 228)
5. In $\mathbb{Z}/n\mathbb{Z}$, $\bar{u}$ is a unit iff $\gcd(u, n) = 1$ (p. 228)

# Construction / Recognition
## To Identify:
1. Find an element v with $uv = vu = 1$
2. In $\mathbb{Z}$: the only units are $\pm 1$
3. In $\mathbb{Z}/n\mathbb{Z}$: u is a unit iff $\gcd(u, n) = 1$

# Context & Application
Units play the role of "invertible elements" in a ring. The group of units $R^{\times}$ is an important algebraic invariant of the ring.

# Examples
**Example 1** (p. 228): $\mathbb{Z}^{\times} = \{\pm 1\}$.

**Example 2** (p. 228): In $\mathbb{Z}/n\mathbb{Z}$, the units are $\bar{u}$ with $\gcd(u, n) = 1$.

**Example 3** (p. 228): In the ring of functions $[0,1] \to \mathbb{R}$, the units are functions that are nonzero at every point.

# Relationships

## Enables
- **group-of-units** — Units form a group $R^{\times}$
- **field** — A field is a ring where all nonzero elements are units
- **associates** — Two elements differing by a unit factor

## Contrasts With
- **zero-divisor** — A unit can never be a zero divisor
- **irreducible-element** — An irreducible is a nonzero nonunit

# Common Errors
- **Error**: Assuming an element that is a unit in a larger ring is a unit in a subring
  **Correction**: $2$ is a unit in $\mathbb{Q}$ but not in $\mathbb{Z}$

# Common Confusions
- **Confusion**: Confusing "unit" with "identity"
  **Clarification**: The identity is a specific unit (namely 1); there may be many other units

# Source Reference
Chapter 7, Section 7.1, Definition (2), page 227.

# Verification Notes
- Definition: Direct from p. 227
- Confidence: HIGH — explicit definition
