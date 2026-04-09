---
concept: Cauchy's Lemma for Abelian Groups
slug: cauchy-lemma-for-abelian-groups
category: group-structure
subcategory: classification-theorems
tier: advanced
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "The Structure of Groups"
chapter_number: 13
pdf_page: 173
section: "Finite Abelian Groups"
extraction_confidence: high
aliases: []
prerequisites:
  - lagranges-theorem
  - p-group
extends: []
related:
  - cauchys-theorem
  - fundamental-theorem-of-finite-abelian-groups
contrasts_with: []
answers_questions:
  - "Does a finite abelian group have an element of prime order p when p divides its order?"
---

# Quick Definition

If $G$ is a finite abelian group and $p$ is a prime dividing $|G|$, then $G$ contains an element of order $p$. This is the abelian case of Cauchy's Theorem, proved by induction as Lemma 13.6.

# Core Definition

**Lemma 13.6**: "Let $G$ be a finite abelian group of order $n$. If $p$ is a prime that divides $n$, then $G$ contains an element of order $p$" (Judson, p. 173).

# Prerequisites

- **Lagrange's theorem** — Used in the inductive proof
- **$p$-group** — Related concept

# Key Properties

1. Uses induction on $|G|$
2. If $G$ has no proper nontrivial subgroups, $|G|$ must be prime
3. If $p | |H|$ for a proper subgroup $H$, done by induction
4. Otherwise, $p | |G/H|$ and induction applies to the quotient
5. This is a special case of Cauchy's Theorem (Theorem 15.1)

# Relationships

## Enables
- **Fundamental Theorem of Finite Abelian Groups** — Building block of the proof

## Related
- **Cauchy's theorem** — General version (for all finite groups)

# Source Reference

Chapter 13: The Structure of Groups, Section 13.1, p. 173. Lemma 13.6.

# Verification Notes

- Definition source: Lemma 13.6
- Confidence: HIGH — complete proof given
