---
concept: FG-Module
slug: fg-module
category: representation-theory
subcategory: linear-representations
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Representation Theory and Character Theory"
chapter_number: 18
pdf_page: 843
section: "18.1 Linear Actions and Modules over Group Rings"
extraction_confidence: high
aliases:
  - "representation module"
prerequisites:
  - group-ring
  - module
extends:
  - module
related:
  - representation
  - irreducible-representation
  - completely-reducible-module
contrasts_with: []
answers_questions:
  - "What is an FG-module?"
---

# Quick Definition
An FG-module is a module over the group ring FG, equivalently a vector space V over F equipped with a linear action of G. FG-submodules correspond to G-stable subspaces.

# Core Definition
An **FG-module** V is a left module over the group ring FG. Giving V the structure of an FG-module is equivalent to giving a representation φ: G → GL(V): the action of g ∈ G on v ∈ V is φ(g)(v) (p. 843). FG-submodules are precisely the G-stable (G-invariant) subspaces.

# Prerequisites
- **group-ring** — FG is the ring of scalars
- **module** — FG-modules are modules over FG

# Key Properties
1. FG-module ↔ pair (V, φ) where V is an F-vector space and φ: G → GL(V)
2. Submodules = G-stable subspaces
3. Quotient modules give quotient representations
4. Direct sums correspond to direct sums of representations

# Relationships
## Builds Upon
- **module** — FG-modules are a special case

## Enables
- **irreducible-representation** — Simple FG-modules
- **completely-reducible-module** — Semisimple FG-modules

# Source Reference
Chapter 18, Section 18.1, pages 843-845.

# Verification Notes
- Confidence: HIGH — bijection with representations explicitly stated
