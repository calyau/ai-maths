---
concept: Hamilton Quaternions
slug: hamilton-quaternions
category: ring-theory
subcategory: basic-definitions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 224
section: "7.1 Basic Definitions and Examples"
extraction_confidence: high
aliases:
  - "real quaternions"
  - "quaternion algebra"
prerequisites:
  - ring
  - division-ring
extends:
  - division-ring
related:
  - field
  - group-ring
contrasts_with:
  - field
  - commutative-ring
answers_questions:
  - "What are the Hamilton Quaternions?"
  - "What is an example of a noncommutative division ring?"
---

# Quick Definition
The Hamilton Quaternions $\mathbb{H}$ are the set $\{a + bi + cj + dk \mid a,b,c,d \in \mathbb{R}\}$ with $i^2 = j^2 = k^2 = -1$, $ij = k$, $ji = -k$, etc. They form a noncommutative division ring.

# Core Definition
Let $\mathbb{H}$ be the collection of elements $a + bi + cj + dk$ where $a, b, c, d \in \mathbb{R}$, with componentwise addition and multiplication defined by $i^2 = j^2 = k^2 = -1$, $ij = -ji = k$, $jk = -kj = i$, $ki = -ik = j$. The Hamilton Quaternions are a noncommutative ring with identity ($1 = 1+0i+0j+0k$), and a division ring with inverses $(a+bi+cj+dk)^{-1} = \frac{a-bi-cj-dk}{a^2+b^2+c^2+d^2}$ (Dummit & Foote, pp. 224-225).

# Prerequisites
- **Ring** — $\mathbb{H}$ is a ring
- **Division ring** — $\mathbb{H}$ is a division ring

# Key Properties
1. $\mathbb{H}$ is a noncommutative division ring
2. The center of $\mathbb{H}$ is $\mathbb{R}$ (the real scalars)
3. $\mathbb{H}^{\times} = \mathbb{H} - \{0\}$ (every nonzero element is a unit)
4. $\mathbb{H}$ contains a copy of $\mathbb{C}$ as a subring (e.g., $\{a + bi\}$)
5. The integral quaternions $\mathbb{Z}[1,i,j,k]$ form a subring

# Examples
**Example** (p. 225): $(1+i+2j)(j+k) = -2 + 2i + 2k$.

# Relationships

## Builds Upon
- **division-ring** — $\mathbb{H}$ is the prototypical noncommutative division ring

## Contrasts With
- **field** — $\mathbb{H}$ is a division ring that is NOT a field (not commutative)
- **commutative-ring** — $\mathbb{H}$ is noncommutative

# Source Reference
Chapter 7, Section 7.1, Example (5), pages 224-225.

# Verification Notes
- Definition: Direct from pp. 224-225
- Confidence: HIGH — explicit construction
