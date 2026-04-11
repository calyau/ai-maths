---
concept: "R[x] is a PID iff R is a Field"
slug: rx-pid-iff-r-field
category: ring-theory
subcategory: structure-theorems
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Euclidean Domains, Principal Ideal Domains, and Unique Factorization Domains"
chapter_number: 8
pdf_page: 284
section: "8.2 Principal Ideal Domains (P.I.D.s)"
extraction_confidence: high
aliases: []
prerequisites:
  - polynomial-ring
  - principal-ideal-domain
  - field
extends: []
related:
  - polynomial-ring-over-field
  - domain-hierarchy
contrasts_with: []
answers_questions:
  - "When is R[x] a PID?"
  - "Why is Z[x] not a PID?"
---

# Quick Definition
$R[x]$ is a PID if and only if R is a field. In particular, $\mathbb{Z}[x]$ is not a PID.

# Core Definition
(Corollary 8) If R is any commutative ring such that $R[x]$ is a PID (or Euclidean Domain), then R is necessarily a field. Proof: $(x)$ is a nonzero prime ideal in $R[x]$ (since $R[x]/(x) \cong R$ is an integral domain), hence maximal by Proposition 7, so $R \cong R[x]/(x)$ is a field (Dummit & Foote, p. 284).

# Prerequisites
- **Polynomial ring** — About the structure of $R[x]$
- **Principal ideal domain** — Whether $R[x]$ is a PID
- **Field** — The characterization of when this holds

# Key Properties
1. Forward: R field $\Rightarrow$ $R[x]$ Euclidean (by polynomial division) $\Rightarrow$ PID
2. Converse: $R[x]$ PID $\Rightarrow$ R field (via the ideal $(x)$)
3. Contrast: R UFD $\Leftrightarrow$ $R[x]$ UFD (Theorem 7), but PID does NOT transfer

# Examples
**Example 1**: $\mathbb{Q}[x]$ is a PID ($\mathbb{Q}$ is a field).

**Example 2**: $\mathbb{Z}[x]$ is NOT a PID ($\mathbb{Z}$ is not a field; $(2, x)$ is not principal).

# Source Reference
Chapter 8, Section 8.2, Corollary 8, page 284.

# Verification Notes
- Definition: Direct from Corollary 8, p. 284
- Confidence: HIGH — explicit corollary with proof
