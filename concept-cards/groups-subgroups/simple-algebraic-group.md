---
# === CORE IDENTIFICATION ===
concept: Simple Algebraic Group
slug: simple-algebraic-group

# === CLASSIFICATION ===
category: algebraic-groups
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 15
section: "Introductory overview"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - affine-algebraic-group
  - connected-algebraic-group
extends: []
related:
  - almost-simple-algebraic-group
contrasts_with:
  - almost-simple-algebraic-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine algebraic group?"
---

# Quick Definition

A connected affine algebraic group G is simple if it is not commutative and has no normal algebraic subgroups other than 1 and G. PSL_n = SL_n/Z is simple. Most "simple" groups in the literature are actually almost-simple.

# Core Definition

A connected affine algebraic group G is **simple** if it is not commutative and has no normal algebraic subgroups (other than 1 and G) (p. 15). This is a very restrictive condition: most "simple" groups in the classification (SL_n, SO_n, Sp_n) are actually almost-simple (they have a nontrivial finite centre).

For example, PSL_n = SL_n/Z is simple, while SL_n itself is only almost-simple (its centre is nontrivial).

# Prerequisites

- **Affine algebraic group** — Simple groups are algebraic groups
- **Connected algebraic group** — Simplicity requires connectedness

# Key Properties

1. No normal algebraic subgroups other than 1 and G
2. Not commutative (excludes G_a and G_m)
3. PSL_n is the prototypical simple algebraic group
4. Over algebraically closed fields, simple groups are the quotients G/Z(G) of almost-simple groups by their centres

# Relationships

## Related
- **Almost-simple algebraic group** — G is almost-simple if G/Z(G) is simple

## Contrasts With
- **Almost-simple algebraic group** — Almost-simple allows a finite centre; simple does not

# Source Reference

Chapter I, Section 1a (p. 15).

# Verification Notes

- Definition source: Direct from p. 15
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
