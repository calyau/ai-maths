---
concept: Classical Semisimple Groups
slug: classical-semisimple-groups
category: classical-groups
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 217
section: "19 The classical semisimple groups"
extraction_confidence: high
aliases:
  - "classical types"
prerequisites:
  - semisimple-algebraic-group
  - almost-simple-algebraic-group
extends: []
related:
  - nonabelian-galois-cohomology
  - forms-of-algebraic-group
  - central-simple-algebra
contrasts_with:
  - exceptional-semisimple-groups
answers_questions:
  - "What is a semisimple algebraic group?"
---

# Quick Definition

Over an algebraically closed field, the classical semisimple algebraic groups are those whose almost-simple factors are of type A_n (SL_{n+1}), B_n (SO_{2n+1}), C_n (Sp_{2n}), or D_n (SO_{2n}).

# Core Definition

Over an algebraically closed field, the **classical semisimple algebraic groups** are those whose almost-simple factors are isogenous to SL_{n+1} (n >= 1), SO_{2n+1} (n >= 2), Sp_{2n} (n >= 3), or SO_{2n} (n >= 4), said to be of type A_n, B_n, C_n, or D_n respectively (Milne, p. 217). Over an arbitrary field k, they are the semisimple groups that become classical over k^{al}.

# Prerequisites

- **Semisimple algebraic group** -- Classical groups are a special class of semisimple groups
- **Almost-simple algebraic group** -- Classification is in terms of almost-simple factors

# Key Properties

1. Over arbitrary fields, classical groups are described by semisimple algebras with involution (p. 217)
2. The forms of SL_n are classified by H^1(k, PGL_n) = central simple algebras of degree n^2
3. The inner forms of SL_n are the groups SL_m(D) for division algebras D of degree n/m (Theorem 19.26)
4. H^1(k, Sp_n) = 1, so the symplectic group has no nontrivial forms (Proposition 19.6)
5. H^1(k, O(phi)) classifies quadratic spaces of the same dimension (Remark 19.7)

# Context & Application

The classification of classical semisimple groups over arbitrary fields uses Galois cohomology and the theory of algebras with involution. This connects representation theory to number theory through class field theory.

# Examples

**Example 1** (p. 217): SL_{n+1} is of type A_n. Its forms over k are the groups SL_m(D) for central division algebras D over k.

**Example 2** (p. 217): SO_{2n+1} is of type B_n, Sp_{2n} is of type C_n, SO_{2n} is of type D_n.

# Relationships

## Builds Upon
- **Semisimple algebraic group** -- Classical groups are semisimple

## Related
- **Nonabelian Galois cohomology** -- Used to classify forms
- **Central simple algebra** -- Forms of SL_n correspond to CSAs

## Contrasts With
- **Exceptional semisimple groups** -- Types G_2, F_4, E_6, E_7, E_8 are not classical

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 19, pages 217-232.

# Verification Notes

- Definition source: Direct from p. 217
- Confidence rationale: Explicit classification
- Uncertainties: None
- Cross-reference status: Verified
