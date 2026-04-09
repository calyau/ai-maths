---
# === CORE IDENTIFICATION ===
concept: Prime Ideal
slug: prime-ideal

# === CLASSIFICATION ===
category: ring-theory
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Rings"
chapter_number: 16
pdf_page: 213
section: "16.4 Maximal and Prime Ideals"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - ideal
  - integral-domain
extends:
  - ideal
related:
  - factor-ring
contrasts_with:
  - maximal-ideal

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a prime ideal?"
  - "How do prime ideals relate to integral domains?"
  - "What distinguishes a maximal ideal from a prime ideal?"
---

# Quick Definition

A prime ideal $P$ in a commutative ring $R$ is a proper ideal such that whenever $ab \in P$, either $a \in P$ or $b \in P$.

# Core Definition

"A proper ideal $P$ in a commutative ring $R$ is called a prime ideal if whenever $ab \in P$, then either $a \in P$ or $b \in P$" (Judson, p. 213). The fundamental characterization is: $P$ is a prime ideal in a commutative ring with identity iff $R/P$ is an integral domain (Proposition 16.38).

# Prerequisites

- **Ideal** — A prime ideal is a special type of ideal
- **Integral domain** — The characterization involves quotient rings being integral domains

# Key Properties

1. $P$ is a proper ideal ($P \neq R$)
2. If $ab \in P$ then $a \in P$ or $b \in P$
3. $R/P$ is an integral domain iff $P$ is prime (Proposition 16.38)
4. Every maximal ideal is prime (Corollary 16.40)
5. The converse fails in general (not every prime ideal is maximal)

# Construction / Recognition

## To Verify:
1. Confirm $P$ is a proper ideal
2. Show that $ab \in P$ implies $a \in P$ or $b \in P$
3. Alternatively, show $R/P$ is an integral domain

# Context & Application

Prime ideals generalize prime numbers. In $\mathbb{Z}$, the prime ideals are exactly $\{0\}$ and $p\mathbb{Z}$ for prime $p$. The name "prime ideal" is justified by this correspondence. In algebraic geometry, prime ideals correspond to irreducible varieties.

# Examples

**Example 1** (p. 213): In $\mathbb{Z}$, the nonzero prime ideals are $p\mathbb{Z}$ for prime $p$. These are also maximal.

**Example 2** (p. 213): $\{0, 2, 4, 6, 8, 10\}$ is a prime ideal in $\mathbb{Z}_{12}$ (and also maximal).

**Example 3** (p. 213): $\mathbb{Z}/n\mathbb{Z}$ is an integral domain iff $n$ is prime, so $n\mathbb{Z}$ is a prime ideal iff $n$ is prime.

# Relationships

## Builds Upon
- **Ideal** — A prime ideal is an ideal with an additional property

## Enables
- **Integral domain** — $R/P$ is an integral domain when $P$ is prime

## Contrasts With
- **Maximal ideal** — Maximal $\Rightarrow$ prime, but prime $\not\Rightarrow$ maximal in general

# Common Errors

- **Error**: Assuming prime and maximal ideals are the same
  **Correction**: Every maximal ideal is prime (Corollary 16.40), but not conversely in non-PID rings

# Common Confusions

- **Confusion**: Confusing the prime ideal condition with the ring element being "prime"
  **Clarification**: A prime ideal is defined by the property $ab \in P \Rightarrow a \in P$ or $b \in P$; this is a property of the ideal, not of a single element

# Source Reference

Chapter 16: Rings, Section 16.4, pages 213-214. See Proposition 16.38 and Corollary 16.40.

# Verification Notes

- Definition source: Direct quote from p. 213
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
