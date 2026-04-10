---
concept: Anisotropic Torus
slug: anisotropic-torus
category: multiplicative-groups
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 171
section: "14e Groups of multiplicative type"
extraction_confidence: high
aliases: []
prerequisites:
  - algebraic-torus
  - character-module
extends:
  - algebraic-torus
related:
  - split-torus
contrasts_with:
  - split-torus
answers_questions:
  - "What is an anisotropic torus?"
---

# Quick Definition

A torus T is anisotropic if X(T) = 0, i.e., it has no nontrivial characters defined over k. Equivalently, X*(T)^Gamma = 0. Every torus decomposes as T = T_s . T_a where T_s is split and T_a is anisotropic with T_s cap T_a finite.

# Core Definition

A torus T is *anisotropic* if X(T) = 0, i.e., if X*(T)^Gamma = 0 (Milne, p. 171). Corollary 14.26: every torus T has a largest split subtorus T_s and a largest anisotropic subtorus T_a, with T_s . T_a = T and T_s cap T_a finite.

# Prerequisites

- **Algebraic torus** -- Anisotropic is a property of tori
- **Character module** -- X*(T)^Gamma = 0 defines anisotropy

# Key Properties

1. X(T) = 0: no rational characters
2. Every torus T = T_s . T_a with T_s split, T_a anisotropic, T_s cap T_a finite
3. Over algebraically closed fields, all tori are split (so no anisotropic tori)
4. Over R, the circle group {z in C^x | |z| = 1} is anisotropic

# Examples

**Example 1** (p. 170): Over R, with X*(T) = Z and nontrivial Gamma-action m -> -m, T(R) = {z in C^x | z.z-bar = 1} is the unit circle, which is anisotropic (and compact!).

# Relationships

## Builds Upon
- **Algebraic torus** -- Anisotropic tori are a special case

## Contrasts With
- **Split torus** -- Has X*(T)^Gamma = X*(T) (all characters rational)

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 14e, page 171. Corollary 14.26.

# Verification Notes

- Definition source: Direct from text following Corollary 14.26
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
