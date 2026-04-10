---
concept: Forms of an Algebraic Group
slug: forms-of-algebraic-group
category: classical-groups
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 220
section: "19b Classifying the forms of an algebraic group"
extraction_confidence: high
aliases:
  - "inner form"
  - "outer form"
prerequisites:
  - nonabelian-galois-cohomology
  - semisimple-algebraic-group
extends: []
related:
  - classical-semisimple-groups
  - central-simple-algebra
contrasts_with: []
answers_questions:
  - "What is a semisimple algebraic group?"
---

# Quick Definition

A form of an algebraic group G_0 over k is an algebraic group G over k that becomes isomorphic to G_0 over k^{al}. The forms are classified by H^1(k, Aut(G_0)). Inner forms come from H^1(k, G^{ad}); outer forms involve nontrivial Dynkin diagram automorphisms.

# Core Definition

The isomorphism classes of algebraic groups G over k that become isomorphic to G_0 over k^{al} are classified by H^1(Gamma, A(k^{al})) where A(k^{al}) is the automorphism group of (G_0)_{k^{al}} (Milne, Theorem 19.8). An **inner form** is one whose cohomology class lies in H^1(k, G^{ad}); forms whose class maps nontrivially to H^1(k, Sym(D)) (where D is the Dynkin diagram) are **outer forms**.

# Prerequisites

- **Nonabelian Galois cohomology** -- Forms are classified by H^1
- **Semisimple algebraic group** -- The theory applies to semisimple groups

# Key Properties

1. For simply connected semisimple G_0, Aut(G_{0,k^{al}}) fits in 1 -> G^{ad}(k^{al}) -> A(k^{al}) -> Sym(D) -> 1 (19.15)
2. The inner forms of SL_n are the groups SL_m(D) for division algebras D (Theorem 19.26)
3. A group of type ^z X_y becomes inner over an extension of degree z
4. The type ^3 D_4 groups are neither classical nor exceptional in the usual sense

# Context & Application

The theory of forms reduces the classification of semisimple groups over arbitrary fields to understanding the Galois cohomology of automorphism groups. This connects to class field theory over number fields and p-adic fields.

# Examples

**Example 1** (p. 225): The inner forms of SL_n are classified by H^1(k, PGL_n), which equals the set of central simple algebras of degree n^2 over k. The form corresponding to a division algebra D of degree n/m is SL_m(D).

# Relationships

## Builds Upon
- **Nonabelian Galois cohomology** -- Forms are classified by H^1

## Related
- **Central simple algebra** -- CSAs are forms of matrix algebras

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 19b, pages 220-226.

# Verification Notes

- Definition source: Direct from Theorem 19.8
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
