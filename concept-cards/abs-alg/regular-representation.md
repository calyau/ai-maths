---
concept: Regular Representation
slug: regular-representation
category: representation-theory
subcategory: linear-representations
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Representation Theory and Character Theory"
chapter_number: 18
pdf_page: 842
section: "18.1 Linear Actions and Modules over Group Rings"
extraction_confidence: high
aliases: []
prerequisites:
  - representation
  - group-ring
extends: []
related:
  - character
contrasts_with:
  - trivial-representation
answers_questions:
  - "What is the regular representation of a group?"
---

# Quick Definition
The regular representation uses FG as a left module over itself, so G acts by left multiplication on the |G|-dimensional space FG. It is always faithful and contains every irreducible representation.

# Core Definition
The **regular representation** of G is the representation afforded by the left FG-module FG (Example 2, p. 842). It has degree |G|, and each nonidentity element induces a nonidentity permutation on the basis G, so it is always faithful. Its character satisfies χ_reg(1) = |G| and χ_reg(g) = 0 for g ≠ 1. Each irreducible representation appears with multiplicity equal to its degree.

# Prerequisites
- **representation** — The regular representation is a representation
- **group-ring** — V = FG

# Key Properties
1. Degree = |G|
2. Always faithful
3. χ_reg(1) = |G|, χ_reg(g) = 0 for g ≠ 1
4. Contains each irreducible with multiplicity n_i (its degree)

# Source Reference
Chapter 18, Section 18.1, Example 2, page 842.

# Verification Notes
- Confidence: HIGH — explicit example with properties
