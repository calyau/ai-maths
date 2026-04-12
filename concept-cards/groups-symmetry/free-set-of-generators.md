---
# === CORE IDENTIFICATION ===
concept: Free Set of Generators
slug: free-set-of-generators

# === CLASSIFICATION ===
category: combinatorial-group-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Free Groups and Presentations"
chapter_number: 27
pdf_page: 173
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - free generators
  - free basis

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
extends: []
related:
  - free-group
  - reduced-word
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a free set of generators?"
  - "What distinguishes a free group from a finitely presented group?"
---

# Quick Definition

A subset X of a group G is a free set of generators if every non-identity element of G can be expressed in a unique way as a reduced word in the elements of X. The uniqueness means there are no "hidden relations" among the generators.

# Core Definition

"A subset X of a group G is called a free set of generators for G if every g in G - {e} can be expressed in a unique way as a product g = x_1^{n_1} x_2^{n_2} ... x_k^{n_k} of finite length, where the x_i lie in X, x_i is never equal to x_{i+1}, and each n_i is a non-zero integer. We call the set of generators free because by the uniqueness of (*) there can be no relations between its elements" (Armstrong, Ch. 27, p. 173).

# Prerequisites

- **Group** -- The ambient structure in which the generators live

# Key Properties

1. Every non-identity element has exactly one representation as a reduced word
2. The uniqueness of representation implies no relations hold among the generators
3. A bijection from X to Y induces an isomorphism F(X) -> F(Y) (Armstrong, p. 175)
4. The cardinality of X (the rank) is an isomorphism invariant (Theorem 27.3)

# Construction / Recognition

## To Verify X is a Free Set of Generators
1. Check that X generates G (every element is a product of elements of X and their inverses)
2. Verify uniqueness: no two distinct reduced words in X represent the same group element
3. Equivalently (Theorem 27.4): verify the universal property -- every function X -> H extends uniquely to a homomorphism G -> H

# Context & Application

The concept of a free set of generators is the starting point for Armstrong's development of free groups. It provides the precision needed to state that "there are no relations" among generators, which is made formal by the uniqueness of reduced word representations.

# Examples

**Example 1** (p. 173): In Z, the set {1} is a free set of generators: every non-zero integer n is uniquely 1^n.

**Example 2** (Exercise 27.9, p. 178): In F_2 = F({x,y}), the set {xyx^{-1}, x^2yx^{-2}, x^3yx^{-3}, ...} is a free set of generators for the subgroup it generates.

# Relationships

## Enables
- **Free group** -- A group with a free set of generators is a free group

## Related
- **Reduced word** -- Elements are uniquely represented as reduced words

# Common Errors

- **Error**: Confusing a generating set with a free set of generators
  **Correction**: Any group has generating sets, but a free set of generators additionally requires unique reduced word representations

# Common Confusions

- **Confusion**: Thinking any minimal generating set is free
  **Clarification**: In Z_6, {1} is a minimal generating set but not free because 1^6 = e imposes a relation

# Source Reference

Chapter 27: Free Groups and Presentations, page 173 (pdf p. 173). Definition at the start of the chapter.

# Verification Notes

- Definition: Directly quoted from Armstrong p. 173
- Confidence: HIGH -- explicit definition
- Cross-references: Verified against planned extractions
- Uncertainties: None
