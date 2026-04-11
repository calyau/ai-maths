---
concept: Commutative Ring
slug: commutative-ring
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
  - "abelian ring"
prerequisites:
  - ring
extends:
  - ring
related:
  - integral-domain
  - field
  - ring-with-identity
contrasts_with:
  - matrix-ring
  - hamilton-quaternions
answers_questions:
  - "What is a commutative ring?"
  - "What distinguishes a commutative ring from a general ring?"
---

# Quick Definition
A commutative ring is a ring in which multiplication is commutative: $ab = ba$ for all elements $a, b$.

# Core Definition
The ring R is *commutative* if multiplication is commutative, i.e., $ab = ba$ for all $a, b \in R$ (Dummit & Foote, p. 223, Definition (2)).

# Prerequisites
- **Ring** — A commutative ring is a ring with an additional property on multiplication

# Key Properties
1. All ring axioms hold
2. Multiplication is commutative: $ab = ba$ for all $a, b \in R$
3. Left and right ideals coincide (every left ideal is a right ideal and vice versa)
4. The notions of left and right multiplication by ring elements are the same

# Construction / Recognition
## To Recognize:
1. Verify R is a ring
2. Check that $ab = ba$ for all $a, b \in R$

# Context & Application
Most rings encountered in number theory and algebraic geometry are commutative. The theory of commutative rings is the algebraic foundation for algebraic geometry and algebraic number theory. Much of Chapters 7-9 focuses on commutative rings (Dummit & Foote, p. 223).

# Examples
**Example 1** (p. 224): $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$ are all commutative rings.

**Example 2** (p. 224): $\mathbb{Z}/n\mathbb{Z}$ is a commutative ring for all $n \geq 2$.

**Example 3** (p. 225): The Hamilton Quaternions $\mathbb{H}$ are a ring that is *not* commutative.

# Relationships

## Builds Upon
- **ring** — A commutative ring is a ring with commutative multiplication

## Enables
- **integral-domain** — A commutative ring with identity and no zero divisors
- **field** — A commutative division ring
- **prime-ideal** — Defined for commutative rings

## Contrasts With
- **matrix-ring** — $M_n(R)$ for $n \geq 2$ is never commutative (when R is nontrivial)
- **hamilton-quaternions** — A noncommutative division ring

# Common Errors
- **Error**: Assuming all rings are commutative
  **Correction**: Matrix rings and group rings of nonabelian groups are noncommutative

# Common Confusions
- **Confusion**: Thinking "commutative ring" means all operations are commutative
  **Clarification**: Addition is always commutative in any ring; "commutative ring" refers specifically to commutativity of multiplication

# Source Reference
Chapter 7: Introduction to Rings, Section 7.1, Definition (2), page 223.

# Verification Notes
- Definition: Direct from p. 223
- Confidence: HIGH — single-sentence explicit definition
