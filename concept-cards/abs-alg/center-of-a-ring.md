---
concept: Center of a Ring
slug: center-of-a-ring
category: ring-theory
subcategory: basic-definitions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 233
section: "7.1 Basic Definitions and Examples"
extraction_confidence: high
aliases: []
prerequisites:
  - ring
  - subring
extends: []
related:
  - commutative-ring
  - hamilton-quaternions
contrasts_with: []
answers_questions:
  - "What is the center of a ring?"
---

# Quick Definition
The center of a ring R is $Z(R) = \{z \in R \mid zr = rz \text{ for all } r \in R\}$, the set of elements that commute with everything. It is a subring containing the identity.

# Core Definition
The *center* of a ring R is $\{z \in R \mid zr = rz \text{ for all } r \in R\}$. The center is a subring that contains the identity. The center of a division ring is a field (Exercise 7, Dummit & Foote, p. 233).

# Prerequisites
- **Ring** — The center is defined for any ring
- **Subring** — The center is a subring

# Key Properties
1. $Z(R)$ is a commutative subring containing the identity (Exercise 7)
2. $Z(D)$ is a field when D is a division ring (Exercise 7)
3. $Z(\mathbb{H}) = \mathbb{R}$ (the real scalars) (Exercise 8, p. 233)
4. $Z(M_n(R)) = $ scalar matrices when R is commutative (Exercise 7, p. 240)

# Source Reference
Chapter 7, Section 7.1, Exercise 7, page 233.

# Verification Notes
- Definition: From Exercise 7, p. 233
- Confidence: HIGH — standard definition
