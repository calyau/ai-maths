---
# === CORE IDENTIFICATION ===
concept: Congruence Modulo n
slug: congruence-modulo-n

# === CLASSIFICATION ===
category: foundations
subcategory: number-theory
tier: foundational

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Preliminaries"
chapter_number: 1
pdf_page: 26
section: "Equivalence Relations and Partitions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - congruence mod n
  - modular congruence

# === TYPED RELATIONSHIPS ===
prerequisites:
  - equivalence-relation
  - divisibility
extends:
  - equivalence-relation
related:
  - integers-mod-n
  - equivalence-class
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
---

# Quick Definition

Two integers $r$ and $s$ are congruent modulo $n$, written $r \equiv s \pmod{n}$, if $n$ divides $r - s$. This defines an equivalence relation on $\mathbb{Z}$.

# Core Definition

"Let $r$ and $s$ be two integers and suppose that $n \in \mathbb{N}$. We say that $r$ is congruent to $s$ modulo $n$, or $r$ is congruent to $s$ mod $n$, if $r - s$ is evenly divisible by $n$; that is, $r - s = nk$ for some $k \in \mathbb{Z}$. In this case we write $r \equiv s \pmod{n}$" (Judson, p. 26).

# Prerequisites

- **Equivalence relation** — Congruence mod $n$ is an equivalence relation
- **Divisibility** — Defined in terms of divisibility

# Key Properties

1. **Reflexive**: $r - r = 0$ is divisible by $n$
2. **Symmetric**: If $r - s = nk$, then $s - r = n(-k)$
3. **Transitive**: If $r - s = nk$ and $s - t = nl$, then $r - t = n(k + l)$
4. Partitions $\mathbb{Z}$ into exactly $n$ equivalence classes

# Construction / Recognition

## To Check if $r \equiv s \pmod{n}$:
1. Compute $r - s$
2. Check if $n$ divides $r - s$ (i.e., the remainder is 0)

# Context & Application

Congruence modulo $n$ is the foundation for constructing the integers mod $n$ ($\mathbb{Z}_n$), which is one of the most important examples of a group in abstract algebra. It is also essential in cryptography and coding theory.

# Examples

**Example 1** (p. 26): $41 \equiv 17 \pmod{8}$ since $41 - 17 = 24$ is divisible by 8.

**Example 2** (p. 26): The equivalence classes modulo 3 are:
- $[0] = \{\ldots, -3, 0, 3, 6, \ldots\}$
- $[1] = \{\ldots, -2, 1, 4, 7, \ldots\}$
- $[2] = \{\ldots, -1, 2, 5, 8, \ldots\}$

# Relationships

## Builds Upon
- **equivalence-relation** — Congruence is a specific equivalence relation

## Enables
- **integers-mod-n** — $\mathbb{Z}_n$ is the set of equivalence classes under congruence mod $n$
- **modular-arithmetic** — Arithmetic operations on congruence classes

# Common Errors

- **Error**: Writing $r \equiv s \pmod{n}$ when $r - s$ is not divisible by $n$
  **Correction**: Verify divisibility; e.g., $7 \not\equiv 3 \pmod{5}$ since $7 - 3 = 4$ is not divisible by 5

# Common Confusions

- **Confusion**: Confusing $r \equiv s \pmod{n}$ with $r = s$
  **Clarification**: Congruence is a weaker relation than equality; many different integers can be congruent mod $n$

# Source Reference

Chapter 1: Preliminaries, Section 1.2, Example 1.30, page 26.

# Verification Notes

- Definition source: Direct quote from p. 26
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
