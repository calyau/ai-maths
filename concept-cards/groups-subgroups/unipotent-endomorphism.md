---
concept: Unipotent Endomorphism
slug: unipotent-endomorphism
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
  - unipotent automorphism
prerequisites:
  - linear-representation
extends: []
related:
  - jordan-decomposition
  - unipotent-group
contrasts_with:
  - semisimple-endomorphism
answers_questions:
  - "What is a unipotent endomorphism?"
---

# Quick Definition

An endomorphism alpha of a vector space V is unipotent if id_V - alpha is nilpotent, equivalently, if all eigenvalues of alpha in k^al equal 1. The unipotent elements of GL_n(k) are those matrices whose characteristic polynomial is (T-1)^n.

# Core Definition

An endomorphism alpha of V is *nilpotent* if alpha^m = 0 for some m > 0, and *unipotent* if id_V - alpha is nilpotent. An endomorphism is unipotent iff its eigenvalues in k^al all equal 1, iff its characteristic polynomial is (T-1)^{dim V}. For a unipotent alpha, there exists a basis of V relative to which the matrix of alpha lies in U_n(k), the group of upper triangular matrices with 1's on the diagonal (Milne, p. 131).

# Prerequisites

- **Linear representation** -- Context for unipotent endomorphisms

# Key Properties

1. Unipotent iff all eigenvalues in k^al equal 1
2. Unipotent iff characteristic polynomial is (T-1)^n
3. A set of commuting unipotent endomorphisms can be simultaneously upper-triangularized (Proposition 15.2)
4. The unipotent part alpha_u of any automorphism is a polynomial in alpha

# Context & Application

Unipotent endomorphisms form one component of the Jordan decomposition. Groups consisting entirely of unipotent elements are called unipotent groups.

# Examples

**Example 1** (p. 176): The group U_n of upper unitriangular matrices consists entirely of unipotent elements. The matrix I + N where N is strictly upper triangular is unipotent since N^n = 0.

# Relationships

## Enables
- **Jordan decomposition** -- The unipotent part of the decomposition
- **Unipotent group** -- Groups of unipotent elements

## Contrasts With
- **Semisimple endomorphism** -- The other part of the Jordan decomposition

# Source Reference

Chapter I, Section 10b, pages 131-132.

# Verification Notes

- Definition source: Direct from text, p. 131
- Confidence rationale: Standard linear algebra reviewed explicitly
- Uncertainties: None
- Cross-reference status: Verified
