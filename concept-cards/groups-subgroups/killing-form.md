---
concept: Killing Form
slug: killing-form
category: semisimple-theory
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Lie Algebras and Algebraic Groups"
chapter_number: 2
pdf_page: 278
section: "5a Semisimple Lie algebras"
extraction_confidence: high
aliases:
  - "Cartan-Killing form"
  - "kappa_g"
prerequisites:
  - lie-algebra
  - adjoint-representation-of-lie-algebra
  - trace-form
extends:
  - trace-form
related:
  - semisimple-lie-algebra
  - cartan-killing-criterion
contrasts_with: []
answers_questions:
  - "What is the Killing form?"
---

# Quick Definition

The Killing form of a Lie algebra g is the trace form for the adjoint representation: kappa_g(x,y) = Tr_g(ad(x) o ad(y)). A Lie algebra is semisimple if and only if its Killing form is nondegenerate.

# Core Definition

The **Killing form** kappa_g on a Lie algebra g is the trace form for the adjoint representation ad: g -> gl_g (Milne, p. 278). Explicitly, kappa_g(x,y) = Tr_g(ad(x) o ad(y)), i.e., the trace of the linear map z -> [x,[y,z]]: g -> g. It is named after W. Killing, though E. Cartan was the first to exploit it systematically.

# Prerequisites

- **Lie algebra** -- The Killing form is defined on any Lie algebra
- **Adjoint representation of Lie algebra** -- kappa uses ad
- **Trace form** -- The Killing form is the trace form for the adjoint representation

# Key Properties

1. kappa_g is a symmetric, bilinear, associative form: kappa([x,y],z) = kappa(x,[y,z]) (Lemma 5.8)
2. The orthogonal complement of an ideal is again an ideal (Lemma 5.7)
3. The Killing form of an ideal a in g restricts to the Killing form on a: kappa_g|_{a x a} = kappa_a (Lemma 5.11)
4. If kappa_g(g,[g,g]) = 0, then g is solvable (Proposition 5.12)
5. g is semisimple iff kappa_g is nondegenerate (Cartan-Killing criterion, Theorem 5.13)

# Construction / Recognition

## To Construct:
1. Compute ad(x) and ad(y) as endomorphisms of g
2. Form the composition ad(x) o ad(y)
3. Take the trace: kappa(x,y) = Tr(ad(x) o ad(y))

# Context & Application

The Killing form is the fundamental invariant for detecting semisimplicity of Lie algebras. Its nondegeneracy is equivalent to semisimplicity (the Cartan-Killing criterion). It also plays a key role in the decomposition of semisimple Lie algebras into simple ideals, since ideal complements can be computed using the Killing form.

# Examples

**Example 1** (p. 278): For sl_2 with basis x, y, h: the Killing form has matrix ((0,0,4),(0,8,0),(4,0,0)) with determinant -128, confirming nondegeneracy and hence semisimplicity.

**Example 2** (p. 278): For sl_n, the matrix of kappa is (n^2-1) x (n^2-1), making direct computation impractical.

# Relationships

## Builds Upon
- **Adjoint representation of Lie algebra** -- kappa uses ad
- **Trace form** -- kappa is the trace form for the adjoint representation

## Enables
- **Cartan-Killing criterion** -- kappa nondegenerate iff g semisimple
- **Decomposition of semisimple Lie algebras** -- Ideal complements via kappa

# Common Errors

- **Error**: Computing kappa using an arbitrary faithful representation instead of the adjoint
  **Correction**: The Killing form specifically uses the adjoint representation; trace forms from other representations are related but different

# Source Reference

Chapter II: Lie Algebras and Algebraic Groups, Section 5a, pages 277-279.

# Verification Notes

- Definition source: Direct from p. 278
- Confidence rationale: Explicit definition with computed example
- Uncertainties: None
- Cross-reference status: Verified
