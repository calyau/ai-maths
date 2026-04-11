---
concept: Divisibility in Rings
slug: divisibility-in-rings
category: ring-theory
subcategory: factorization
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Euclidean Domains, Principal Ideal Domains, and Unique Factorization Domains"
chapter_number: 8
pdf_page: 275
section: "8.1 Euclidean Domains"
extraction_confidence: high
aliases:
  - "divides"
  - "multiple"
  - "divisor"
prerequisites:
  - commutative-ring
extends: []
related:
  - principal-ideal
  - gcd-in-ring
  - associates
contrasts_with: []
answers_questions:
  - "What does it mean for one element to divide another in a ring?"
  - "How does divisibility relate to ideals?"
---

# Quick Definition
In a commutative ring R, $b$ divides $a$ (written $b \mid a$) if $a = bx$ for some $x \in R$. Equivalently, $a \in (b)$, or $(a) \subseteq (b)$.

# Core Definition
Let R be a commutative ring and $a, b \in R$ with $b \neq 0$. Then a is a *multiple* of b if $a = bx$ for some $x \in R$; in this case b *divides* a, written $b \mid a$ (Dummit & Foote, p. 275).

# Prerequisites
- **Commutative ring** — Divisibility is defined in commutative rings

# Key Properties
1. $b \mid a$ iff $a \in (b)$ iff $(a) \subseteq (b)$
2. $a$ and $b$ are associates iff $a \mid b$ and $b \mid a$ iff $(a) = (b)$
3. u is a unit iff $u \mid 1$ iff $(u) = R$
4. Divisibility gives a partial order on associates classes

# Source Reference
Chapter 8, Section 8.1, Definition, page 275.

# Verification Notes
- Definition: Direct from p. 275
- Confidence: HIGH — explicit definition
