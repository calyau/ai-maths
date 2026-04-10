---
concept: Group-Like Element
slug: group-like-element
category: multiplicative-groups
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 162
section: "14a Group-like elements"
extraction_confidence: high
aliases: []
prerequisites:
  - coalgebra
  - hopf-algebra
extends: []
related:
  - character-of-affine-group
  - diagonalizable-group
contrasts_with: []
answers_questions:
  - "What is a group-like element in a Hopf algebra?"
---

# Quick Definition

An element a of a k-coalgebra (A, Delta, epsilon) is group-like if Delta(a) = a tensor a and epsilon(a) = 1. In a Hopf algebra, group-like elements are exactly the units a with Delta(a) = a tensor a. They are always linearly independent.

# Core Definition

An element a of a k-coalgebra (A, Delta, epsilon) is *group-like* if Delta(a) = a tensor a and epsilon(a) = 1 (Definition 14.1). In a bialgebra, group-like elements form a submonoid of (A, multiplication). In a Hopf algebra with antipode S, the group-like elements are exactly the units a with Delta(a) = a tensor a, and a^{-1} = S(a) (Milne, pp. 162-164). *Lemma 14.2*: The group-like elements in any coalgebra are linearly independent.

# Prerequisites

- **Coalgebra** -- Group-like elements are defined in coalgebras
- **Hopf algebra** -- Additional structure makes them a group

# Key Properties

1. Group-like elements are linearly independent (Lemma 14.2)
2. In a bialgebra, the product of group-like elements is group-like
3. In a Hopf algebra, group-like elements form a group under multiplication with inverse S(a)
4. Characters of G correspond bijectively to group-like elements of O(G)
5. G is diagonalizable iff group-like elements span O(G)

# Context & Application

Group-like elements are the algebraic incarnation of characters. The linear independence of group-like elements is used throughout the theory, notably in proving the direct sum decomposition of eigenspaces (Theorem 8.65).

# Examples

**Example 1** (p. 162): In O(G_m) = k[X, X^{-1}], the elements X^n for n in Z are all group-like, forming the character group Z.

**Example 2** (p. 162): In O(mu_n) = k[x]/(x^n - 1), the element x is group-like with Delta(x) = x tensor x.

# Relationships

## Enables
- **Character of affine group** -- Characters = group-like elements
- **Diagonalizable group** -- Defined by group-like elements spanning O(G)

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 14a, pages 162-164. Definition 14.1, Lemma 14.2.

# Verification Notes

- Definition source: Direct from Definition 14.1
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
