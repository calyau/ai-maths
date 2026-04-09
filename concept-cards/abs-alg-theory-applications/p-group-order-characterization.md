---
concept: p-Group Order Characterization
slug: p-group-order-characterization
category: group-structure
subcategory: group-classification
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
  - p-group
  - lagranges-theorem
  - cauchy-lemma-for-abelian-groups
extends:
  - p-group
related:
  - cauchys-theorem
contrasts_with: []
answers_questions:
  - "When is a finite group a p-group?"
---

# Quick Definition

A finite abelian group is a $p$-group if and only if its order is a power of $p$. For general finite groups, this follows from Corollary 15.2 (Cauchy's Theorem).

# Core Definition

**Lemma 13.7**: "A finite abelian group is a $p$-group if and only if its order is a power of $p$" (Judson, p. 173). If $|G| = p^n$ then by Lagrange's theorem every element order divides $p^n$. Conversely, if $|G|$ has a prime divisor $q \neq p$, Lemma 13.6 gives an element of order $q$.

# Prerequisites

- **$p$-group** — Subject of characterization
- **Lagrange's theorem** — Orders divide $|G|$
- **Cauchy's Lemma for abelian groups** — Provides elements of prime order

# Key Properties

1. For finite abelian groups: $G$ is a $p$-group $\iff$ $|G| = p^n$
2. Extended to all finite groups by Corollary 15.2

# Relationships

## Builds Upon
- **$p$-group** — Characterizes these groups

# Source Reference

Chapter 13: The Structure of Groups, Section 13.1, p. 173. Lemma 13.7.

# Verification Notes

- Definition source: Lemma 13.7
- Confidence: HIGH
