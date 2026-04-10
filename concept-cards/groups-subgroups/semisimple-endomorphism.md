---
concept: Semisimple Endomorphism
slug: semisimple-endomorphism
category: representations
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 131
section: "10b Application to Jordan decompositions"
extraction_confidence: high
aliases:
  - diagonalizable endomorphism
prerequisites:
  - linear-representation
extends: []
related:
  - jordan-decomposition
  - unipotent-endomorphism
contrasts_with:
  - unipotent-endomorphism
answers_questions:
  - "What is a semisimple endomorphism?"
---

# Quick Definition

An endomorphism alpha of a vector space V is semisimple if it becomes diagonalizable after extending the base field. Equivalently, its minimum polynomial has distinct roots, or the subalgebra k[alpha] of End(V) is separable.

# Core Definition

An endomorphism alpha of a finite-dimensional vector space V is *diagonalizable* if V has a basis of eigenvectors for alpha, and *semisimple* if it becomes diagonalizable after an extension of the base field k. From linear algebra, alpha is semisimple iff its minimum polynomial m_alpha(T) has distinct roots, iff k[alpha] = k[T]/(m_alpha(T)) is a separable k-algebra (Milne, p. 131).

# Prerequisites

- **Linear representation** -- Semisimple endomorphisms arise in representations

# Key Properties

1. Semisimple iff minimum polynomial has distinct roots
2. Semisimple iff k[alpha] is a separable subalgebra of End(V)
3. Diagonalizable iff all eigenvalues lie in k; semisimple iff diagonalizable over k^al
4. The semisimple part alpha_s of any automorphism is a polynomial in alpha (Theorem 10.12)

# Context & Application

Semisimple endomorphisms form one half of the Jordan decomposition. An element of an algebraic group is semisimple when it acts semisimply in every (equivalently, some faithful) representation.

# Examples

**Example 1** (p. 131): The linear map x -> Ax on k^n is semisimple iff there exists P in GL_n(k^al) with PAP^{-1} diagonal.

# Relationships

## Enables
- **Jordan decomposition** -- The semisimple part of the decomposition

## Contrasts With
- **Unipotent endomorphism** -- The other part of the Jordan decomposition

# Source Reference

Chapter I, Section 10b, pages 131-132.

# Verification Notes

- Definition source: Direct from text, p. 131
- Confidence rationale: Standard linear algebra reviewed explicitly
- Uncertainties: None
- Cross-reference status: Verified
