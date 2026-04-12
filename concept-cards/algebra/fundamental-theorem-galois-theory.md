---
concept: Fundamental Theorem of Galois Theory
slug: fundamental-theorem-galois-theory
category: galois-theory
subcategory: main-results
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Galois Theory"
chapter_number: 16
pdf_page: 488
section: "16.7 The Main Theorem"
extraction_confidence: high
aliases:
  - "Main Theorem of Galois Theory"
  - "Galois correspondence"
prerequisites:
  - galois-extension
  - galois-group
  - fixed-field
extends: []
related:
  - intermediate-field
  - normal-subgroup
contrasts_with: []
answers_questions:
  - "What is the Fundamental Theorem of Galois Theory?"
  - "How does the Galois group relate to intermediate fields?"
---

# Quick Definition

The Fundamental Theorem establishes a bijective, inclusion-reversing correspondence between subgroups of the Galois group G(K/F) and intermediate fields F in L in K. A subgroup H corresponds to its fixed field K^H, and an intermediate field L corresponds to the Galois group G(K/L).

# Core Definition

Let K be a Galois extension of a field F, and let G be its Galois group. There is a bijective correspondence between subgroups of G and intermediate fields (Artin, Theorem 16.7.1):

{subgroups of G} <-> {intermediate fields F in L in K}

This correspondence associates to a subgroup H its fixed field K^H, and to an intermediate field L the Galois group G(K/L). The maps H -> K^H and L -> G(K/L) are inverse functions.

# Prerequisites

- **Galois extension** -- The theorem applies to Galois extensions
- **Galois group** -- The group side of the correspondence
- **Fixed field** -- The maps use the fixed field construction

# Key Properties

1. The correspondence reverses inclusions: H in H' iff K^H contains K^{H'} (Corollary 16.7.2(a))
2. G corresponds to F; the trivial subgroup {1} corresponds to K (16.7.2(b))
3. [K:L] = |H| and [L:F] = [G:H] (16.7.2(c))
4. L/F is Galois iff H is normal in G; if so, G(L/F) = G/H (Theorem 16.7.5)
5. A finite extension K/F has finitely many intermediate fields (Corollary 16.7.3)

# Construction / Recognition

## To Apply:
1. Verify K/F is a Galois extension (splitting field, |G| = [K:F])
2. List all subgroups of G
3. For each subgroup H, compute the fixed field K^H
4. The correspondence gives ALL intermediate fields

# Context & Application

This is the central result of Galois theory and the capstone of Artin's Chapter 16. It transforms questions about field extensions (which are hard) into questions about group theory (which are easier). It is used to determine intermediate fields, prove impossibility results, and analyze solvability by radicals.

# Examples

**Example 1** (p. 501): K = Q(sqrt(3), sqrt(5)) over Q. G is the Klein four group with three subgroups of order 2, giving three intermediate fields Q(sqrt(3)), Q(sqrt(5)), Q(sqrt(15)). These are all proper intermediate fields.

**Example 2** (p. 499-500): For the splitting field of an irreducible cubic with G = S_3: four proper subgroups give four proper intermediate fields: F(alpha_1), F(alpha_2), F(alpha_3), and F(delta) where delta is the square root of the discriminant.

# Relationships

## Builds Upon
- **Galois extension** -- The setting for the theorem
- **Galois group** -- One side of the correspondence
- **Fixed field** -- The construction underlying the correspondence

## Enables
- **Solvability by radicals** -- Analyzed via the Galois correspondence
- **Constructibility** -- Intermediate fields correspond to construction steps

## Related
- **Normal subgroup** -- Normal subgroups correspond to Galois intermediate extensions

# Common Errors

- **Error**: Applying the theorem to non-Galois extensions
  **Correction**: The theorem requires K/F to be Galois. For non-Galois extensions, the correspondence fails.

- **Error**: Forgetting that the correspondence reverses inclusions
  **Correction**: Larger subgroups correspond to smaller fields, and vice versa.

# Common Confusions

- **Confusion**: Thinking normal subgroups are needed for the basic correspondence
  **Clarification**: The basic bijection works for all subgroups. Normality is needed only to characterize which intermediate fields are themselves Galois over F.

# Source Reference

Chapter 16: Galois Theory, Section 16.7, pages 500-504. Theorem 16.7.1, Corollary 16.7.2, Theorem 16.7.5.

# Verification Notes

- Definition source: Direct from Artin, Theorem 16.7.1
- Confidence rationale: Complete statement and proof given, central theorem of the chapter
- Uncertainties: None
- Cross-reference status: Verified
