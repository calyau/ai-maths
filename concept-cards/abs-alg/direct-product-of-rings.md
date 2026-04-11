---
concept: Direct Product of Rings
slug: direct-product-of-rings
category: ring-theory
subcategory: ring-constructions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 265
section: "7.6 The Chinese Remainder Theorem"
extraction_confidence: high
aliases:
  - "ring direct product"
prerequisites:
  - ring
extends: []
related:
  - chinese-remainder-theorem
contrasts_with: []
answers_questions:
  - "What is the direct product of rings?"
---

# Quick Definition
The direct product $R_1 \times R_2$ of rings is the set of ordered pairs $(r_1, r_2)$ with componentwise addition and multiplication.

# Core Definition
The (ring) direct product of $R_1$ and $R_2$ is defined as their direct product as abelian groups with multiplication defined componentwise: $(r_1, r_2)(s_1, s_2) = (r_1s_1, r_2s_2)$ (Dummit & Foote, p. 265).

# Prerequisites
- **Ring** — Both factors are rings

# Key Properties
1. $R_1 \times R_2$ is commutative iff both $R_1$ and $R_2$ are commutative
2. $R_1 \times R_2$ has identity iff both $R_1$ and $R_2$ have identities
3. Units of $R_1 \times R_2$ are pairs of units: $(R_1 \times R_2)^{\times} = R_1^{\times} \times R_2^{\times}$
4. If $R_1$ and $R_2$ are nonzero, $R_1 \times R_2$ is never a field (Exercise 4, p. 269)
5. Every ideal of $R \times S$ has the form $I \times J$ (Exercise 3, p. 269)

# Examples
**Example**: $\mathbb{Z}/6\mathbb{Z} \cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/3\mathbb{Z}$ by the Chinese Remainder Theorem.

# Relationships

## Related
- **chinese-remainder-theorem** — Produces direct products from quotients by comaximal ideals

# Source Reference
Chapter 7, Section 7.6, page 265.

# Verification Notes
- Definition: Direct from p. 265
- Confidence: HIGH — explicit definition
