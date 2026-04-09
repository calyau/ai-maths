---
concept: Nontrivial Center of p-Groups
slug: nontrivial-center-of-p-group
category: group-structure
subcategory: p-group-theory
tier: advanced
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Group Actions"
chapter_number: 14
pdf_page: 184
section: "The Class Equation"
extraction_confidence: high
aliases: []
prerequisites:
  - class-equation
  - p-group
  - center-of-group
extends: []
related:
  - groups-of-order-p-squared
  - cauchys-theorem
contrasts_with: []
answers_questions:
  - "Why does every p-group have a nontrivial center?"
---

# Quick Definition

Every group of order $p^n$ (where $p$ is prime) has a nontrivial center. This follows from the class equation, since $p$ divides every nontrivial conjugacy class size and divides $|G|$, forcing $p | |Z(G)|$.

# Core Definition

**Theorem 14.15**: "Let $G$ be a group of order $p^n$ where $p$ is prime. Then $G$ has a nontrivial center" (Judson, p. 184).

# Prerequisites

- **Class equation** — Tool for the proof
- **$p$-group** — The hypothesis
- **Center of group** — The conclusion

# Key Properties

1. $|Z(G)| \geq p$ for any $p$-group
2. This means no group of order $p^n$ ($n > 1$) is simple
3. Combined with Corollary 14.16: groups of order $p^2$ are abelian

# Context & Application

This result is fundamental to the theory of $p$-groups and is used in proving the Sylow theorems and Cauchy's theorem.

# Relationships

## Builds Upon
- **Class equation** — The proof mechanism

## Enables
- **Groups of order $p^2$ are abelian** — Direct corollary
- **Cauchy's theorem** — Used in the proof

# Source Reference

Chapter 14: Group Actions, Section 14.2, p. 184. Theorem 14.15.

# Verification Notes

- Definition source: Theorem 14.15
- Confidence: HIGH
