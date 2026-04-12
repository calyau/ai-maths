---
concept: Image
slug: image
category: group-theory
subcategory: null
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Groups"
chapter_number: 2
pdf_page: 48
section: "2.5 Homomorphisms"
extraction_confidence: high
aliases:
  - "im"
prerequisites:
  - homomorphism
extends: []
related:
  - kernel
  - first-isomorphism-theorem
contrasts_with:
  - kernel
answers_questions:
  - "What is a homomorphism?"
---

# Quick Definition

The image of a homomorphism phi: G -> G' is the set of elements in G' that are hit by phi: im(phi) = {x in G' : x = phi(a) for some a in G}. It is a subgroup of G'.

# Core Definition

The image of a homomorphism phi: G -> G', often denoted im(phi), is the image of phi as a map of sets: im(phi) = {x in G' : x = phi(a) for some a in G} (Artin, p. 61, formula 2.5.4). The image is a subgroup of G'.

# Prerequisites

- **Homomorphism** — The image is defined for a homomorphism

# Key Properties

1. im(phi) is a subgroup of G'
2. phi is surjective iff im(phi) = G'
3. |G| = |ker(phi)| * |im(phi)| for finite groups (Corollary 2.8.13)
4. |im(phi)| divides both |G| and |G'|

# Construction / Recognition

## To Construct:
1. Apply phi to every element of G
2. Collect the results

## To Recognize:
1. The range of phi as a function

# Context & Application

The image records the "visible part" of G inside G'. Together with the kernel, it completely describes the homomorphism via the First Isomorphism Theorem: G/ker(phi) ≅ im(phi).

# Examples

**Example 1** (p. 61): The image of the map Z+ -> G sending n -> a^n is the cyclic subgroup <a>.

**Example 2** (p. 62): The image of the sign homomorphism S_n -> {+/-1} is {+/-1} (surjective).

# Relationships

## Builds Upon
- **Homomorphism** — Image is a property of a homomorphism

## Enables
- **First isomorphism theorem** — G/ker(phi) ≅ im(phi)

## Contrasts With
- **Kernel** — The kernel records what collapses; the image records the range

# Common Errors

- **Error**: Forgetting the image is a subgroup (not just a subset)
  **Correction**: The image inherits the group structure from G'

# Common Confusions

- **Confusion**: Confusing image with codomain
  **Clarification**: The image is the actual range of phi, which may be a proper subset of G'

# Source Reference

Chapter 2: Groups, Section 2.5, pages 61-62.

# Verification Notes

- Definition source: Direct from (2.5.4), p. 61
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
