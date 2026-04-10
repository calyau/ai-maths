---
concept: Adjoint Representation of a Lie Algebra
slug: adjoint-representation-of-lie-algebra
category: lie-algebras
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Lie Algebras and Algebraic Groups"
chapter_number: 2
pdf_page: 240
section: "1a Lie algebras: basic definitions"
extraction_confidence: high
aliases:
  - "ad"
  - "adjoint map"
prerequisites:
  - lie-algebra
  - derivation-of-lie-algebra
extends: []
related:
  - adjoint-representation-of-group
  - killing-form
contrasts_with: []
answers_questions:
  - "What is a Lie algebra?"
---

# Quick Definition

The adjoint representation of a Lie algebra g is the homomorphism ad: g -> Der(g) sending x to the map y -> [x,y]. Its kernel is the centre z(g), and the inner derivations are exactly those of the form ad(x).

# Core Definition

For x in g, **ad(x)** denotes the map y -> [x,y]: g -> g (Milne, Example 1.4). The Jacobi identity shows ad(x) is a derivation of g, and ad: g -> Der_k(g) is a homomorphism of Lie algebras because ad([x,y])z = ad(x)(ad(y)z) - ad(y)(ad(x)z). The kernel of ad is the **centre** z(g) = {x in g | [x,g] = 0}. Derivations of the form ad(x) are called **inner**.

# Prerequisites

- **Lie algebra** -- The adjoint representation is a fundamental construction on Lie algebras
- **Derivation of Lie algebra** -- ad(x) is a derivation

# Key Properties

1. ad: g -> Der(g) is a Lie algebra homomorphism
2. Ker(ad) = z(g), the centre of g
3. The space of inner derivations ad(g) is an ideal in Der(g) (Lemma 5.20)
4. For semisimple g, every derivation is inner: ad: g -> Der(g) is an isomorphism (Theorem 5.21)

# Context & Application

The adjoint representation is the most basic representation of a Lie algebra. The Killing form is defined using it, and Engel's theorem and the Cartan-Killing criterion are proved using properties of ad.

# Examples

**Example 1** (p. 240): For gl_n, ad(A)(B) = AB - BA.

**Example 2** (p. 278): For sl_2 with basis x, y, h: ad(h) has eigenvalues 2, 0, -2 (see Example 5.10).

# Relationships

## Builds Upon
- **Lie algebra** -- ad is defined for any Lie algebra

## Enables
- **Killing form** -- kappa(x,y) = Tr(ad(x) o ad(y))
- **Engel's theorem** -- Uses nilpotency of ad

# Source Reference

Chapter II: Lie Algebras and Algebraic Groups, Section 1a, pages 240.

# Verification Notes

- Definition source: Direct from Example 1.4
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
