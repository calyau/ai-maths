---
concept: Ideal-Quotient Correspondence
slug: ideal-quotient-correspondence
category: ring-theory
subcategory: structure-theorems
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 245
section: "7.3 Ring Homomorphisms and Quotient Rings"
extraction_confidence: high
aliases:
  - "ideal-kernel correspondence"
prerequisites:
  - ideal
  - ring-homomorphism
  - quotient-ring
extends: []
related:
  - first-isomorphism-theorem-rings
  - lattice-isomorphism-theorem-rings
contrasts_with: []
answers_questions:
  - "How are ideals related to ring homomorphisms?"
  - "What is the correspondence between ideals and kernels?"
---

# Quick Definition
Every ideal is the kernel of a ring homomorphism (namely the natural projection), and every kernel of a ring homomorphism is an ideal. This establishes a perfect correspondence.

# Core Definition
(Theorem 7(2)) If I is any ideal of R, then the natural projection $R \to R/I$ defined by $r \mapsto r + I$ is a surjective ring homomorphism with kernel I. Thus every ideal is the kernel of a ring homomorphism, and conversely, every kernel is an ideal (Dummit & Foote, p. 246).

# Prerequisites
- **Ideal** — The correspondence involves ideals
- **Ring homomorphism** — Ideals = kernels
- **Quotient ring** — The natural projection $R \to R/I$

# Key Properties
1. Ideal $\Leftrightarrow$ kernel of ring homomorphism (complete correspondence)
2. Analogous to: normal subgroup $\Leftrightarrow$ kernel of group homomorphism
3. This justifies studying ideals as the "right" notion for forming quotients

# Context & Application
This correspondence is the foundation for all of ring theory. It shows that ideals play exactly the same role for rings as normal subgroups play for groups.

# Source Reference
Chapter 7, Section 7.3, Theorem 7, page 246.

# Verification Notes
- Definition: Direct from Theorem 7(2), p. 246
- Confidence: HIGH — fundamental result
