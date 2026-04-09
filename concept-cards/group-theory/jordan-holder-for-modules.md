---
# === CORE IDENTIFICATION ===
concept: Jordan-Holder Theorem for Modules
slug: jordan-holder-for-modules

# === CLASSIFICATION ===
category: module-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Representations of Finite Groups"
chapter_number: 7
pdf_page: 105
section: "Semisimple modules"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "composition series for modules"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - simple-module
  - f-algebra
extends: []
related:
  - semisimple-module
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Does the Jordan-Holder theorem hold for modules?"
  - "Is a composition series of a module unique?"
---

# Quick Definition

Every A-module V admits a filtration with simple quotients, and any two such filtrations have the same length and (up to permutation) isomorphic quotients.

# Core Definition

**Theorem 7.10.** Every A-module V admits a filtration V = V_0 > V_1 > ... > V_s = {0} such that the quotients V_i/V_{i+1} are simple A-modules. If V = W_0 > W_1 > ... > W_t = {0} is a second such filtration, then s = t and there is a permutation sigma of {1, ..., s} such that V_i/V_{i+1} is isomorphic to W_{sigma(i)}/W_{sigma(i)+1}. (Milne, Theorem 7.10, p. 105)

# Prerequisites

- **Simple module** — the quotients in the filtration are simple
- **F-algebra** — modules are over an F-algebra

# Key Properties

1. Every module has a composition series (filtration with simple quotients)
2. The length s of the series is an invariant of V
3. The multiset of composition factors (simple quotients) is unique up to isomorphism
4. This is a variant of the Jordan-Holder theorem for groups (6.2)

# Construction / Recognition

1. If V is simple, the filtration is V > {0}
2. Otherwise, find a proper nonzero submodule W
3. Recursively construct filtrations for W and V/W
4. Combine to get a filtration of V

# Context & Application

The Jordan-Holder theorem for modules ensures that the "building blocks" (composition factors) of any module are well-defined. For semisimple modules, the composition factors are exactly the simple direct summands (with multiplicity).

# Examples

**Example 1** (p. 105, 7.11): If V = V_1 + ... + V_s = W_1 + ... + W_t with all V_i, W_j simple, then s = t and there is a permutation sigma with V_i isomorphic to W_{sigma(i)}.

# Relationships

## Builds Upon
- **simple-module** — composition factors are simple modules

## Enables
- Uniqueness of decomposition into simple summands (7.11)

## Related
- **semisimple-module** — for semisimple modules, composition series = direct sum decomposition

## Contrasts With
- Jordan-Holder theorem for groups (same idea, different setting)

# Source Reference

Chapter 7: Representations of Finite Groups, Theorem 7.10 and Corollary 7.11, pp. 105-106.

# Verification Notes

- Definition source: Direct from Theorem 7.10
- Confidence rationale: HIGH — explicit theorem statement
- Uncertainties: None
