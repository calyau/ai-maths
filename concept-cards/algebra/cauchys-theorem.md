---
concept: "Cauchy's Theorem"
slug: cauchys-theorem
category: group-theory
subcategory: sylow-theory
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "More Group Theory"
chapter_number: 7
pdf_page: 206
section: "7.7 The Sylow Theorems"
extraction_confidence: high
aliases: []
prerequisites:
  - first-sylow-theorem
extends: []
related:
  - sylow-p-subgroup
contrasts_with: []
answers_questions:
  - "Does a group of order divisible by p contain an element of order p?"
---

# Quick Definition

Cauchy's Theorem: A finite group whose order is divisible by a prime p contains an element of order p. This follows immediately from the First Sylow Theorem.

# Core Definition

A finite group whose order is divisible by a prime p contains an element of order p (Artin, Corollary 7.7.3, p. 217). Proof: Let H be a Sylow p-subgroup. H contains an element x of order p^k for some k >= 1. Then x^{p^{k-1}} has order p.

# Prerequisites

- **First Sylow theorem** — Cauchy's theorem is a corollary

# Key Properties

1. If p | |G|, then G contains an element of order p
2. Stronger than just knowing the order of elements divides |G| (Lagrange)
3. A group of order 6, for instance, MUST have elements of orders 2 and 3

# Context & Application

Cauchy's Theorem fills a gap left by Lagrange's theorem: while Lagrange says the order of any element divides |G|, Cauchy says that for each prime divisor p, there actually IS an element of order p. This is not obvious -- one might imagine a group of order 6 with only elements of order 2.

# Examples

**Example 1** (p. 217): A group of order 6 must contain an element of order 3 and an element of order 2 -- it cannot consist of 1 and five elements of order 2.

# Relationships

## Builds Upon
- **First Sylow theorem** — Immediate corollary

# Source Reference

Chapter 7: More Group Theory, Section 7.7, Corollary 7.7.3, p. 217.

# Verification Notes

- Definition source: Direct from Corollary 7.7.3
- Confidence rationale: Named theorem, explicitly stated
- Uncertainties: None
- Cross-reference status: Verified
