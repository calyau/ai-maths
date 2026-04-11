---
concept: Factor Set
slug: factor-set
category: homological-algebra
subcategory: group-theory
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Homological Algebra and Group Cohomology"
chapter_number: 17
pdf_page: 825
section: "17.4 Group Extensions, Factor Sets and H^2(G,A)"
extraction_confidence: high
aliases:
  - "2-cocycle"
prerequisites:
  - group-extension
  - group-cohomology
extends: []
related:
  - crossed-homomorphism
contrasts_with: []
answers_questions:
  - "What is a factor set?"
---

# Quick Definition
A factor set (2-cocycle) is a function f: G × G → A satisfying the cocycle condition. Factor sets modulo coboundaries form H^2(G,A), classifying group extensions.

# Core Definition
A **factor set** (or 2-cocycle) is a function f: G × G → A satisfying the cocycle condition: gf(h,k) - f(gh,k) + f(g,hk) - f(g,h) = 0 for all g,h,k ∈ G (p. 825). The class of f in H^2(G,A) = Z^2/B^2 determines the equivalence class of the extension.

# Prerequisites
- **group-extension** — Factor sets encode extensions
- **group-cohomology** — Factor sets are 2-cocycles

# Key Properties
1. The cocycle condition ensures associativity of the extension
2. Coboundaries give equivalent extensions
3. f = 0 gives the split extension (semidirect product)

# Source Reference
Chapter 17, Section 17.4, pages 825-830.

# Verification Notes
- Confidence: HIGH — explicit definition with cocycle condition
