---
concept: Semisimple Module
slug: semisimple-module
category: semisimple-theory
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Lie Algebras and Algebraic Groups"
chapter_number: 2
pdf_page: 286
section: "6a Generalities on semisimple modules"
extraction_confidence: high
aliases:
  - "completely reducible module"
prerequisites: []
extends: []
related:
  - weyls-theorem
  - semisimple-representation-of-reductive-group
  - schurs-lemma
contrasts_with: []
answers_questions:
  - "What is a reductive algebraic group?"
---

# Quick Definition

A module M is semisimple (completely reducible) if every submodule has a complement -- equivalently, if M is a sum (equivalently, direct sum) of simple submodules.

# Core Definition

An A-module M (over an associative or Lie algebra A) is **semisimple** if it satisfies the equivalent conditions: (a) M is a sum of simple modules, (b) M is a direct sum of simple modules, (c) every submodule N has a complement N' with M = N + N' (Milne, Proposition 6.1, Definition 6.2).

# Prerequisites

This is a foundational concept in representation theory.

# Key Properties

1. Three equivalent characterizations (Proposition 6.1)
2. Schur's lemma: if V is simple and k algebraically closed, then End_A(V) = k (Lemma 6.3)
3. Semisimplicity of g-modules can be checked after base change to k^{al} (Proposition 6.4)
4. For connected G (char 0): V is semisimple as G-module iff as g-module (Corollary 6.5)

# Context & Application

Semisimple modules form the building blocks of representation theory. Weyl's theorem says that for semisimple Lie algebras in char 0, all finite-dimensional modules are semisimple. This extends to reductive groups.

# Examples

**Example 1**: A one-dimensional module is always simple (hence semisimple).

# Relationships

## Enables
- **Weyl's theorem** -- Uses the concept of semisimple modules
- **Semisimple representation of reductive group** -- Characterizes reductivity

## Related
- **Schur's lemma** -- Endomorphisms of simple modules are scalars

# Source Reference

Chapter II: Lie Algebras and Algebraic Groups, Section 6a, pages 286-287.

# Verification Notes

- Definition source: Direct from Definition 6.2
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
