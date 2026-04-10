---
# === CORE IDENTIFICATION ===
concept: Affine Group Scheme
slug: affine-group-scheme

# === CLASSIFICATION ===
category: algebraic-groups
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 53
section: "Affine groups and affine group schemes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - group scheme
  - algebraic group scheme

# === TYPED RELATIONSHIPS ===
prerequisites:
  - affine-scheme
  - affine-group
  - hopf-algebra
extends:
  - affine-scheme
related:
  - affine-algebraic-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine group scheme?"
  - "What distinguishes an algebraic group from a group scheme?"
---

# Quick Definition

An affine group scheme over k is a group object in the category of affine schemes over k. The functor Spec defines an equivalence between affine groups and affine group schemes.

# Core Definition

An **affine group scheme over k** is a group object in the category of affine k-schemes, i.e., an affine scheme V over k together with morphisms m: V x V -> V, e: Spec(k) -> V, and inv: V -> V satisfying the group axioms (Section 6b, p. 55).

**Theorem 6.2** (p. 55): The functor Spec defines an equivalence from the category of affine groups over k to the category of affine group schemes over k.

**Summary 6.11** (p. 59): For a field k, there are canonical equivalences between:
(a) affine algebraic groups over k
(b) functors Alg_k -> Grp representable by finitely generated k-algebras
(c) the opposite of finitely generated Hopf algebras over k
(d) affine algebraic group schemes over k

After Section 6g (p. 60), Milne abbreviates to "group scheme" and "algebraic group scheme".

# Prerequisites

- **Affine scheme** — The underlying geometric object
- **Affine group** — The algebraic counterpart
- **Hopf algebra** — The algebraic encoding

# Key Properties

1. Equivalent to affine groups via the Spec functor
2. Equivalent to (opposite of) Hopf algebras
3. For |G| = Spm(O(G)), the set |G| is a group when k is algebraically closed (via Nullstellensatz)
4. |G| is NOT usually a group for non-algebraically-closed k (Section "Is the set |G| a group?", p. 59)

# Context & Application

The group scheme perspective embeds affine algebraic groups into the larger category of group schemes (which includes non-affine examples like abelian varieties). The geometric viewpoint (especially over algebraically closed fields) provides tools from algebraic geometry for studying algebraic groups: dimension, smoothness, irreducibility, etc.

# Examples

**Example 1** (p. 58): For an algebraic group G, |G| = Spm(O(G)) with group structure inherited from the Hopf algebra. When k is algebraically closed, |G| = G(k) as a group.

# Relationships

## Extends
- **Affine scheme** — An affine group scheme is a group object in affine schemes

## Related
- **Affine algebraic group** — Equivalent via the Spec functor

# Common Confusions

- **Confusion**: Thinking the underlying topological space |G| is always a group
  **Clarification**: |G| is only a group when k is algebraically closed; otherwise spm does not preserve products (p. 59)

# Source Reference

Chapter I, Section 6b (p. 55), Theorem 6.2, Summary 6.11 (p. 59).

# Verification Notes

- Definition source: Direct from Section 6b
- Confidence rationale: Explicit definition with equivalence theorem
- Uncertainties: None
- Cross-reference status: Verified
