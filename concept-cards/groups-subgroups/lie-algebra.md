---
concept: Lie Algebra
slug: lie-algebra
category: lie-algebras
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Lie Algebras and Algebraic Groups"
chapter_number: 2
pdf_page: 239
section: "1a Lie algebras: basic definitions"
extraction_confidence: high
aliases:
  - "g"
prerequisites: []
extends: []
related:
  - lie-bracket
  - lie-algebra-of-algebraic-group
  - lie-subalgebra
  - ideal-of-lie-algebra
contrasts_with: []
answers_questions:
  - "What is a Lie algebra?"
---

# Quick Definition

A Lie algebra over a field k is a k-vector space g equipped with a k-bilinear bracket [,]: g x g -> g satisfying [x,x] = 0 (skew-symmetry) and the Jacobi identity.

# Core Definition

A **Lie algebra** over a field k is a vector space g over k together with a k-bilinear map [,]: g x g -> g (called the **bracket**) such that (a) [x,x] = 0 for all x in g, and (b) [x,[y,z]] + [y,[z,x]] + [z,[x,y]] = 0 for all x,y,z in g (the **Jacobi identity**) (Milne, Definition 1.1). A **homomorphism** of Lie algebras is a k-linear map alpha: g -> g' with alpha([x,y]) = [alpha(x), alpha(y)].

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Condition (a) implies skew-symmetry: [x,y] = -[y,x] (equation 126)
2. The Jacobi identity can be rewritten as [x,[y,z]] = [[x,y],z] + [y,[x,z]] (equation 127)
3. A Lie subalgebra is a k-subspace s with [s,s] contained in s
4. An ideal is a subspace a with [g,a] contained in a
5. Every associative algebra A becomes a Lie algebra with [a,b] = ab - ba (Example 1.2)

# Construction / Recognition

## To Construct:
1. Start with a vector space g
2. Define a k-bilinear bracket [,]: g x g -> g
3. Verify [x,x] = 0 for all x
4. Verify the Jacobi identity

## To Recognize:
1. Check it is a k-vector space with a bilinear operation
2. Verify skew-symmetry and the Jacobi identity

# Context & Application

Lie algebras are the "infinitesimal" or "linear approximation" to algebraic groups. They are much more elementary to study than groups, yet in characteristic zero they capture most of the group structure. The functor G -> Lie(G) from algebraic groups to Lie algebras is faithful on connected groups in characteristic zero.

# Examples

**Example 1** (p. 239): For any associative k-algebra A, the bracket [a,b] = ab - ba makes A into a Lie algebra. When A = End(V), this is denoted gl_V.

**Example 2** (p. 239): The set of k-derivations Der_k(A) of a k-algebra A is a Lie subalgebra of gl_A.

# Relationships

## Enables
- **Lie algebra of algebraic group** -- Lie(G) is a Lie algebra
- **Adjoint representation** -- ad: g -> Der(g) is a key homomorphism
- **Semisimple Lie algebra** -- A distinguished class of Lie algebras

# Common Confusions

- **Confusion**: Believing the Lie bracket is associative
  **Clarification**: The Lie bracket satisfies the Jacobi identity instead of associativity; the Jacobi identity says ad(x) is a derivation

# Source Reference

Chapter II: Lie Algebras and Algebraic Groups, Section 1a, pages 238-239.

# Verification Notes

- Definition source: Direct from Definition 1.1
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
