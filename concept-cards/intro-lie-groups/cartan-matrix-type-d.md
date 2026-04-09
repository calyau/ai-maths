---
# === CORE IDENTIFICATION ===
concept: Cartan Matrix of Type D_n
slug: cartan-matrix-type-d

# === CLASSIFICATION ===
category: classification
subcategory: type-d
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Appendix C - Root Systems and Simple Lie Algebras"
chapter_number: null
pdf_page: 128
section: "C.4 D_n = so(2n,C)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - simple-roots-type-d
  - cartan-matrix
extends: []
related:
  - dynkin-diagram-type-d
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Cartan matrix of type D_n?"
---

# Quick Definition
The Cartan matrix of $D_n$ is symmetric (simply laced) with the standard tridiagonal pattern for nodes 1 through $n-2$, plus the fork: $a_{n-2,n} = a_{n,n-2} = -1$ and $a_{n-1,n} = a_{n,n-1} = 0$.

# Core Definition
(Kirillov, p. 128):

$$A = \begin{pmatrix} 2 & -1 & & & & \\ -1 & 2 & -1 & & & \\ & \ddots & \ddots & \ddots & & \\ & & -1 & 2 & -1 & -1 \\ & & & -1 & 2 & 0 \\ & & & -1 & 0 & 2 \end{pmatrix}$$

# Prerequisites
- **Simple roots type D** -- entries from simple root pairings
- **Cartan matrix** -- general concept

# Key Properties
1. Symmetric (simply laced)
2. The last two rows/columns reflect the fork: node $n-2$ connects to both $n-1$ and $n$
3. $a_{n-1,n} = a_{n,n-1} = 0$ (the two fork nodes are not connected)
4. $\det A = 4$ for even $n$ (since $P/Q \cong \mathbb{Z}_2 \times \mathbb{Z}_2$)

# Source Reference
Appendix C, Section C.4, p. 128.

# Verification Notes
- Definition source: Direct from p. 128
- Confidence rationale: Explicit matrix
- Uncertainties: None
- Cross-reference status: Verified
