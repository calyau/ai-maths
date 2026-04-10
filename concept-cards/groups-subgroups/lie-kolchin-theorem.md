---
concept: Lie-Kolchin Theorem
slug: lie-kolchin-theorem
category: solvable-groups
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 190
section: "16d Solvable algebraic groups"
extraction_confidence: high
aliases: []
prerequisites:
  - solvable-algebraic-group
  - trigonalizable-group
extends: []
related:
  - eigenspace
contrasts_with: []
answers_questions:
  - "When is a solvable group trigonalizable?"
---

# Quick Definition

The Lie-Kolchin theorem states that a connected, smooth, solvable algebraic group over an algebraically closed field is trigonalizable, i.e., can be put in upper triangular form in any representation.

# Core Definition

*Theorem 16.31 (Lie-Kolchin)*: Let G be a subgroup of GL_V. If G is connected, smooth, and solvable, and k is algebraically closed, then G is trigonalizable (i.e., there exists a basis of V such that G(k) is contained in T_n(k)). All four hypotheses are necessary: connected, smooth, solvable, and k algebraically closed (Milne, pp. 190-192).

# Prerequisites

- **Solvable algebraic group** -- The hypothesis on G
- **Trigonalizable group** -- The conclusion

# Key Properties

1. All four hypotheses are necessary (counterexamples in 16.32)
2. Connected is needed: the group of monomial 2x2 matrices is solvable but not trigonalizable
3. Smooth is needed: in char 2, certain non-smooth subgroups of SL_2 are solvable but not trigonalizable
4. k algebraically closed is needed: the circle group over R is commutative but not trigonalizable over R
5. The proof uses induction on the length of the derived series and eigenspace decomposition

# Context & Application

The Lie-Kolchin theorem is the group-theoretic analogue of Lie's theorem for Lie algebras. It reduces the study of solvable groups over algebraically closed fields to upper triangular matrix groups.

# Examples

**Example 1** (p. 191): Counterexample for "connected": the group of monomial 2x2 matrices is solvable but D_2(k) has eigenvectors e_1, e_2 that are swapped by the permutation matrix, so no common eigenvector exists.

**Example 2** (p. 191): Counterexample for "k algebraically closed": {((a,b),(-b,a)) | a^2+b^2=1} over R is commutative but not trigonalizable over R.

# Relationships

## Builds Upon
- **Solvable algebraic group** -- The input hypothesis

## Enables
- **Structure of solvable groups** -- Over k^al, solvable groups have the form 1 -> G_u -> G -> T -> 1

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 16d, pages 190-192. Theorem 16.31, Remark 16.32.

# Verification Notes

- Definition source: Direct from Theorem 16.31
- Confidence rationale: Major theorem with detailed proof and counterexamples
- Uncertainties: None
- Cross-reference status: Verified
