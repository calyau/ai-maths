---
concept: Involution of an Algebra
slug: involution-of-algebra
category: classical-groups
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 226
section: "19e Involutions of k-algebras"
extraction_confidence: high
aliases:
  - "involution of first kind"
  - "involution of second kind"
prerequisites:
  - central-simple-algebra
extends: []
related:
  - classical-semisimple-groups
contrasts_with: []
answers_questions:
  - "What is a semisimple algebraic group?"
---

# Quick Definition

An involution of a k-algebra A is a k-linear map a -> a* satisfying (ab)* = b*a* and a** = a. It is of the first kind if it acts trivially on the centre, and of the second kind otherwise. Algebras with involution classify certain classical groups.

# Core Definition

An **involution** of a k-algebra A is a k-linear map a -> a*: A -> A such that (ab)* = b*a* and a** = a (Milne, Definition 19.27). The involution is of the **first kind** if it acts trivially on the centre of A, and of the **second kind** otherwise.

# Prerequisites

- **Central simple algebra** -- Involutions are studied on CSAs

# Key Properties

1. On M_n(k), the standard involution is X -> X^t (transpose), of the first kind (Example 19.28a)
2. On a quaternion algebra H(a,b), i -> -i, j -> -j is an involution of the first kind (Example 19.28b)
3. An inner automorphism inn(a) commutes with * iff a*a is in the centre (Lemma 19.29)
4. The groups attached to algebras with involution are classical semisimple groups

# Context & Application

Involutions on algebras provide a unified framework for classifying the classical semisimple groups of types B, C, and D over arbitrary fields. The unitary, orthogonal, and symplectic groups all arise from algebras with involution.

# Examples

**Example 1** (p. 226): The transpose X -> X^t on M_n(k) is the standard involution of the first kind.

**Example 2** (p. 226): On a quadratic extension K/k, complex conjugation is a nontrivial involution of the second kind.

# Relationships

## Builds Upon
- **Central simple algebra** -- Involutions are defined on CSAs

## Enables
- **Classical semisimple groups** -- Groups of types B, C, D arise from algebras with involution

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 19e, pages 226-228.

# Verification Notes

- Definition source: Direct from Definition 19.27
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
