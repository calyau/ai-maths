---
concept: Algebraic Closure
slug: algebraic-closure
category: field-theory
subcategory: splitting-fields
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Field Theory"
chapter_number: 13
pdf_page: 540
section: "13.4 Splitting Fields and Algebraic Closures"
extraction_confidence: high
aliases:
  - "algebraically closed field"
prerequisites:
  - algebraic-extension
  - splitting-field
extends: []
related:
  - fundamental-theorem-algebra
contrasts_with: []
answers_questions:
  - "What is an algebraic closure?"
  - "What is an algebraically closed field?"
---

# Quick Definition
A field F is algebraically closed if every non-constant polynomial in F[x] has a root in F. The algebraic closure $\bar{F}$ of F is the smallest algebraically closed field containing F; it is unique up to isomorphism.

# Core Definition
A field F is algebraically closed if every non-constant polynomial in F[x] splits into linear factors (equivalently, every irreducible polynomial has degree 1). The algebraic closure $\bar{F}$ of F is an algebraic extension of F that is algebraically closed. It exists and is unique up to F-isomorphism. $\mathbb{C}$ is the algebraic closure of $\mathbb{R}$ (by the Fundamental Theorem of Algebra), and $\bar{\mathbb{Q}}$ (algebraic numbers) is the algebraic closure of $\mathbb{Q}$ (Dummit & Foote, pp. 540-543).

# Prerequisites
- **algebraic-extension** — $\bar{F}$ is algebraic over F
- **splitting-field** — $\bar{F}$ is the "universal" splitting field

# Key Properties
1. $\bar{F}$ is algebraically closed and algebraic over F
2. $\bar{F}$ is unique up to F-isomorphism
3. $\mathbb{C}$ is algebraically closed (FTA)
4. $\bar{\mathbb{Q}} \subset \mathbb{C}$ is countable; $\mathbb{C}$ is uncountable

# Relationships
## Builds Upon
- **algebraic-extension**, **splitting-field**

# Source Reference
Chapter 13, Section 13.4, pp. 540-543.

# Verification Notes
- Confidence: HIGH — explicit definition with existence/uniqueness
