---
concept: Jordan Block
slug: jordan-block
category: linear-algebra
subcategory: canonical-forms
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Modules over Principal Ideal Domains"
chapter_number: 12
pdf_page: 491
section: "12.3 The Jordan Canonical Form"
extraction_confidence: high
aliases:
  - "Jordan cell"
prerequisites:
  - matrix-of-linear-transformation
extends: []
related:
  - jordan-canonical-form
  - generalized-eigenspace
contrasts_with: []
answers_questions:
  - "What is a Jordan block?"
---

# Quick Definition
A Jordan block $J_k(\lambda)$ is a $k \times k$ matrix with eigenvalue $\lambda$ on the main diagonal, 1's on the superdiagonal, and zeros elsewhere. It represents the action of T on the cyclic module $F[x]/(x - \lambda)^k$.

# Core Definition
The Jordan block $J_k(\lambda)$ is the $k \times k$ matrix $\lambda I + N$ where N has 1's on the superdiagonal and zeros elsewhere. It corresponds to the elementary divisor $(x - \lambda)^k$ in the structure theorem. The Jordan canonical form is a block diagonal matrix of Jordan blocks (Dummit & Foote, p. 491).

# Prerequisites
- **matrix-of-linear-transformation**

# Key Properties
1. $J_k(\lambda)$ has eigenvalue $\lambda$ with algebraic multiplicity k and geometric multiplicity 1
2. $J_k(\lambda) - \lambda I$ is nilpotent of order k
3. $J_1(\lambda) = (\lambda)$ is a $1 \times 1$ block (diagonal entry)

# Relationships
## Enables
- **jordan-canonical-form** — Built from Jordan blocks

# Source Reference
Chapter 12, Section 12.3, pp. 491-493.

# Verification Notes
- Confidence: HIGH — explicit definition
