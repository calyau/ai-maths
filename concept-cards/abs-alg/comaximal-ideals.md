---
concept: Comaximal Ideals
slug: comaximal-ideals
category: ring-theory
subcategory: ideals
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
  - "coprime ideals"
  - "relatively prime ideals"
prerequisites:
  - ideal
  - ring-with-identity
extends: []
related:
  - chinese-remainder-theorem
  - sum-of-ideals
contrasts_with: []
answers_questions:
  - "What does it mean for two ideals to be comaximal?"
---

# Quick Definition
Two ideals A and B of a ring R are comaximal if $A + B = R$.

# Core Definition
The ideals A and B of the ring R are said to be *comaximal* if $A + B = R$ (Dummit & Foote, p. 265). This generalizes the notion of relatively prime integers.

# Prerequisites
- **Ideal** — Comaximality is defined for ideals
- **Ring with identity** — $A + B = R$ means $1 \in A + B$, i.e., $a + b = 1$ for some $a \in A$, $b \in B$

# Key Properties
1. In $\mathbb{Z}$: $(m)$ and $(n)$ are comaximal iff $\gcd(m, n) = 1$
2. If A and B are comaximal, then $AB = A \cap B$
3. The CRT requires pairwise comaximal ideals

# Examples
**Example 1**: $3\mathbb{Z}$ and $5\mathbb{Z}$ are comaximal in $\mathbb{Z}$ since $3(2) + 5(-1) = 1$.

**Example 2**: $2\mathbb{Z}$ and $4\mathbb{Z}$ are NOT comaximal since $2\mathbb{Z} + 4\mathbb{Z} = 2\mathbb{Z} \neq \mathbb{Z}$.

# Relationships

## Related
- **chinese-remainder-theorem** — Requires pairwise comaximal ideals
- **sum-of-ideals** — $A + B = R$ is the comaximality condition

# Source Reference
Chapter 7, Section 7.6, Definition on page 265.

# Verification Notes
- Definition: Direct from p. 265
- Confidence: HIGH — explicit definition
