---
concept: Almost-Simple Algebraic Group
slug: almost-simple-algebraic-group
category: group-structure
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 197
section: "17d Semisimple groups"
extraction_confidence: high
aliases:
  - "almost simple group"
prerequisites:
  - semisimple-algebraic-group
  - connected-algebraic-group
extends:
  - semisimple-algebraic-group
related:
  - simple-algebraic-group
  - almost-direct-product
contrasts_with:
  - simple-algebraic-group
answers_questions:
  - "What is a semisimple algebraic group?"
---

# Quick Definition

An almost-simple algebraic group is a connected noncommutative algebraic group all of whose proper normal subgroups are finite. Every semisimple group is an almost-direct product of almost-simple factors.

# Core Definition

An algebraic group G is **almost-simple** if it is connected, noncommutative, and all its proper normal subgroups are finite (Milne, p. 197). By contrast, G is **simple** if its only proper normal subgroup is 1. For n > 1, SL_n is almost-simple and PSL_n = SL_n/mu_n is simple.

# Prerequisites

- **Semisimple algebraic group** -- Almost-simple groups are the building blocks of semisimple groups
- **Connected algebraic group** -- Almost-simple groups must be connected

# Key Properties

1. A semisimple group has finitely many almost-simple normal subgroups G_1,...,G_r (Theorem 17.16)
2. The map (g_1,...,g_r) -> g_1...g_r from G_1 x ... x G_r to G is surjective with finite kernel
3. Each connected normal subgroup of a semisimple G is a product of some G_i
4. An algebraic group is semisimple iff it is an almost-direct product of almost-simple groups
5. The G_i are called the almost-simple factors of G

# Construction / Recognition

## To Recognize:
1. Check G is connected and noncommutative
2. Verify every proper normal subgroup is finite

# Context & Application

Almost-simple groups are the atomic building blocks of semisimple groups. The classification of semisimple groups reduces to classifying almost-simple groups. Over algebraically closed fields, the almost-simple groups correspond to Dynkin diagrams: A_n (SL_{n+1}), B_n (SO_{2n+1}), C_n (Sp_{2n}), D_n (SO_{2n}), and the exceptional types G_2, F_4, E_6, E_7, E_8.

# Examples

**Example 1** (p. 197): SL_n (n > 1) is almost-simple. Its only proper normal subgroup is the centre mu_n, which is finite.

**Example 2** (p. 197): PSL_n = SL_n/mu_n is simple (not just almost-simple), since its centre is trivial.

# Relationships

## Builds Upon
- **Semisimple algebraic group** -- Almost-simple groups are the simple factors

## Enables
- **Classical semisimple groups** -- Classified by Dynkin type

## Contrasts With
- **Simple algebraic group** -- Simple means the ONLY proper normal subgroup is 1; almost-simple allows finite normal subgroups

# Common Errors

- **Error**: Confusing "almost-simple" with "simple"
  **Correction**: SL_n is almost-simple but not simple (it has centre mu_n); PSL_n is simple

# Common Confusions

- **Confusion**: Believing the almost-direct product decomposition is a direct product
  **Clarification**: The kernel of G_1 x ... x G_r -> G is typically finite but nonzero

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 17d, pages 197-199.

# Verification Notes

- Definition source: Direct from p. 197
- Confidence rationale: Explicit definition with examples
- Uncertainties: None
- Cross-reference status: Verified
