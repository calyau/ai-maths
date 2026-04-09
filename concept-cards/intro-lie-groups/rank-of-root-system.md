---
# === CORE IDENTIFICATION ===
concept: Rank of Root System
slug: rank-of-root-system

# === CLASSIFICATION ===
category: root-systems
subcategory: abstract-root-systems
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Root Systems"
chapter_number: 8
pdf_page: 90
section: "8.1. Abstract root systems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "rank"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - abstract-root-system
extends: []
related:
  - simple-roots
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the rank of a root system?"
---

# Quick Definition
The rank of a root system $R \subset E$ is $r = \dim E$, the dimension of the ambient Euclidean space. It equals the number of simple roots.

# Core Definition
The number $r = \dim E$ is called the rank of $R$ (Definition 8.1, p. 90). Since simple roots form a basis of $E$ (Theorem 8.16, p. 95), the rank equals $|\Pi|$, the number of simple roots.

# Prerequisites
- **abstract-root-system** -- rank is a property of a root system

# Key Properties
1. Rank equals $\dim E$
2. Rank equals the number of simple roots $|\Pi|$ (Theorem 8.16)
3. Rank equals the size of the Cartan matrix and the number of vertices in the Dynkin diagram
4. For $A_{n-1}$: rank $= n-1$ (Example 8.4, p. 91)

# Construction / Recognition
The rank can be read off from the Dynkin diagram as the number of vertices, or computed as the dimension of the span of the roots.

# Context & Application
Rank is the primary size parameter for root systems. The classification (Theorem 8.49) lists root systems by type and rank, e.g., $A_n$ has rank $n$, $B_n$ has rank $n$.

# Examples
**Example** (p. 91): The root system $A_{n-1} = \{e_i - e_j\} \subset E$ where $E = \{\lambda \in \mathbb{R}^n \mid \sum\lambda_i = 0\}$ has rank $n-1$ (since $\dim E = n-1$). The subscript in $A_{n-1}$ matches the rank.

# Relationships
## Builds Upon
- **abstract-root-system**

## Enables
- **cartan-matrix** -- an $r \times r$ matrix
- **dynkin-diagram** -- has $r$ vertices

## Related
- **simple-roots** -- there are exactly $r$ simple roots

## Contrasts With
(none)

# Common Errors
- **Error**: Confusing the rank with the total number of roots $|R|$
  **Correction**: Rank $= \dim E$, which is much smaller than $|R|$; for $A_{n-1}$, rank $= n-1$ but $|R| = n(n-1)$

# Common Confusions
(none)

# Source Reference
Chapter 8: Root Systems, Section 8.1, page 90. Definition 8.1.

# Verification Notes
- Definition source: Direct from Definition 8.1
- Confidence rationale: HIGH -- explicit definition
- Uncertainties: None
- Cross-reference status: Verified
