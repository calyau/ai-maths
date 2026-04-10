---
concept: Replete Subcategory
slug: replete-subcategory
category: representations
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 114
section: "8n Sub-coalgebras and subcategories"
extraction_confidence: high
aliases: []
prerequisites:
  - category-of-representations
extends: []
related:
  - normal-subgroup-kernel
contrasts_with: []
answers_questions:
  - "What is a replete subcategory?"
  - "How do subcategories of Rep(G) correspond to quotient groups?"
---

# Quick Definition

A full subcategory of an abelian category is replete if it is closed under finite direct sums, subobjects, and quotient objects. Replete subcategories of Comod(C) correspond bijectively to sub-coalgebras of C, and replete subcategories of Rep(G) closed under tensor products and duals correspond to quotient groups of G.

# Core Definition

A full subcategory of an abelian category is *replete* if it is closed under finite direct sums, subobjects, and quotient objects (Definition 8.60). A replete subcategory is itself abelian, and the inclusion functor is exact. Theorem 8.61: the map D -> D^dual is a bijection from sub-coalgebras of C to replete subcategories of Comod(C). Theorem 8.63: the map Q -> Q^dual is a bijection from quotient groups of G to replete subcategories of Rep(G) closed under tensor products and contragredients (Milne, pp. 114-116).

# Prerequisites

- **Category of representations** -- Replete subcategories live inside Rep(G)

# Key Properties

1. Replete subcategories correspond to sub-coalgebras (Theorem 8.61)
2. Tensor-closed replete subcategories correspond to quotient groups (Theorem 8.63)
3. Normal-subgroup-closed replete subcategories correspond to normal subgroups via Rep(G)^N (Corollary 8.76)

# Context & Application

Replete subcategories provide the categorical framework for understanding the lattice of quotient groups and normal subgroups of G entirely in terms of Rep(G).

# Examples

**Example 1** (p. 116): For G -> Q a quotient, the representations of Q form a replete subcategory of Rep(G) closed under tensor products and duals.

# Relationships

## Builds Upon
- **Category of representations** -- Context for the definition

## Enables
- **Normal subgroup kernel** -- Normal subgroups correspond to special replete subcategories

# Source Reference

Chapter I: Basic Theory of Affine Groups, Sections 8n-8o, pages 114-116. Definition 8.60, Theorems 8.61, 8.63.

# Verification Notes

- Definition source: Direct from Definition 8.60
- Confidence rationale: Explicit definition with classification theorems
- Uncertainties: None
- Cross-reference status: Verified
