---
concept: Maximal Ideal
slug: maximal-ideal
category: ring-theory
subcategory: ideals
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 254
section: "7.4 Properties of Ideals"
extraction_confidence: high
aliases: []
prerequisites:
  - ideal
  - field
extends:
  - prime-ideal
related:
  - quotient-ring
  - prime-ideal
contrasts_with:
  - prime-ideal
answers_questions:
  - "What is a maximal ideal?"
  - "What distinguishes a prime ideal from a maximal ideal?"
  - "How do maximal ideals relate to fields?"
---

# Quick Definition
A maximal ideal M of a ring R is a proper ideal ($M \neq R$) that is not contained in any other proper ideal -- the only ideals containing M are M and R itself.

# Core Definition
An ideal M in an arbitrary ring S is called a *maximal ideal* if $M \neq S$ and the only ideals containing M are M and S (Dummit & Foote, p. 254).

# Prerequisites
- **Ideal** — A maximal ideal is a special kind of ideal
- **Field** — Needed for the characterization via quotients

# Key Properties
1. M is maximal iff $R/M$ is a field (Proposition 12, p. 256; for commutative R)
2. Every maximal ideal is a prime ideal (Corollary 14, p. 258)
3. In a ring with $1 \neq 0$, every proper ideal is contained in a maximal ideal (Proposition 11, p. 254; uses Zorn's Lemma)
4. In a PID, every nonzero prime ideal is maximal (Proposition 7, p. 283)
5. In $\mathbb{Z}$, the maximal ideals are exactly $(p)$ for prime p (p. 255)

# Construction / Recognition
## To Recognize:
1. Verify M is a proper ideal
2. Check: if $M \subseteq I \subseteq R$ with I an ideal, then $I = M$ or $I = R$
3. Equivalently (for commutative R): check that $R/M$ is a field

## To Construct:
1. Quotient by a maximal ideal: $R/M$ is a field

# Context & Application
Maximal ideals are the ring-theoretic tool for constructing fields. In algebraic geometry, maximal ideals of polynomial rings correspond to "points." Every commutative ring with identity has at least one maximal ideal (via Zorn's Lemma).

# Examples
**Example 1** (p. 255): $p\mathbb{Z}$ is a maximal ideal in $\mathbb{Z}$ for each prime p, since $\mathbb{Z}/p\mathbb{Z}$ is a field.

**Example 2** (p. 255): $(2, x)$ is a maximal ideal in $\mathbb{Z}[x]$ since $\mathbb{Z}[x]/(2, x) \cong \mathbb{Z}/2\mathbb{Z}$.

**Example 3** (p. 256): For the ring of continuous functions on $[0,1]$, $M_a = \{f \mid f(a) = 0\}$ is a maximal ideal for each $a \in [0,1]$.

# Relationships

## Builds Upon
- **prime-ideal** — Every maximal ideal is prime (but not conversely)

## Enables
- **field** — $R/M$ is a field when M is maximal (in commutative R)

## Contrasts With
- **prime-ideal** — A prime ideal P gives $R/P$ integral domain; maximal gives a field

# Common Errors
- **Error**: Assuming every prime ideal is maximal
  **Correction**: $(0)$ in $\mathbb{Z}$ is prime but not maximal; $(x)$ in $\mathbb{Z}[x]$ is prime but not maximal

# Common Confusions
- **Confusion**: Thinking "maximal" means "largest ideal"
  **Clarification**: A maximal ideal is a proper ideal that is maximal among proper ideals; R itself is the largest ideal but is not considered maximal

# Source Reference
Chapter 7, Section 7.4, Definition on page 254. See Propositions 11 and 12 on pages 254-256.

# Verification Notes
- Definition: Direct from p. 254
- Key results: Propositions 11, 12; Corollary 14
- Confidence: HIGH — explicit definition with clean characterization
