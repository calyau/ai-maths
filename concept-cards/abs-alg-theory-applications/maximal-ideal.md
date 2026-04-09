---
# === CORE IDENTIFICATION ===
concept: Maximal Ideal
slug: maximal-ideal

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
pdf_page: 212
section: "16.4 Maximal and Prime Ideals"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - ideal
  - field
extends:
  - ideal
related:
  - factor-ring
contrasts_with:
  - prime-ideal

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a maximal ideal?"
  - "How do maximal ideals relate to fields?"
  - "What distinguishes a maximal ideal from a prime ideal?"
---

# Quick Definition

A maximal ideal $M$ of a ring $R$ is a proper ideal that is not contained in any other proper ideal of $R$. Equivalently, if $I$ is an ideal with $M \subset I \subset R$, then $I = M$ or $I = R$.

# Core Definition

"A proper ideal $M$ of a ring $R$ is a maximal ideal of $R$ if the ideal $M$ is not a proper subset of any ideal of $R$ except $R$ itself" (Judson, p. 212). The fundamental characterization is: $M$ is maximal in a commutative ring with identity iff $R/M$ is a field (Theorem 16.35).

# Prerequisites

- **Ideal** — A maximal ideal is a special type of ideal
- **Field** — The characterization involves quotient rings being fields

# Key Properties

1. $M$ is a proper ideal ($M \neq R$)
2. No ideal properly contains $M$ except $R$
3. $R/M$ is a field iff $M$ is maximal (Theorem 16.35)
4. Every maximal ideal is a prime ideal (Corollary 16.40)
5. In a PID, $\langle p \rangle$ is maximal iff $p$ is irreducible (Theorem 18.12)

# Construction / Recognition

## To Verify:
1. Confirm $M$ is a proper ideal of $R$
2. Show that any ideal $I$ with $M \subset I \subset R$ satisfies $I = M$ or $I = R$
3. Alternatively, show $R/M$ is a field

# Context & Application

Maximal ideals are the ring-theoretic analog of maximal normal subgroups. They produce the "simplest" nontrivial quotient rings (fields). In algebraic geometry, maximal ideals correspond to points.

# Examples

**Example 1** (p. 213): $p\mathbb{Z}$ is a maximal ideal of $\mathbb{Z}$ for any prime $p$, since $\mathbb{Z}/p\mathbb{Z} \cong \mathbb{Z}_p$ is a field.

**Example 2** (p. 213): $\{0, 2, 4, 6, 8, 10\}$ is a maximal ideal in $\mathbb{Z}_{12}$.

# Relationships

## Builds Upon
- **Ideal** — A maximal ideal is a maximal proper ideal

## Enables
- **Field** — $R/M$ is a field when $M$ is maximal

## Contrasts With
- **Prime ideal** — Every maximal ideal is prime, but not every prime ideal is maximal (in general)

# Common Errors

- **Error**: Assuming every prime ideal is maximal
  **Correction**: In $\mathbb{Z}[x]$, $\langle x \rangle$ is prime (since $\mathbb{Z}[x]/\langle x \rangle \cong \mathbb{Z}$ is an integral domain) but not maximal (since $\mathbb{Z}$ is not a field)

# Common Confusions

- **Confusion**: Thinking "maximal" means "largest ideal"
  **Clarification**: A maximal ideal is a proper ideal not contained in any other proper ideal; $R$ itself is always the largest ideal but is not "proper"

# Source Reference

Chapter 16: Rings, Section 16.4, pages 212-213. See Theorem 16.35 and Corollary 16.40.

# Verification Notes

- Definition source: Direct quote from p. 212
- Confidence: HIGH — explicit definition with characterization theorem
- Cross-reference status: Verified
- Uncertainties: None
