---
concept: Lie Algebra of an Algebraic Group
slug: lie-algebra-of-algebraic-group
category: lie-algebras
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Lie Algebras and Algebraic Groups"
chapter_number: 2
pdf_page: 241
section: "1c The Lie algebra of an algebraic group"
extraction_confidence: high
aliases:
  - "Lie(G)"
  - "Lie functor"
prerequisites:
  - lie-algebra
  - dual-numbers
extends: []
related:
  - adjoint-representation-of-group
  - lie-bracket
contrasts_with: []
answers_questions:
  - "What is a Lie algebra?"
  - "How does the Lie algebra functor connect algebraic groups to Lie algebras?"
---

# Quick Definition

The Lie algebra Lie(G) of an algebraic group G is the kernel of G(k[epsilon]) -> G(k), where k[epsilon] = k[X]/(X^2) is the ring of dual numbers. It is the tangent space at the identity with a natural bracket.

# Core Definition

For an algebraic group G over k, **Lie(G)** = Ker(G(k[epsilon]) -> G(k)) where k[epsilon] = k[X]/(X^2) and the map sends epsilon to 0 (Milne, Definition 1.9). Equivalently, Lie(G) = Hom_{k-lin}(I_G/I_G^2, k) where I_G is the augmentation ideal (Proposition 1.11). There is a unique Lie algebra structure on Lie(G) such that Lie(GL_n) = gl_n (Theorem 1.12).

# Prerequisites

- **Lie algebra** -- Lie(G) is a Lie algebra
- **Dual numbers** -- The construction uses k[epsilon]

# Key Properties

1. Lie is a functor from algebraic groups to Lie algebras (Theorem 1.12)
2. Lie(GL_n) = gl_n with bracket [A,B] = AB - BA (Lemma 1.31)
3. An embedding G -> H gives an injection Lie(G) -> Lie(H)
4. Lie preserves fibred products: Lie(G x_H G') = Lie(G) x_{Lie(H)} Lie(G') (Proposition 1.34)
5. Lie(Ker(alpha)) = Ker(Lie(alpha)) (Example 1.36)
6. For field extensions K/k: Lie(G_K) = K tensor_k Lie(G) (Proposition 1.27)
7. dim Lie(G) >= dim G, with equality iff G is smooth (Proposition 2.2)

# Construction / Recognition

## To Construct:
1. Embed G in GL_n
2. Compute which matrices I + epsilon A satisfy the defining equations of G in M_n(k[epsilon])
3. The set of such A is Lie(G) as a subspace of gl_n

## To Recognize:
1. It is a Lie subalgebra of gl_n for any embedding G -> GL_n

# Context & Application

The Lie algebra functor is the primary bridge between algebraic groups and linear algebra. In characteristic zero, it is faithful on connected groups (Theorem 2.11), exact on short exact sequences (Corollary 2.7), and sends semisimple groups to semisimple Lie algebras (Theorem 5.23). However, it is not fully faithful and trivial on etale groups.

# Examples

**Example 1** (p. 241): Lie(GL_n) consists of elements I_n + epsilon A in M_n(k[epsilon]), giving gl_n = M_n(k).

**Example 2** (p. 242): Lie(SL_n) = {A in M_n(k) | trace(A) = 0} = sl_n.

**Example 3** (p. 242): Lie(O_n) = {A in M_n(k) | A^t + A = 0} = skew-symmetric matrices.

# Relationships

## Builds Upon
- **Lie algebra** -- Lie(G) is a Lie algebra

## Enables
- **Adjoint representation of group** -- Ad: G -> GL(Lie(G))
- **Semisimple Lie algebra** -- Lie(G) is semisimple iff G is (in char 0)

# Common Errors

- **Error**: Assuming Lie(G) determines G
  **Correction**: The Lie algebra determines G only up to isogeny in char 0; infinitely many nonisomorphic groups can have the same Lie algebra (2.14)

# Common Confusions

- **Confusion**: Believing Lie is right exact
  **Clarification**: The functor Lie is left exact but NOT right exact in general (1.39)

# Source Reference

Chapter II: Lie Algebras and Algebraic Groups, Sections 1c-1j, pages 241-251.

# Verification Notes

- Definition source: Direct from Definition 1.9
- Confidence rationale: Explicit definition with many examples
- Uncertainties: None
- Cross-reference status: Verified
