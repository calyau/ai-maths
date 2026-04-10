---
concept: Hausdorff Series
slug: hausdorff-series
category: lie-algebras
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Lie Algebras and Algebraic Groups"
chapter_number: 2
pdf_page: 273
section: "4a Preliminaries on Lie algebras"
extraction_confidence: high
aliases:
  - "Baker-Campbell-Hausdorff formula"
  - "BCH formula"
prerequisites:
  - nilpotent-lie-algebra
extends: []
related:
  - unipotent-nilpotent-equivalence
contrasts_with: []
answers_questions:
  - "How does the Lie algebra functor connect algebraic groups to Lie algebras?"
---

# Quick Definition

The Hausdorff series H(X,Y) expresses exp(X).exp(Y) = exp(H(X,Y)) for nilpotent matrices. It begins H^1 = X + Y, H^2 = (1/2)[X,Y], and involves only iterated Lie brackets with rational coefficients.

# Core Definition

The **Hausdorff series** is a formal power series H(X,Y) = sum_{n>0} H^n(X,Y) with rational coefficients, where H^n is homogeneous of degree n, satisfying exp(X).exp(Y) = exp(H(X,Y)) for nilpotent matrices (Milne, p. 273). For a nilpotent Lie algebra g (char 0), H^n(x,y) = 0 for large n, giving a well-defined group structure on g.

# Prerequisites

- **Nilpotent Lie algebra** -- The series converges for nilpotent algebras

# Key Properties

1. H^1(X,Y) = X + Y, H^2(X,Y) = (1/2)[X,Y]
2. All terms involve only iterated Lie brackets with rational coefficients
3. For a nilpotent Lie algebra over a field of char 0, this defines a unipotent group structure on g_a

# Context & Application

The Hausdorff series provides the explicit equivalence between nilpotent Lie algebras and unipotent algebraic groups in characteristic zero (Theorem 4.7). The group multiplication on the vector space g is given by the Hausdorff formula.

# Examples

**Example 1** (p. 273): For nilpotent matrices X, Y in M_n(k) (char 0), exp(X).exp(Y) = exp(H(X,Y)).

# Relationships

## Enables
- **Unipotent-nilpotent equivalence** -- Provides the group structure on nilpotent Lie algebras

# Source Reference

Chapter II: Lie Algebras and Algebraic Groups, Section 4a, pages 273-274.

# Verification Notes

- Definition source: Direct from p. 273
- Confidence rationale: Explicit formula
- Uncertainties: None
- Cross-reference status: Verified
