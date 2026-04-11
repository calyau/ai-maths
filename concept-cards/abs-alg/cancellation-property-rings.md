---
concept: Cancellation Property in Rings
slug: cancellation-property-rings
category: ring-theory
subcategory: basic-definitions
tier: foundational
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 229
section: "7.1 Basic Definitions and Examples"
extraction_confidence: high
aliases:
  - "cancellation law"
prerequisites:
  - ring
  - zero-divisor
extends: []
related:
  - integral-domain
contrasts_with: []
answers_questions:
  - "When can we cancel in a ring?"
  - "What is the cancellation property in rings?"
---

# Quick Definition
In a ring, if a is not a zero divisor and $ab = ac$, then either $a = 0$ or $b = c$. In an integral domain, cancellation always holds for nonzero elements.

# Core Definition
(Proposition 2) If $a, b, c$ are elements of any ring with a not a zero divisor, and $ab = ac$, then either $a = 0$ or $b = c$. In particular, in an integral domain, if $ab = ac$ then $a = 0$ or $b = c$ (Dummit & Foote, p. 229).

# Prerequisites
- **Ring** — The cancellation law applies in rings
- **Zero divisor** — Cancellation fails for zero divisors

# Key Properties
1. Cancellation holds when a is not a zero divisor
2. In integral domains: cancellation holds for all nonzero elements
3. Proof: $ab = ac \Rightarrow a(b-c) = 0$; if a is not a zero divisor, $b = c$
4. Any finite integral domain is a field (Corollary 3, uses cancellation)

# Source Reference
Chapter 7, Section 7.1, Proposition 2, page 229.

# Verification Notes
- Definition: Direct from Proposition 2, p. 229
- Confidence: HIGH — explicit proposition
