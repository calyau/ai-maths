---
# === CORE IDENTIFICATION ===
concept: Constant Finite Algebraic Group
slug: constant-finite-algebraic-group

# === CLASSIFICATION ===
category: classical-groups
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 14
section: "Introductory overview"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "(F)_k"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - affine-algebraic-group
extends: []
related:
  - group-of-nth-roots-of-unity
  - cartier-duality
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine algebraic group?"
---

# Quick Definition

A constant finite algebraic group (F)_k is the algebraic group obtained from a finite (abstract) group F by taking O((F)_k) = product of copies of k indexed by elements of F. When R has no nontrivial idempotents, (F)_k(R) = F.

# Core Definition

For a finite group F, let O(F) = product_{g in F} k_g (product of copies of k indexed by elements of F). Then R -> Hom_{k-alg}(O(F), R) is an affine algebraic group (F)_k such that (F)_k(R) = F for any k-algebra R with no nontrivial idempotents (3.3, p. 29; 5.23, p. 49).

The Hopf algebra structure on O(F) is given by (5.23, p. 49):
- Delta(e_rho) = sum_{sigma*tau = rho} e_sigma tensor e_tau
- epsilon(e_sigma) = 1 if sigma = 1, else 0
- S(e_sigma) = e_{sigma^{-1}}

where the e_sigma are the complete system of orthogonal idempotents (e_sigma^2 = e_sigma, e_sigma * e_tau = 0 for sigma != tau, sum e_sigma = 1).

# Prerequisites

- **Affine algebraic group** — Constant finite algebraic groups are a special case

# Key Properties

1. Every finite group can be realized as a constant algebraic group, hence as a subgroup of GL_n (p. 14)
2. (F)_k(R) may be larger than F when R has nontrivial idempotents
3. Constant finite algebraic groups are smooth (etale) in characteristic zero
4. The theory of algebraic groups includes the theory of finite groups via this construction

# Examples

**Example 1** (p. 29): The trivial group gives G(R) = {1} for all R, represented by O(G) = k.

**Example 2** (p. 14): The symmetric group S_n is realized as a constant algebraic subgroup of GL_n via permutation matrices I(sigma).

# Relationships

## Related
- **Group of nth roots of unity** — mu_n is related but not constant in general (it is etale when char(k) does not divide n)

# Source Reference

Chapter I, Section 1 (p. 14), 3.3 (p. 29), 5.23 (p. 49).

# Verification Notes

- Definition source: Direct from 3.3 and 5.23
- Confidence rationale: Explicit definition with full Hopf algebra structure
- Uncertainties: None
- Cross-reference status: Verified
