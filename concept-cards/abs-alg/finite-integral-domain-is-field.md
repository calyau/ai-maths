---
concept: Finite Integral Domain is a Field
slug: finite-integral-domain-is-field
category: ring-theory
subcategory: structure-theorems
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 229
section: "7.1 Basic Definitions and Examples"
extraction_confidence: high
aliases:
  - "Wedderburn little theorem (commutative case)"
prerequisites:
  - integral-domain
  - field
extends: []
related:
  - integral-domain
  - field
contrasts_with: []
answers_questions:
  - "Why is every finite integral domain a field?"
---

# Quick Definition
Every finite integral domain is a field. This follows because the cancellation law implies that multiplication by any nonzero element is injective, hence surjective (by finiteness), so every nonzero element has an inverse.

# Core Definition
(Corollary 3) Any finite integral domain is a field. Proof: Let a be nonzero in the finite integral domain R. The map $x \mapsto ax$ is injective (by cancellation). Since R is finite, this map is also surjective. In particular, $ab = 1$ for some b, so a is a unit (Dummit & Foote, p. 229).

# Prerequisites
- **Integral domain** — R must be an integral domain
- **Field** — The conclusion is that R is a field

# Key Properties
1. Shows $\mathbb{Z}/p\mathbb{Z}$ is a field for prime p (as a finite integral domain)
2. Wedderburn's theorem generalizes: a finite division ring (not assumed commutative) is also a field (p. 229)

# Source Reference
Chapter 7, Section 7.1, Corollary 3, page 229.

# Verification Notes
- Definition: Direct from Corollary 3, p. 229
- Confidence: HIGH — explicit corollary with proof
