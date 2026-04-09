---
# === CORE IDENTIFICATION ===
concept: Ideal
slug: ideal

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
pdf_page: 210
section: "16.3 Ring Homomorphisms and Ideals"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "two-sided ideal"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - ring
  - subring
extends:
  - subring
related:
  - kernel-of-ring-homomorphism
  - factor-ring
  - principal-ideal
contrasts_with:
  - subring

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an ideal of a ring?"
  - "How do ideals relate to quotient rings?"
---

# Quick Definition

An ideal $I$ in a ring $R$ is a subring of $R$ such that for every $a \in I$ and $r \in R$, both $ar \in I$ and $ra \in I$. Ideals are to rings what normal subgroups are to groups.

# Core Definition

"An ideal in a ring $R$ is a subring $I$ of $R$ such that if $a$ is in $I$ and $r$ is in $R$, then both $ar$ and $ra$ are in $I$; that is, $rI \subset I$ and $Ir \subset I$ for all $r \in R$" (Judson, p. 210). Every kernel of a ring homomorphism is an ideal (Proposition 16.27), and every ideal is the kernel of the natural homomorphism $R \to R/I$ (Theorem 16.30).

# Prerequisites

- **Ring** — Ideals are defined within rings
- **Subring** — An ideal is a subring with an extra property

# Key Properties

1. $I$ is a subring of $R$
2. Absorption: $rI \subset I$ and $Ir \subset I$ for all $r \in R$
3. If $R$ has identity and $1 \in I$, then $I = R$
4. Every ring has trivial ideals $\{0\}$ and $R$
5. In a commutative ring, left ideals = right ideals = two-sided ideals
6. The kernel of any ring homomorphism is an ideal

# Construction / Recognition

## To Verify:
1. Check $I$ is nonempty
2. Check $a - b \in I$ for all $a, b \in I$ (subgroup under addition)
3. Check $ra \in I$ and $ar \in I$ for all $a \in I$, $r \in R$ (absorption)

# Context & Application

Ideals are the ring-theoretic analog of normal subgroups. They are exactly the substructures needed to form quotient rings $R/I$. Maximal and prime ideals characterize when quotient rings are fields or integral domains.

# Examples

**Example 1** (p. 210): Every ring $R$ has trivial ideals $\{0\}$ and $R$.

**Example 2** (p. 210): $n\mathbb{Z}$ is an ideal in $\mathbb{Z}$. Every ideal in $\mathbb{Z}$ is of this form (Theorem 16.25).

**Example 3** (p. 210): In a commutative ring with identity, $\langle a \rangle = \{ar : r \in R\}$ is an ideal (a principal ideal).

# Relationships

## Builds Upon
- **Subring** — An ideal is a subring with the absorption property

## Enables
- **Factor ring** — $R/I$ is a ring when $I$ is an ideal
- **Maximal ideal** — An ideal not properly contained in any other proper ideal
- **Prime ideal** — An ideal where $ab \in I$ implies $a \in I$ or $b \in I$

## Related
- **Kernel of ring homomorphism** — Every ideal is a kernel and vice versa
- **Normal subgroup** — The group-theoretic analog

## Contrasts With
- **Subring** — A subring $S$ need not satisfy $rS \subset S$ for all $r \in R$

# Common Errors

- **Error**: Checking only that $I$ is closed under multiplication of its own elements
  **Correction**: Must verify $ra \in I$ for all $r \in R$ (not just $r \in I$); the key property is absorption by the whole ring

# Common Confusions

- **Confusion**: Thinking every subring is an ideal
  **Clarification**: $\mathbb{Z}$ is a subring of $\mathbb{Q}$ but not an ideal of $\mathbb{Q}$ (e.g., $\frac{1}{2} \cdot 1 = \frac{1}{2} \notin \mathbb{Z}$)

# Source Reference

Chapter 16: Rings, Section 16.3, pages 210-211. See Proposition 16.27 and Theorem 16.29.

# Verification Notes

- Definition source: Direct quote from p. 210
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
